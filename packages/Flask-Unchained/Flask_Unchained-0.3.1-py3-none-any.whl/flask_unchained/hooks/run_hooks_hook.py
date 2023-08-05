import inspect
import networkx as nx

from collections import namedtuple
from flask import Flask
from importlib import import_module
from typing import *

from ..app_factory_hook import AppFactoryHook
from ..bundle import Bundle


HookTuple = namedtuple('HookTuple', ('Hook', 'store'))


class RunHooksHook(AppFactoryHook):
    """
    An internal hook to discover and run all the other hooks
    """
    bundle_module_name = 'hooks'

    def run_hook(self, app: Flask, bundles: List[Type[Bundle]]):
        for hook in self.collect_from_bundles(bundles):
            if hook.action_category and hook.action_table_columns:
                self.unchained.register_action_table(hook.action_category,
                                                     hook.action_table_columns,
                                                     hook.action_table_converter)
            hook.run_hook(app, bundles)
            hook.update_shell_context(self.unchained._shell_ctx)
            self.unchained.log_action('hook', hook)

        app.shell_context_processor(lambda: self.unchained._shell_ctx)

    def collect_from_bundles(self, bundles: List[Type[Bundle]],
                             ) -> List[AppFactoryHook]:
        hooks = self.collect_from_unchained()
        for bundle in bundles:
            hooks += self.collect_from_bundle(bundle)
        hook_tuples = self.resolve_hook_order(hooks)
        return [hook_tuple.Hook(self.unchained, hook_tuple.store)
                for hook_tuple in hook_tuples]

    def collect_from_unchained(self) -> List[HookTuple]:
        hooks_pkg = import_module('flask_unchained.hooks')
        return [HookTuple(Hook, None)
                for Hook in self._collect_from_package(hooks_pkg).values()]

    def collect_from_bundle(self, bundle: Type[Bundle]) -> List[HookTuple]:
        bundle_store = self.find_bundle_store(bundle)
        if bundle_store:
            bundle_store = bundle_store()
            self.unchained._bundle_stores[bundle.name] = bundle_store
        return [HookTuple(Hook, bundle_store)
                for Hook in super().collect_from_bundle(bundle).values()]

    def find_bundle_store(self, bundle):
        for bundle in bundle.iter_class_hierarchy():
            hooks_pkg = self.import_bundle_module(bundle)
            if hasattr(hooks_pkg, 'Store'):
                return hooks_pkg.Store

    def type_check(self, obj):
        is_class = inspect.isclass(obj) and issubclass(obj, AppFactoryHook)
        return is_class and obj not in {AppFactoryHook, RunHooksHook}

    def resolve_hook_order(self, hook_tuples: List[HookTuple],
                           ) -> List[HookTuple]:
        dag = nx.DiGraph()

        for hook_tuple in hook_tuples:
            dag.add_node(hook_tuple.Hook.name, hook_tuple=hook_tuple)
            for dep_name in hook_tuple.Hook.run_after:
                dag.add_edge(hook_tuple.Hook.name, dep_name)
            for successor_name in hook_tuple.Hook.run_before:
                dag.add_edge(successor_name, hook_tuple.Hook.name)

        try:
            order = reversed(list(nx.topological_sort(dag)))
        except nx.NetworkXUnfeasible:
            msg = 'Circular dependency detected between hooks'
            problem_graph = ', '.join([f'{a} -> {b}'
                                       for a, b in nx.find_cycle(dag)])
            raise Exception(f'{msg}: {problem_graph}')

        rv = []
        for hook_name in order:
            hook_tuple = dag.nodes[hook_name].get('hook_tuple')
            if hook_tuple:
                rv.append(hook_tuple)
        return rv
