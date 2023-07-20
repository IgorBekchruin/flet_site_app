from flet import *


class Product(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True