from flet import *
import flet as ft


class Counter(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.token = self.page.session.get('token')

    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.my_row.controls.append(
            ft.Text(value=f"{self.page.session.get('token')}"))
        self.update()

    def minus_click(self, e):
        self.counter -= 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        print(self.token)

        self.counter = 0
        self.text = ft.Text(str(self.counter))
        self.my_row = ft.Row(controls=[
            ft.ElevatedButton("-", on_click=self.minus_click),
            self.text,
            ft.ElevatedButton("+", on_click=self.add_click)],
            alignment=ft.MainAxisAlignment.CENTER)
        return self.my_row
