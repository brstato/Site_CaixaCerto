import flet as ft

class Destaque(ft.UserControl):
    def __init__(self, titulo: str, conteudo: str, **kwargs):
        super().__init__(**kwargs)
        self.titulo = titulo
        self.conteudo = conteudo

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(
                        spans=[
                            ft.TextSpan(
                                text=self.titulo,
                                style=ft.TextStyle(
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),
                            ft.TextSpan(
                                text=self.conteudo,
                            ),
                        ],
                    ),
                ft.Divider(),     
            ],
        )  