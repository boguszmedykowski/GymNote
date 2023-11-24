from flet import *
import flet as ft
from api.api_call import *


class Register(ft.UserControl):
    def __init__(self, page):
        super().__init__()

    def add_clicked(self, e):
        self.response.value = f"{register(name=self.name_field.value, email=self.email_field.value, password=self.password_field.value)}"
        self.login = get_token(email=self.email_field.value,
                               password=self.password_field.value)
        self.response.controls.append(ft.Text(value=self.response.value))
        self.email_field.value = ""
        self.update()
        if self.login == "Token obtained successfully. Status Code: 200":
            self.page.go('/workouts')
        else:
            pass

    def build(self):
        self.name_field = ft.TextField(
            label='name', hint_text='name', width=400)

        self.email_field = ft.TextField(
            label='email', hint_text="email", width=400)

        self.password_field = ft.TextField(
            label='password', hint_text="password", password=True, width=400)

        self.response = ft.Column()

        self.login_button = ft.FloatingActionButton(
            text="register", on_click=self.add_clicked)

        self.view = ft.Column(
            [
                ft.Row(
                    [
                        self.name_field,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        self.email_field,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        self.password_field,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        self.login_button,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        self.response,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ]
        )
        return self.view
