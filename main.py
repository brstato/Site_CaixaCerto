import flet as ft
from content   import Content
from footer    import Footer
from cabecalho import Topo
from titulo    import Titulo
from descricao import Descricao

class App:
    def __init__(self, page: ft.Page):
        page.title = 'CaixaCerto - Gerenciamento Inteligente para seu negócio'
        self.page = page
        self.page.theme_mode=ft.ThemeMode.DARK
        self.main()

    def main(self):
        
        self.header    = Topo()
        self.titulo    = Titulo()
        self.content   = Content()
        self.descricao = Descricao()
        self.footer    = Footer()
        

        self.layout = ft.Container(
         
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[    
                    self.header,   

                    self.titulo,               

                    self.content, 

                    self.descricao,
                    
                    self.footer,          
                ],
                
                
            ), 
            expand=True,
            bgcolor=ft.colors.BLACK,
            image_fit=ft.ImageFit.COVER,
            image_opacity=0.5,
            blur=10,
            image_src='bnarios.jpg',
        )


        self.page.add(self.layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')