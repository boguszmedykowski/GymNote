from flet import *
import flet as ft
from pages.login import Login
from pages.home import Home
from pages.register import Register
from elements.appbar import create_appbar


def views_handler(page: ft.Page):
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.update()
    return {
        '/': View(
            route='/',
            controls=[
                create_appbar(page),
                Home(page)
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
    }
