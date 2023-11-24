from flet import *
import flet as ft
from pages.login import Login
from pages.home import Counter
from pages.register import Register
from pages.workouts import WorkoutsApp, EditWorkout, new_workout
from elements.appbar import create_appbar


def views_handler(page: ft.Page):
    return {
        '/': View(
            route='/',
            controls=[
                create_appbar(page),
                Counter()
            ]
        ),
        '/login': View(
            route='/login',
            controls=[
                create_appbar(page),
                Login(page)
            ]
        ),
        '/register': View(
            route='/register',
            controls=[
                create_appbar(page),
                Register(page)
            ]
        ),
        '/workouts': View(
            route='/workouts',
            controls=[
                create_appbar(page),
                WorkoutsApp(page)
            ]
        ),
        '/edit_workout': View(
            route='/edit_workout',
            controls=[
                create_appbar(page),
                EditWorkout(page)
            ]
        ),
        '/new_workout': View(
            route='/new_workout',
            controls=[
                create_appbar(page),
                new_workout(page)
            ]
        ),
    }
