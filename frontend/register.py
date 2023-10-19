from flet import *
import flet as ft
from pages.api_call import *


class Register(UserControl):
    def build(self):
        self.name_field = ft.TextField(
            label='name', hint_text='name', expand=True)
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
                        self.name_field,
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
        self.response.value = f"'{self.email_field.value}', '{register(name=self.name_field.value, email=self.email_field.value, password=self.password_field.value)}"
        self.response.controls.append(ft.Text(value=self.response.value))
        self.email_field.value = ""
        self.update()
