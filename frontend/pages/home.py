from flet import *
import flet as ft
from api.api_call import get_workouts


def licznik(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(
        value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    return ft.Row(
        [
            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click=plus_click),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
