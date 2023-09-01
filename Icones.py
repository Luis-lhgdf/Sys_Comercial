import customtkinter as ctk
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")  


MenuIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "menu_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "menu_light.png")), size=(20, 20))


HomeIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "home_light.png")),  size=(17, 17))


FotoPerfil = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "perfil.jpg")),
                    dark_image=Image.open(os.path.join(image_path, "perfil.jpg")), size=(100, 100))

img_apresentacao = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "apresentacao.jpg")),
                    dark_image=Image.open(os.path.join(image_path, "apresentacao.jpg")), size=(1500, 1125))



ExcelIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "excel.png")),
            dark_image=Image.open(os.path.join(image_path, "excel.png")), size=(30, 30))


EntradaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "entrada_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "entrada_light.png")), size=(17, 17))


SeuLogo2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "logo2.png")),
                    dark_image=Image.open(os.path.join(image_path, "logo2.png")), size=(130, 130))


EstoqueIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "estoque_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "estoque_light.png")), size=(17, 17))

CadastroIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "cadastro_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "cadastro_light.png")),  size=(17, 17))


AgendaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "agenda_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "agenda_light.png")), size=(17, 17))


carteiraIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "carteira_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "carteira_light.png")),  size=(17, 17))


UsuarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "usuario_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "usuario_light.png")), size=(17, 17))



UsuarioIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "usuario_light.png")),
                    dark_image=Image.open(os.path.join(image_path, "usuario_light.png")), size=(50, 50))


ConfiguracoesIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "configuracoes_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "configuracoes_light.png")), size=(17, 17))


EntradaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "entrada_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "entrada_light.png")), size=(17, 17))


SaidaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "saida_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "saida_light.png")), size=(17, 17))


InventarioIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "inventario_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "inventario_light.png")), size=(17, 17))



AdicionarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "adicionar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "adicionar_light.png")), size=(30, 30))


EditarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "editar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "editar_light.png")), size=(30, 30))


EditarIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "editar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "editar_light.png")), size=(17, 17))


sincronizar = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "sincronizar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "sincronizar_light.png")), size=(30, 30))


ItemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "item_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "item_light.png")), size=(17, 17))


VisualizarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "visualizar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "visualizar_light.png")), size=(17, 17))


VoltarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "voltar_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "voltar_light.png")), size=(30, 30))


FinancasIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "financas_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "financas_light.png")), size=(17, 17))


VendasIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "vendas_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "vendas_light.png")), size=(17, 17))


DespesaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "despesa_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "despesa_light.png")), size=(17, 17))



ReceitaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "receita_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "receita_light.png")), size=(17, 17))


FaturamentoIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "faturamento_black.png")),
                    dark_image=Image.open(os.path.join(image_path, "faturamento_light.png")), size=(17, 17))

GerenciarUserIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "gerenciarUser_black.png")),
            dark_image=Image.open(os.path.join(image_path, "gerenciarUser_light.png")), size=(17, 17))

DeletarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "deletar_black.png")),
    dark_image=Image.open(os.path.join(image_path, "deletar_light.png")), size=(30, 30))


DeletarIcon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "deletar_black.png")),
    dark_image=Image.open(os.path.join(image_path, "deletar_light.png")), size=(17, 17))


SalvarIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "salvar_black.png")),
    dark_image=Image.open(os.path.join(image_path, "salvar_light.png")), size=(30, 30))  


        
ImagemIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "imagem_black.png")),
    dark_image=Image.open(os.path.join(image_path, "imagem_light.png")), size=(17, 17))


            
SenhaIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "senha_black.png")),
    dark_image=Image.open(os.path.join(image_path, "senha_light.png")), size=(17, 17))



perfilIcon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "perfil.png")),
            dark_image=Image.open(os.path.join(image_path, "perfil.png")), size=(80, 80))



fundoLogin = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "fundologin.jpg")),
            dark_image=Image.open(os.path.join(image_path, "fundologin.jpg")),  size=(400, 450))


