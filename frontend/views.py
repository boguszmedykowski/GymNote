from flet import *
import flet as ft
from login import Login
from home import Home
from register import Register
from appbar import create_appbar


def views_handler(page):
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
