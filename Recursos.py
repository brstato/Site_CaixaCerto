import flet as ft


class recursos(ft.UserControl):
    def __init__(self, Desc: str, Icone: bool, **kwargs):
        super().__init__(**kwargs)
        self.desc = Desc
        self.icone = Icone

    def build(self):
        return ft.Container(               
            content=ft.ResponsiveRow(                       
                controls=[


                    ft.Divider(5),

                    ft.Container(
                        col={'xs':8, 'md':8, 'xl':8},
                        content=ft.Text(
                            value=self.desc,
                            color=ft.colors.WHITE,
                            text_align=ft.CrossAxisAlignment.START,
                        )
                    ),
                    ft.Container(
                        col={'xs':4, 'md':4, 'xl':4},                      
                            content=ft.Icon(
                                    name=ft.icons.CHECK,
                                    color=ft.colors.AMBER_600,
                                    size=20,
                                )
                        if self.icone else 
                            ft.Text(
                                value='Em breve',
                                color=ft.colors.AMBER_600,
                                                                                    
                        )        
                    )
                ],
            )
            # bgcolor=ft.colors.BLACK45,
            # height=150, 
        )
        


       