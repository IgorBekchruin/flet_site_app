import flet
from flet import *

from pages.about import About
from pages.contatcs import Contact
from pages.home import Home
from pages.products import Product


class Main(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.init_help()

    def init_help(self):
        self.page.on_route_change = self.route_change
        self.page.go("/")

    def route_change(self, route):
        new_page = {
            "/": Home,
            "/products": Product,
            "/about": About,
            "/contacts": Contact,
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )


app(target=Main, assets_dir='assets', view=WEB_BROWSER)