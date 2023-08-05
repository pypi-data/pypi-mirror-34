from flask_unchained.bundles.controller import func, include

from .views import view_one, view_two


routes = [
    func(view_one),
    func(view_two),
    include('tests.bundles.controller.fixtures.vendor_bundle.routes'),
    include('tests.bundles.controller.fixtures.warning_bundle.routes'),
]
