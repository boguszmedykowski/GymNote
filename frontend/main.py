import flet as ft
from flet import *
from api.api_call import *
from views import views_handler
from elements.appbar import *


def main(page: ft.Page):

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )
        pass

    # back
    def view_pop(e: ViewPopEvent):
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go('/')


ft.app(target=main, view=ft.WEB_BROWSER)
