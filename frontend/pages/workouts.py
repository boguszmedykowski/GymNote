import flet as ft
from api.api_call import get_workouts, create_workout


class WorkoutsApp(ft.UserControl):
    def build(self):
        self.text = ft.TextField(label="home site")
        self.get_workouts_list = get_workouts()
        self.workouts_list = []

        for item in self.get_workouts_list:
            workout = ft.Container(
                content=ft.ElevatedButton(f"{item['title']}"),
                bgcolor=ft.colors.AMBER,
                padding=5
            )
            self.workouts_list.append(workout)

        self.workout_title = ft.TextField(
            label='title', hint_text='workout title', width=400)

        self.workouts = ft.Column(
            self.workouts_list
        )

        self.add_workout_button = ft.FloatingActionButton(
            text="Add Workout", on_click=self.add_clicked)

        self.response = ft.Column()
        return ft.Column(
            [
                ft.Row(
                    [
                        self.add_workout_button,
                        self.workout_title,
                        self.response
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        self.workouts,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )

            ]
        )

    def add_clicked(self, e):
        self.response.value = f"{create_workout(title=self.workout_title.value)}'"

        self.response.controls.append(ft.Text(value=self.response.value))
        self.workout_title.value = ""
        self.clean()
        self.build()
        self.update()
