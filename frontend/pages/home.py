from flet import *
import flet as ft
from api.api_call import get_workouts


class Counter(ft.UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def minus_click(self, e):
        self.counter -= 1
        self.text.value = str(self.counter)
        self.update

    def build(self):
        self.counter = 0
        self.text = ft.Text(str(self.counter))
        return ft.Row([
            ft.ElevatedButton("Add", on_click=self.minus_click),
            self.text,
            ft.ElevatedButton("Add", on_click=self.add_click)],
            alignment=ft.MainAxisAlignment.CENTER)
