import flet as ft
from api.api_call import get_workouts, create_workout, get_workout


class WorkoutsApp(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

    def build(self):
        self.get_workouts_dict = get_workouts(self.page.session.get('token'))

        self.workout_title = ft.TextField(
            label='new workout title', hint_text='workout title', width=400)

        self.add_workout_button = ft.FloatingActionButton(
            text=" + ", on_click=lambda _: self.page.go("/new_workout")
        )

        self.workout_list = ft.Column(
            spacing=10,
            height=500,
            width=float("inf"),
            scroll=ft.ScrollMode.ALWAYS,
        )
        # if type(self.get_workouts_dict) != str:
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
                ft.Row([self.add_workout_button,
                        self.workout_title]),
                self.response,

                ft.Container(self.workout_list, border=ft.border.all(1)),
            ]
        )

    def workout_panel(self, e, id):
        self.page.session.set("trening_id", id)
        print(self.page.session.get("trening_id"), f"{id} ugagaga")
        self.page.go("/edit_workout")

    def add_workout_clicked(self, e):
        self.response.value = f"{create_workout(self.page.session.get('token'), title=self.workout_title.value)}'"

        self.response.controls.append(ft.Text(value=self.response.value))
        self.workout_title.value = ""
        self.update()


class EditWorkout(ft.UserControl):
    def __init__(self, page):
        super().__init__()

        self.page = page

    def build(self):
        self.id = self.page.session.get("trening_id")
        self.data = get_workout(self.page.session.get("token"),
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

    def build(self):

        self.view = ft.Column(
            [
                ft.Row([ft.TextField(label="title")],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ft.ElevatedButton(text="Add Exercise")],
                       alignment=ft.MainAxisAlignment.CENTER),
            ],
        )

        return self.view
