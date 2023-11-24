import flet as ft
from api.api_call import create_workout, get_workouts, get_workout


class WorkoutsApp(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.token = self.page.session.get("token")

    def workout_panel(self, e, id):
        self.page.session.set("trening_id", id)
        print(self.page.session.get("trening_id"), f"{id}")
        self.page.go("/edit_workout")

    def add_workout_clicked(self, e):
        self.response.value = f"{create_workout(self.token, title=self.workout_title.value)}'"

        self.response.controls.append(ft.Text(value=self.response.value))
        self.workout_title.value = ""
        self.update()

    def build(self):
        self.get_workouts_dict = get_workouts(self.token)
        ft.FloatingActionButton(
            text=" + new wokout", on_click=lambda _: self.page.go("/new_workout")
        )
        self.workout_list = ft.Column(
            spacing=10,
            height=500,
            width=float("inf"),
            scroll=ft.ScrollMode.ALWAYS,
        )
        try:
            for i in self.get_workouts_dict:
                self.workout_list.controls.append(
                    ft.ElevatedButton(
                        text=f"{i['title']}",
                        on_click=lambda e, id=i['id']: self.workout_panel(
                            e, id)
                    )
                )
        except:
            pass
        self.response = ft.Column()

        return ft.Column(
            [
                ft.Row([
                    ft.FloatingActionButton(
                        text="new wokout", width=150, on_click=lambda _: self.page.go("/new_workout")
                    )
                ],
                    alignment=ft.MainAxisAlignment.CENTER),
                self.response,

                ft.Row([self.workout_list],
                       alignment=ft.MainAxisAlignment.CENTER),
            ]
        )


class EditWorkout(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.token = self.page.session.get("token")

    def build(self):
        self.id = self.page.session.get("trening_id")
        self.data = get_workout(self.token,
                                self.id)

        self.title = self.data["title"]
        self.exercises = self.data["exercises"]
        self.view = ft.Column(
            [
                ft.Row([ft.TextField(value=f"{self.title}")],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text(value=f"{self.exercises}")],
                       alignment=ft.MainAxisAlignment.CENTER),
            ],
        )

        return self.view


class NewWorkout(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.token = self.page.session.get("token")

    def add_exercise(self, e):
        self.exercise_field = ft.TextField(
            hint_text="exercise name", label=" exercise name")
        self.exercises_column.controls.append(
            ft.Row([self.exercise_field],
                   alignment=ft.MainAxisAlignment.CENTER)
        )
        self.update()

    def save(self, e):
        for row in self.exercises_column.controls:
            for text in row.controls:
                self.exercise_list.append({"name": text.value,
                                           "description": ""})

        response = create_workout(self.token,
                                  self.workout_title.value,
                                  self.exercise_list)
        print(response)
        if response == 201:
            self.page.go('/workouts')

    def build(self):
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.workout_title = ft.TextField(
            hint_text="workout title", label=" workout title")
        self.exercises_column = ft.Column([])
        self.exercise_list = []

        return ft.Column(
            [
                ft.Row([self.workout_title],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.ElevatedButton(text=" + exercise",
                                          on_click=self.add_exercise),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                self.exercises_column,
                ft.Row([ft.ElevatedButton(text="save", on_click=self.save)],
                       alignment=ft.MainAxisAlignment.CENTER)

            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
