from flet import *
import flet as ft
from api.api_call import get_workouts


class Home(ft.UserControl):

    def build(self):
        self.text = ft.TextField(label="home site")
        self.workouts_button = ft.TextButton(
            text="Workouts", on_click=self.add_clicked)
        self.workouts_list = ft.Column()

        return ft.Column()

        # return ft.Column(
        #     [
        #         ft.Row(
        #             [self.workouts_button],
        #             alignment=ft.MainAxisAlignment.CENTER
        #         ),
        #         ft.Row(
        #             [self.workouts_list],
        #             alignment=ft.MainAxisAlignment.CENTER
        #         )

        #     ]
        # )

    def add_clicked(self, e):
        self.workouts_list.value = f"{get_workouts()}"
        self.workouts_list.controls.append(
            ft.Text(value=self.workouts_list.value))
        self.update()
