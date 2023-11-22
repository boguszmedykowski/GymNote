from flet import *
import flet as ft
from api.api_call import get_workouts


class Home(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

    def build(self):

        cl = ft.Column(
            spacing=10,
            height=600,
            width=float("inf"),
            scroll=ft.ScrollMode.ALWAYS,
        )
        for i in range(0, 100):
            cl.controls.append(ft.Text(f"Text line {i}"))

        return ft.Column(
            [
                ft.Container(cl, border=ft.border.all(1)),
            ]
        )
