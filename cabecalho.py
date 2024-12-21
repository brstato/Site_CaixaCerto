import flet as ft
from urls import download

class Topo(ft.UserControl):
    def __init__(self):
        super().__init__()
        

    def build(self):
        return ft.Container(
            border=ft.Border(
                    bottom=ft.BorderSide(
                        width=0.5,
                        color=ft.colors.WHITE,
                    ),
                ),
            blur=10,
            bgcolor=ft.colors.WHITE12,    
            padding=ft.padding.all(5),
            content=ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value='Contato: ',
                                color=ft.colors.WHITE,
                                theme_style=ft.TextThemeStyle.BODY_LARGE,
                            ),
                            ft.TextButton(
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                        src='WhatsBranco512.png',
                                        width=24,
                                        height=24,
                                        ),

                                        ft.Text(
                                            value='Whatsapp',
                                            color=ft.colors.WHITE,
                                            ),
                                    ],
                                ),
                                url='https://web.whatsapp.com/send?phone=5524998564421',
                                
                            ),
                            ft.TextButton(
                                content=ft.Row(
                                    controls=[
                                        ft.Image(
                                        src='EmailBranco512.png',
                                        width=24,
                                        height=24,
                                        ),

                                        ft.Text(
                                            value='e-Mail',
                                            color=ft.colors.WHITE,
                                            ),
                                    ],
                                ),
                                url='mailto:brstatoo@hotmail.com',
                                
                            ),                            
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),           
                    ft.Container(expand=True),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5),
                                    bgcolor=ft.colors.GREY_900,
                                ),
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(
                                            ft.icons.DOWNLOAD,
                                            color=ft.colors.AMBER_800,                                  
                                        ),
                                        ft.Text(
                                            value='Download',
                                            color=ft.colors.AMBER_800,
                                        ),
                                    ],
                                ),
                                url=download,                        
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),                             
                ],
            ),
        )  