from flet import *
import flet as ft
from pages.api_call import *


class Login(UserControl):
    def build(self):
        self.email_field = ft.TextField(
            label='email', hint_text="email", expand=True)
        self.password_field = ft.TextField(label='password',
                                           hint_text="password", expand=True, password=True)
        self.response = ft.Column()

        # application's root control (i.e. "view") containing all other controls
        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.email_field,
                        self.password_field,
                        ft.FloatingActionButton(
                            text="Login", on_click=self.add_clicked),
                    ],
                ),
                self.response,
            ],
        )

    def add_clicked(self, e):
        self.response.value = f"'{self.email_field.value}', '{get_token(email=self.email_field.value, password=self.password_field.value)}"
        self.response.controls.append(ft.Text(value=self.response.value))
        self.email_field.value = ""
        self.update()
