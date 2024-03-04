import customtkinter as ctk
from PIL import Image
import os

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icon")



menu_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "menu_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "menu_light.png")), size=(20, 20))

home_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(17, 17))

profile_photo = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "profile.jpg")),
                          dark_image=Image.open(os.path.join(image_path, "profile.jpg")), size=(100, 100))

presentation_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "presentation.jpg")),
                                dark_image=Image.open(os.path.join(image_path, "presentation.jpg")), size=(1500, 1125))

excel_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "excel.png")),
                         dark_image=Image.open(os.path.join(image_path, "excel.png")), size=(30, 30))

entry_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "entry_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "entry_light.png")), size=(17, 17))

your_logo2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "logo2.png")),
                        dark_image=Image.open(os.path.join(image_path, "logo2.png")), size=(130, 130))

stock_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "stock_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "stock_light.png")), size=(17, 17))

register_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "register_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "register_light.png")), size=(17, 17))

agenda_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "agenda_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "agenda_light.png")), size=(17, 17))

wallet_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "wallet_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "wallet_light.png")), size=(17, 17))

user_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "user_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "user_light.png")), size=(17, 17))

user_icon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "user_light.png")),
                            dark_image=Image.open(os.path.join(image_path, "user_light.png")), size=(50, 50))

settings_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "settings_black.png")),
                                 dark_image=Image.open(os.path.join(image_path, "settings_light.png")),
                                 size=(17, 17))

exit_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "exit_black.png")),
                         dark_image=Image.open(os.path.join(image_path, "exit_light.png")), size=(17, 17))

inventory_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "inventory_black.png")),
                              dark_image=Image.open(os.path.join(image_path, "inventory_light.png")), size=(17, 17))

add_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_black.png")),
                             dark_image=Image.open(os.path.join(image_path, "add_light.png")), size=(30, 30))

edit_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "edit_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "edit_light.png")), size=(30, 30))

edit_icon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "edit_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "edit_light.png")), size=(17, 17))

update_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "update_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "update_light.png")), size=(30, 30))

item_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "item_black.png")),
                        dark_image=Image.open(os.path.join(image_path, "item_light.png")), size=(17, 17))

view_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "view_black.png")),
                              dark_image=Image.open(os.path.join(image_path, "view_light.png")), size=(17, 17))

back_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "back_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "back_light.png")), size=(30, 30))

finance_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "finance_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "finance_light.png")), size=(17, 17))

sales_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "sales_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "sales_light.png")), size=(17, 17))

expense_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "expense_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "expense_light.png")), size=(17, 17))

income_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "income_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "income_light.png")), size=(17, 17))

revenue_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "revenue_black.png")),
                               dark_image=Image.open(os.path.join(image_path, "revenue_light.png")), size=(17, 17))

manage_user_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "manageuser_black.png")),
                                 dark_image=Image.open(os.path.join(image_path, "manageuser_light.png")),
                                 size=(17, 17))

delete_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "delete_black.png")),
                           dark_image=Image.open(os.path.join(image_path, "delete_light.png")), size=(30, 30))

delete_icon2 = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "delete_black.png")),
                            dark_image=Image.open(os.path.join(image_path, "delete_light.png")), size=(17, 17))

save_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "save_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "save_light.png")), size=(30, 30))

image_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "image_black.png")),
                          dark_image=Image.open(os.path.join(image_path, "image_light.png")), size=(17, 17))

password_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "password_black.png")),
                         dark_image=Image.open(os.path.join(image_path, "password_light.png")), size=(17, 17))

profiledefault_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "profiledefault.png")),
                          dark_image=Image.open(os.path.join(image_path, "profiledefault.png")), size=(80, 80))

illustration_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "illustration.png")),
                          dark_image=Image.open(os.path.join(image_path, "illustration.png")), size=(400, 380))

linkedin_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "linkedin.png")),
                          dark_image=Image.open(os.path.join(image_path, "linkedin.png")), size=(60, 60))

github_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "github.png")),
                          dark_image=Image.open(os.path.join(image_path, "github.png")), size=(60, 60))

website_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "website.png")),
                          dark_image=Image.open(os.path.join(image_path, "website.png")), size=(60, 60))


alert_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "alert.png")),
                          dark_image=Image.open(os.path.join(image_path, "alert.png")), size=(30, 30))