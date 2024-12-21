import flet as ft

class Titulo(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='Caixa',
                                    style=ft.TextStyle(
                                        color=ft.colors.GREY_100,
                                        
                                    ),
                                    
                                ),
                                ft.TextSpan(
                                    text='Certo',
                                    style=ft.TextStyle(
                                        color=ft.colors.AMBER_800,
                                        
                                    ),                                                    
                                ),
                            ],
                            theme_style=ft.TextThemeStyle.HEADLINE_LARGE,
                            size=80,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.alignment.center,
                    ),
                        
                    
                    ft.Container(
                        content=ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='Organize seu negócio e melhore seus lucros com ',
                                ),
                                ft.TextSpan(
                                    text='Caixa',
                                    style=ft.TextStyle(
                                            height=ft.FontWeight.BOLD,
                                            color=ft.colors.GREY_100,
                                        ),
                                    ),
                                ft.TextSpan(
                                    text='Certo',
                                    style=ft.TextStyle(
                                            height=ft.FontWeight.BOLD,
                                            color=ft.colors.AMBER_800,
                                        ),                                    
                                    ),                                
                                ft.TextSpan('.'),
                            ],
                            text_align=ft.TextAlign.CENTER,
                            size=14.5,
                        ),
                        alignment=ft.alignment.center,
                        offset=ft.Offset(x=0, y=-0.4),
                    ),
                ],
            ),
            alignment=ft.alignment.center,
        )    