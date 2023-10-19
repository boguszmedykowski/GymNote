import flet as ft


def create_appbar(page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    appbar = ft.AppBar(
        leading_width=40,
        title=ft.FilledButton(text="Gymnote", on_click=lambda _: page.go('/')),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.FilledButton(
                text="Login", on_click=lambda _: page.go('/login')),
            ft.FilledButton(text="Register",
                            on_click=lambda _: page.go('/register')),  # Wywołanie funkcji po kliknięciu
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
