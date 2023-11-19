import flet as ft
from api.api_call import URL


def create_appbar(page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def logout():
        pass

    appbar = ft.AppBar(
        leading_width=40,
        title=ft.IconButton(icon=ft.icons.HOME,
                            on_click=lambda _: page.go('/')),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.ElevatedButton(
                text="REST API", bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, url=f'{URL}/api/docs/'),
            ft.TextButton(
                text="github", url='https://github.com/boguszmedykowski/GymNote'),
            ft.FilledButton(
                text='Workouts', on_click=lambda _: page.go('/workouts')),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Sign in", on_click=lambda _: page.go('/login')),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Sign up", on_click=lambda _: page.go('/register')),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Logout", on_click=lambda _: page.go('/register')),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ]
    )

    return appbar
