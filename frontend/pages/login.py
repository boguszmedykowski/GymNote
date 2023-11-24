from flet import *
import flet as ft
from api.api_call import *


class Login(UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

    def login_clicked(self, e):
        self.response.value = f"{get_token(email=self.email_field.value, password=self.password_field.value)}"
        # self.response.controls.append(ft.Text(value=self.response.value))
        self.email_field.value = ""
        self.page.session.set("token", self.response.value)
        self.snack_bar = ft.SnackBar(ft.Text(f"Hello"))
        self.snack_bar.open = True
        self.update()

        if self.response.value != "Error":
            self.page.go("/workouts")
        else:
            pass

    def build(self):
        self.snack_bar = ft.SnackBar(
            content=ft.Text("Hello, world!"),
            action="Alright!",
        )
        self.email_field = ft.TextField(
            label='email', hint_text="email", width=300)
        self.password_field = ft.TextField(label='password',
                                           hint_text="password", password=True, width=300)
        self.response = ft.Column()
        self.login_button = ft.ElevatedButton(
            text="Login", on_click=self.login_clicked)

        self.view = ft.Column(
            [
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="Sign in", on_click=lambda _: self.page.go('/register')),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
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
                self.snack_bar
            ]
        )
        return self.view
