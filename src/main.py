import flet
from flet import AppBar, Page, Text, ElevatedButton, View, colors

def main(page: Page):
    t = Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Chords"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton(" Go to Scales", on_click=lambda _: page.go("/scales")),
                ]
            )
        )
        if page.route == "/scales":
            page.views.append(
                View(
                    "/scales",
                    [
                        AppBar(title=Text("Scales"), bgcolor=colors.SURFACE_VARIANT),
                        ElevatedButton("Go to Chord", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

flet.app(target=main)