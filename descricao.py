import flet as ft
from urls import download
from conteudo_descricao import Destaque

class Descricao(ft.UserControl):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return ft.Container(
                bgcolor=ft.colors.WHITE12,
                padding=ft.padding.all(10),
                border_radius=ft.border_radius.all(10),
                border=ft.border.all(width=0.5, color=ft.colors.WHITE),
                blur=10,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='Caixa',
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.GREY_100,
                                    ),
                                ),
                                ft.TextSpan(
                                    text='Certo',
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.AMBER_800,
                                    ),
                                ),                                    
                                ft.TextSpan(
                                    text=': O Gerenciamento Inteligente que Seu Negócio Merece!',
                                ),
                            ],
                            size=18,
                        ),
                        ft.Text(
                            value='Transforme a administração do seu negócio com o CaixaCerto, '+
                            'o app perfeito para barbearias, salões de beleza e estúdios de tatuagem. '+
                            'Simplifique a gestão do seu empreendimento e aumente sua visibilidade com ',
                            spans= [
                                ft.TextSpan(
                                    text='Caixa',
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.GREY_100,
                                    ),
                                ),
                                ft.TextSpan(
                                    text='Certo',
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.colors.AMBER_800,
                                    ),
                                ),       
                                ft.TextSpan(
                                    text='.',
                                ),
                            ],    
                        ),    
                        ft.Text(
                            value='Funcionalidades Incríveis:',
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),      
                        Destaque('Gestão Eficiente: ','Controle financeiro, estoque, agendamentos e muito mais, tudo em um só lugar.'),
                        Destaque('Site Integrado: ','Crie sua presença online com uma site para o seu negócio, atraindo novos clientes e aumentando sua visibilidade.'),
                        Destaque('Agendamentos Online: ','Em breve, seus clientes poderão agendar serviços diretamente pela seu site.'),
                        Destaque('Marketing e Remarketing: ', 'Utilize estratégias de WhatsApp automatizado (disponível em breve) para manter seus clientes informados sobre promoções, novidades e lembretes de agendamentos.'),
                        Destaque('Relatórios Inteligentes com IA: ','Tenha insights sobre a saúde do seu negócio e receba sugestões de atividades que possam melhorar o faturamento, tudo com a ajuda da inteligência artificial.'),
                        ft.Text(
                            value='Benefícios que Você Vai Amar:',
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),   
                        Destaque('Facilidade de Uso: ','Interface intuitiva e fácil de usar, mesmo para quem não tem experiência com tecnologia.'),
                        Destaque('Aumento da Produtividade: ','Automatize tarefas administrativas e foque no que realmente importa: atender bem seus clientes.'),
                        Destaque('Crescimento do Negócio: ','Aumente sua base de clientes e fidelize os atuais com ferramentas de marketing eficazes.'),

                        ft.Text(
                            value='Oferta de Lançamento Imperdível: ',
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.AMBER_800,
                                size=20,
                            ),   
                        ),  
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='Preço Especial: ',
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                                ft.TextSpan(
                                    text='Aproveite o valor promocional de lançamento! De ',
                                ),    
                                ft.TextSpan(
                                    text='R$ 149,90 ',
                                    style=ft.TextStyle(color=ft.colors.AMBER_800),
                                ),      
                                ft.TextSpan(
                                    text='por apenas ',
                                ),    
                                ft.TextSpan(
                                    text='R$ 49,90 ',
                                    style=ft.TextStyle(color=ft.colors.AMBER_800),
                                ),   
                                ft.TextSpan(
                                    text='mensais. ',
                                ),                                                                                                                                                    
                            ],
                        ),   
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='Teste Grátis: ',
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ),
                                ft.TextSpan(
                                    text='Experimente o CaixaCerto por um mês, sem amarras e sem pegadinhas.',
                                ),                                
                            ],
                        ),
                        ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    col={'xs': 6, 'md': 10, 'lg': 10},
                                    content=ft.Text(
                                        spans=[
                                            ft.TextSpan(
                                                text='Baixe o '
                                            ),

                                            ft.TextSpan(
                                                text='Caixa',
                                                style=ft.TextStyle(
                                                    color=ft.colors.GREY_100,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                            ),
                                            ft.TextSpan(
                                                text='Certo ',
                                                style=ft.TextStyle(
                                                    color=ft.colors.AMBER_800,
                                                    weight=ft.FontWeight.BOLD,
                                                ),
                                            ),     
                                            ft.TextSpan(
                                                text='agora e leve seu negócio ao próximo nível!',
                                            ),                                       
                                        ],

                                        style=ft.TextStyle(
                                            weight=ft.FontWeight.BOLD,
                                            size=16,
                                        ),
                                    ),
                                    alignment=ft.alignment.center_left,
                                ),
                                # ft.Container(expand=True),
                                ft.Container(
                                    col={'xs': 6, 'md': 2, 'lg': 2},
                                    content=ft.ElevatedButton(
                                        icon=ft.icons.DOWNLOAD,
                                        text='Download',
                                        url=download,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                            color=ft.colors.AMBER_800,
                                        ),
                                        
                                    ),
                                    alignment=ft.alignment.center_right,
                                    margin=ft.margin.only(right=20),
                                ),
                            ],
                        ),                                                                     
                    ],
                ),
                margin=ft.margin.only(left=20, right=20),
        )    