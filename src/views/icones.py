import customtkinter as ctk
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")

menu_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "menu_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "menu_light.png")), size=(20, 20))

home_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(17, 17))

profile_photo = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "perfil.jpg")),
                          dark_image=Image.open(os.path.join(image_path, "perfil.jpg")), size=(100, 100))

presentation_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "apresentacao.jpg")),
                                dark_image=Image.open(os.path.join(image_path, "apresentacao.jpg")), size=(1500, 1125))

excel_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "excel.png")),
                         dark_image=Image.open(os.path.join(image_path, "excel.png")), size=(30, 30))

entry_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "entrada_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "entrada_light.png")), size=(17, 17))

your_logo2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "logo2.png")),
                        dark_image=Image.open(os.path.join(image_path, "logo2.png")), size=(130, 130))

stock_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "estoque_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "estoque_light.png")), size=(17, 17))

register_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "cadastro_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "cadastro_light.png")), size=(17, 17))

agenda_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "agenda_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "agenda_light.png")), size=(17, 17))

wallet_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "carteira_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "carteira_light.png")), size=(17, 17))

user_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "usuario_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "usuario_light.png")), size=(17, 17))

user_icon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "usuario_light.png")),
                            dark_image=Image.open(os.path.join(image_path, "usuario_light.png")), size=(50, 50))

settings_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "configuracoes_black.png")),
                                 dark_image=Image.open(os.path.join(image_path, "configuracoes_light.png")),
                                 size=(17, 17))

entry_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "entrada_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "entrada_light.png")), size=(17, 17))

exit_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "saida_black.png")),
                         dark_image=Image.open(os.path.join(image_path, "saida_light.png")), size=(17, 17))

inventory_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "inventario_black.png")),
                              dark_image=Image.open(os.path.join(image_path, "inventario_light.png")), size=(17, 17))

add_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "adicionar_black.png")),
                             dark_image=Image.open(os.path.join(image_path, "adicionar_light.png")), size=(30, 30))

edit_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "editar_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "editar_light.png")), size=(30, 30))

edit_icon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "editar_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "editar_light.png")), size=(17, 17))

synchronize_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "sincronizar_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "sincronizar_light.png")), size=(30, 30))

item_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "item_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "item_light.png")), size=(17, 17))

view_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "visualizar_black.png")),
                              dark_image=Image.open(os.path.join(image_path, "visualizar_light.png")), size=(17, 17))

back_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "voltar_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "voltar_light.png")), size=(30, 30))

finance_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "financas_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "financas_light.png")), size=(17, 17))

sales_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "vendas_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "vendas_light.png")), size=(17, 17))

expense_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "despesa_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "despesa_light.png")), size=(17, 17))

income_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "receita_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "receita_light.png")), size=(17, 17))

revenue_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "faturamento_black.png")),
                               dark_image=Image.open(os.path.join(image_path, "faturamento_light.png")), size=(17, 17))

manage_user_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "gerenciarUser_black.png")),
                                 dark_image=Image.open(os.path.join(image_path, "gerenciarUser_light.png")),
                                 size=(17, 17))

delete_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "deletar_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "deletar_light.png")), size=(30, 30))

delete_icon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "deletar_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "deletar_light.png")), size=(17, 17))

save_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "salvar_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "salvar_light.png")), size=(30, 30))

image_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "imagem_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "imagem_light.png")), size=(17, 17))

password_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "senha_black.png")),
                         dark_image=Image.open(os.path.join(image_path, "senha_light.png")), size=(17, 17))

profile_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "perfil.png")),
                          dark_image=Image.open(os.path.join(image_path, "perfil.png")), size=(80, 80))

illustration_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "illustration.png")),
                          dark_image=Image.open(os.path.join(image_path, "illustration.png")), size=(400, 380))

linkedin_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "linkedin.png")),
                          dark_image=Image.open(os.path.join(image_path, "linkedin.png")), size=(60, 60))

github_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "github.png")),
                          dark_image=Image.open(os.path.join(image_path, "github.png")), size=(60, 60))

website_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "site.png")),
                          dark_image=Image.open(os.path.join(image_path, "site.png")), size=(60, 60))


alert_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "alert.png")),
                          dark_image=Image.open(os.path.join(image_path, "alert.png")), size=(30, 30))