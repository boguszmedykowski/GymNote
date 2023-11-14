import flet as ft
from api.api_call import URL


def create_appbar(page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    appbar = ft.AppBar(
        leading_width=40,
        title=ft.FilledButton(text="GymNote", on_click=lambda _: page.go('/')),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.ElevatedButton(
                text="API", bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, url=f'{URL}/api/docs/'),
            ft.TextButton(
                text="github", url='https://github.com/boguszmedykowski/GymNote'),
            ft.FilledButton(
                text='Workouts', on_click=lambda _: page.go('/workouts')),
            ft.FilledButton(
                text="Login", on_click=lambda _: page.go('/login')),
            ft.FilledButton(text="Register",
                            on_click=lambda _: page.go('/register')),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ]
    )

    return appbar
