import flet as ft
from Recursos import recursos, recursos
from carouusel import Carousel 
from urls import download

class Depoimentos(ft.UserControl):
    def __init__(self, user: str, job: str, depoimento: str, image: str = 'testimonial-default.jpg', **kwargs):
        super().__init__(**kwargs)
        self.user = user
        self.job = job
        self.depoimento = depoimento
        self.image = image

    def build(self):
        return ft.Stack(
            controls=[  
                ft.Stack(
                    controls=[
                        ft.Container(
                            blur=10, 
                            border_radius=ft.border_radius.all(10),
                            border=ft.border.all(width=0.5, color=ft.colors.WHITE),
                            height=200,
                            width=400,
                            offset=ft.Offset(x=0.05, y=0.1),
                        ),
                        ft.Container(
                            # 
                            height=200,
                            width=400,                            
                            border_radius=ft.border_radius.all(10),
                            bgcolor=ft.colors.WHITE12,  
                            
                            padding=ft.padding.all(30),
                            margin=ft.margin.all(20),
                            
                        
                            content=ft.Stack(
                                controls=[
                                    ft.Column(
                                    
                                        controls=[
                                            ft.Text(
                                                value=self.user,
                                                theme_style=ft.TextThemeStyle.LABEL_LARGE,
                                                color=ft.colors.WHITE,
                                            ),
                                            ft.Text(
                                                value=self.job,
                                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                                color=ft.colors.WHITE,
                                                italic=True,
                                            ),
                                            ft.Text(
                                                value=self.depoimento,
                                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                                color=ft.colors.WHITE,
                                                text_align=ft.alignment.center_left,
                                            ),
                                            # ft.Divider(height=20),
                                            # ft.Container(
                                            #     content=ft.Row(
                                            #         controls=[
                                            #             ft.Icon(
                                            #                 name=ft.icons.STAR,
                                            #                 color=ft.colors.AMBER_800,
                                            #                 size=15,
                                            #             ),
                                            #             ft.Icon(
                                            #                 name=ft.icons.STAR,
                                            #                 color=ft.colors.AMBER_800,
                                            #                 size=15,
                                            #             ),
                                            #                                                     ft.Icon(
                                            #                 name=ft.icons.STAR,
                                            #                 color=ft.colors.AMBER_800,
                                            #                 size=15,
                                            #             ),
                                            #             ft.Icon(
                                            #                 name=ft.icons.STAR,
                                            #                 color=ft.colors.AMBER_800,
                                            #                 size=15,
                                            #             ),
                                            #             ft.Icon(
                                            #                 name=ft.icons.STAR,
                                            #                 color=ft.colors.AMBER_800,
                                            #                 size=15,
                                            #             ),                                                                                                                        
                                            #         ],
                                            #         tight=True,
                                            #     ),
                                            #     padding=ft.padding.symmetric(vertical=5, horizontal=10),
                                            #     border_radius=ft.border_radius.all(50),
                                            # )

                                        ]
                                    ),
                                ],
                            ) 
                        ), 
                        ft.Image(
                            src=self.image,
                            border_radius=ft.border_radius.all(100),
                            width=100,
                            top=0,
                            right=0,
                            offset=ft.Offset(x=-0.4, y=0),                            
                        ),                                               
                    ],
                ), 
            ],
        ) 
    
       

class Content(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        banner = ft.Container(
            offset=ft.Offset(x=0, y=-0.01),
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            image_opacity=0.5,
            margin=ft.margin.only(top=10, left=10, right=10,),
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.ResponsiveRow(
                    
                    offset=ft.Offset(x=0, y=0),
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    
                    controls=[
                        ft.Column(
                            col={'xs': 12, 'md': 12, 'lg': 8},
                            controls=[
                                ft.Container(
                                                                
                                    content=ft.Image(
                                        src='screenshot051220242.png',
                                        fit=ft.Offset(
                                            x=120,
                                            y=40
                                            ),    
                                        ),
                                                                    
                                    shadow=ft.BoxShadow(
                                        color=ft.colors.BLACK45,
                                        blur_radius=100,
                                        offset=ft.Offset(x=20, y=20),
                                        spread_radius=-50,
                                    
                                        
                                    ),
                                    alignment=ft.alignment.center_left,
                                                            
                                ),

                            ]
                        ),
                       
                        ft.Container(
                            col={'xs': 12, 'md': 12, 'lg': 4},
                            padding=ft.padding.only(left=10, right=10),
                            content=ft.Column(
                                controls=[                                 
                                    ft.Container(                       
                                        content=ft.ResponsiveRow(                                             
                                            col=12,                                                                                      
                                            controls=[
                                                ft.Container(                                                   
                                                    content=ft.ResponsiveRow(
                                                        columns=12,
                                                        controls=[
                                                            ft.Container(
                                                                col={'xs': 6, 'md': 6, 'lg': 6, 'xl': 6},
                                                                content=ft.Column(
                                                                    controls=[
                                                                        ft.Text(
                                                                            value='Oferta de lançamento: ',
                                                                            weight=ft.FontWeight.BOLD,
                                                                            size=16,
                                                                            color=ft.colors.AMBER_800,
                                                                            
                                                                        ),
                                                                        ft.Text(
                                                                            value='de ',
                                                                            size=16,
                                                                            spans=[
                                                                                ft.TextSpan(
                                                                                    text='R$ ',
                                                                                ),
                                                                                ft.TextSpan(
                                                                                    text='149,90 ',
                                                                                    style=ft.TextStyle(
                                                                                        color=ft.colors.AMBER_800,
                                                                                    )
                                                                                ),
                                                                                ft.TextSpan(
                                                                                    text='por mês',
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        ft.Text(
                                                                            value='',
                                                                            size=16,
                                                                        ),
                                                                    ],

                                                                ),

                                                                alignment=ft.alignment.center_left,
                                                            ),

                                                            ft.Container(
                                                                col           = {'xs': 6, 'md': 6, 'lg': 6},
                                                                bgcolor       = ft.colors.ORANGE_800,
                                                                alignment     = ft.alignment.top_right,
                                                                padding       = ft.padding.all(10),
                                                                border_radius = ft.border_radius.only(bottom_left=10),                                                                                                                     
                                                                offset        = ft.Offset(x=0.65,y=-0.20),
                                                                border        = ft.border.all(width=1, color=ft.colors.WHITE70),   
                                                                margin        = ft.margin.only(left=-100, bottom=-20, right=110),
                                                                opacity=0.8,
                                                                content   = ft.ResponsiveRow(
                                                                    columns  = 12,
                                                                    controls = [                                                                     
                                                                        ft.Text(            
                                                                            value      = 'Por 49,90 mês',
                                                                            color      = ft.colors.WHITE,
                                                                            weight     = ft.FontWeight.BOLD,
                                                                            text_align = ft.alignment.center,
                                                                            size       = 24,
                                                                        ),                                                                       
                                                                    ],
                                                                ),
                                                                
 
                                                                shadow=ft.BoxShadow(
                                                                    blur_radius = 30,                 
                                                                    color       = ft.colors.WHITE30,
                                                                ),
                                                                
                                                            ),

                                                        ],
                                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                                    ),
                                                    
                                                    height=75,                                                                                                                                                                                   
                                                ),                                                

                                                recursos('Controle de loja', True),
                                                recursos('Interface amigavel e de fácil uso', True),
                                                recursos('Sem amarras, cancele quando quiser', True),
                                                recursos('Sem necessidade de cartões de crédito, pague via pix', True),
                                                recursos('Suporte fácil, nos chame pelo whatsapp', True),
                                                recursos('Não precisa de internet para funcionar', True),
                                                recursos('Site para sua loja integrado a sua agenda, seja mais visto, venda mais', False),
                                                recursos('Bot de atendimento para whatsapp, campanhas, vendas e muito mais...', False),
                                                recursos('Integração com IA, tenha seus relatorios explicados por nosa IA, e receba insights de como melhorar seu faturamento', False),
                                                recursos('Dispositivos móveis, IOS e android, tenha todas informações na palma da sua mão', False),        
                                                                                                
                                                                                                                                                                                                                                                                                                                            
                                            ], 
                                            alignment   = ft.MainAxisAlignment.CENTER,   
                                            offset      = ft.Offset(x=0, y=0),
                                            run_spacing = 5,              
                                                                                                                      
                                        ),                                        
                                        
                                        bgcolor       = ft.colors.GREY_900,    
                                        border_radius = 10,    
                                        padding       = ft.padding.all(5),   
                                    ),                                    

                                    ft.ElevatedButton(
                                        url=download,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=5), 
                                            bgcolor=ft.colors.AMBER_900,
                                            
                                        ),
                                        
                                        content=ft.Row(
                                            
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.DOWNLOAD,
                                                    color=ft.colors.WHITE,   
                                                ), 
                                                ft.Text(
                                                    value='Experimente gratis',
                                                    size=28,
                                                    color=ft.colors.WHITE,
                                                    weight=ft.FontWeight.BOLD,
                                                ),                                               
                                                
                                            ],
                                            tight=True,
                                        ),
                                    )
                                ],
                            ),
                            alignment=ft.alignment.center,
                        ),   

                        Carousel(
                            controls=[
                                Depoimentos(
                                    user='Bruno Ribeiro',
                                    job='@brunoribeiro.tatuador',
                                    depoimento='Sou tatuador e as vezes me perdia com meu faturamento, ou clientes '+
                                                'que eu deveria entrar em contato, o app CaixaCerto '+
                                                'me judou muito',
                                    image='bruno.png'
                                ),     
                                Depoimentos(
                                    user='Maicon Jesus',
                                    job='Barbearia Tropa',
                                    depoimento='Me ajudou muito, organizou minha agenda, comissões, estoque...',
                                    image='tropa.png'
                                ),
                                Depoimentos(
                                    user='Elza Ribeiro',
                                    job='Elza piercer',
                                    depoimento='App muito bom, facil de usar, usamos no estudio atualmente, conseguimos ter uma boa noção de quem são os nossos clientes',
                                    image='elza.png'
                                ),                                                                                                           
                            ],
                        ),                                            
                    ],
                    
                ),],
            ),    
                
        )
        return banner    