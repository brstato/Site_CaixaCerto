import flet as ft
from typing import List


class Carousel(ft.UserControl):
    def __init__(self, controls: List[ft.Control], height: int = 250, **kwargs):
        super().__init__(**kwargs)
        self.controls = controls
        self.carousel = None

    def mover(self, e, Delta: int = 0):
        if self.carousel:
            self.carousel.scroll_to(
                delta=Delta,
                duration=300,
                curve=ft.AnimationCurve.DECELERATE
            )    
            self.carousel.update()

    def build(self):
        self.carousel = ft.Row(
            height=self.height,
            scroll=ft.ScrollMode.AUTO,
            controls=self.controls,
        )
        return ft.Column(
            controls=[
                self.carousel,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_LEFT,
                            on_click=lambda e: self.mover(e, -100),
                        ),
                        ft.IconButton(
                            icon=ft.icons.KEYBOARD_ARROW_RIGHT,
                            on_click=lambda e: self.mover(e, 100),
                        ),
                    ],
                    
                    
                )
            ]
        )