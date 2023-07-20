import flet
from flet import *


class Home(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.page.title = 'Главная'
        # self.page.theme = 'light'
        self.content = Column(
            scroll=ScrollMode.AUTO,
            spacing=0,
            controls=[
                Container(
                    height=70,
                    bgcolor='black',
                    border=border.only(bottom=border.BorderSide(5, 'grey')),
                    content=Row(
                        alignment='spaceBetween',
                        controls=[
                            Row(
                                controls=[
                                    Container(
                                        width=70,
                                        height=70,
                                        bgcolor='green',
                                        border=border.only(right=border.BorderSide(5, 'grey'))
                                    ),
                                    Image(
                                        src='logo.png'
                                    )
                                ]
                            ),
                            Row(
                                alignment='center',
                                controls=[
                                    TextButton(
                                        content=Container(
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        'Главная',
                                                        color='white'
                                                    )
                                                ]
                                            )
                                        )
                                    ),
                                    TextButton(
                                        content=Container(
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        'Продукция',
                                                        color='white'
                                                    )
                                                ]
                                            )
                                        )
                                    ),
                                    TextButton(
                                        content=Container(
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        'О нас',
                                                        color='white'
                                                    )
                                                ]
                                            )
                                        )
                                    ),
                                    TextButton(
                                        content=Container(
                                            content=Row(
                                                controls=[
                                                    Text(
                                                        'Контакты',
                                                        color='white'
                                                    )
                                                ]
                                            )
                                        )
                                    ),
                                ]
                            )
                        ]
                    )
                ),

                Container(
                    content=Stack(

                        controls=[
                            Row(
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    Image(
                                        height=900,
                                        width=1400,
                                        fit=ImageFit.COVER,
                                        src="banner.png",
                                    ),
                                ]
                            ),
                            Container(
                                padding=padding.only(top=300),
                                alignment=alignment.center,
                                content=Text(
                                    'ОРИОН',
                                    color='white',
                                    size=70,
                                    weight=FontWeight.W_800,
                                )
                            ),
                            Container(
                                padding=padding.only(top=400),
                                alignment=alignment.center,
                                content=Text(
                                    'ПРОИЗВОДСТВО ФАНЕРЫ, ГНУТОКЛЕЕНЫХ ДЕТАЛЕЙ И ПИЛОМАТЕРИАЛОВ',
                                    color='white',
                                    size=30,
                                    weight=FontWeight.W_300,
                                )
                            )
                        ]
                    )
                ),

                Container(
                    padding=padding.only(left=100, top=20, right=100, bottom=20),
                    bgcolor='lightgrey',
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Container(
                                width=500,
                                height=400,
                                content=Text(
                                    'НАШЕ ПРОИЗВОДСТВО',
                                     color='black'
                                )
                            ),
                            Container(
                                width=500,
                                height=400,
                                bgcolor='green',
                                content=Text(
                                    'ООО «Орион» специализируется на производстве фанеры, гнутоклееных деталей и '
                                    'пиломатериалов. Мы являемся сертифицированным производителем, это значит, '
                                    'что мы не выступаем посредниками в сделке, что даёт вам дополнительные гарантии '
                                    'в сотрудничестве. Вся наша продукция производится на бразильских станках Fezer и '
                                    'тайваньских станках Takayama. За короткий срок предприятие освоило и сохраняет '
                                    'позиции как на внутреннем, так и на мировом рынке. В 2020 году пущено в работу '
                                    'производство широкоформатной фанеры 4×8 на бразильском и тайваньском оборудовании',
                                    color='white'
                                )
                            )
                        ]
                    )
                )
            ]
        )
