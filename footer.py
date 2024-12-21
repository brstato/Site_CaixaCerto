import flet as ft

class Footer(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
            bgcolor=ft.colors.WHITE12,
            blur=10,
            padding=ft.padding.symmetric(vertical=10, horizontal=50),
            content=ft.Row(
                controls=[
                    ft.Container(
                        col={'xs': 6, 'md': 6, 'xl': 6},
                        content=ft.Text(
                            value='₢ 2024 Todos os direitos reservados.',
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                            text_align=ft.TextAlign.START,
                            color=ft.colors.WHITE,
                        )
                    ),
                    ft.Container(
                        col={'xs': 6, 'md': 6, 'xl': 6},
                        alignment=ft.alignment.center_right,  # Alinha o conteúdo à direita
                        content=ft.Text(
                            spans=[
                                ft.TextSpan(text='Contato: '),
                                ft.TextSpan(
                                    text='brstatoo@hotmail.com',
                                    url='mailto:brstatoo@hotmail.com',
                                ),
                            ],
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                            color=ft.colors.WHITE,
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Garante que os itens estejam nas extremidades
            )
        )
