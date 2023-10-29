from flet import *
import flet as ft
from api.api_call import *


class Login(UserControl):
    def build(self):
        self.email_field = ft.TextField(
            label='email', hint_text="email", width=400)
        self.password_field = ft.TextField(label='password',
                                           hint_text="password", password=True, width=400)
        self.response = ft.Column()
        self.login_button = ft.FloatingActionButton(
            text="Login", on_click=self.add_clicked)

        self.view = ft.Column(
            [
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

    def add_clicked(self, e):
        self.response.value = f"'{self.email_field.value}', '{get_token(email=self.email_field.value, password=self.password_field.value)}"
        self.response.controls.append(ft.Text(value=self.response.value))
        self.email_field.value = ""
        self.update()
