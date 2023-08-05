import click

from flask.cli import cli


@cli.command()
def vendor_top_level():
    """vendor_bundle docstring"""
    click.echo('vendor_bundle')


# this group will have its baz command overridden
@click.group()
def foo_group():
    """vendor_bundle docstring"""


# this group should get overridden by the myapp bundle
@click.group()
def goo_group():
    """vendor_bundle docstring"""


@foo_group.command()
def bar():
    """vendor_bundle docstring"""
    click.echo('vendor_bundle')


@foo_group.command()
def baz():
    """vendor_bundle docstring"""
    click.echo('vendor_bundle')


@goo_group.command()
def gar():
    """vendor_bundle docstring"""
    click.echo('vendor_bundle')


@goo_group.command()
def gaz():
    """the overridden group should not contain this command"""
    click.echo('vendor_bundle')
