import flet
from flet import AppBar, Page, Text, ElevatedButton, UserControl,\
    View, colors, TextField, FloatingActionButton, icons, margin, Column, \
    Row, Dropdown, dropdown, PopupMenuItem, Icon, PopupMenuButton, Container
from db import get_engine
from sqlalchemy import text


def search_song(query: str):
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("PRAGMA case_sensitive_like=OFF;"))
        res = conn.execute(text(f"SELECT title from song where title like '%{query}%'"))
        titles = res.fetchall()
    return titles


class ChordViewApp(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.appbar_items = [
            PopupMenuItem(text="About"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("Chord View", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )

        self.update()

    def search_clicked(self, e):
        titles = search_song(self.sngname.value)
        # print(titles)
        for t in titles:
            self.sdd.options.append(dropdown.Option(t[0]))
        self.sdd.value = titles[0][0]
        self.update()
    def select_song(self, e):
        self.sngname.value = self.sdd.value
        self.update()

    def build(self):
        self.song = TextField(hint_text="Which song do you want to play?", width=300)
        self.sngname = Text(" ", style="titleLarge")
        self.selection = Row([Text("Selected Song: ", style="titleMedium"), self.sngname])
        self.sdd = Dropdown(width=600, options=[], on_change=self.select_song)
        self.page.appbar = self.appbar
        self.search_view = Row(controls=[self.sdd, self.song, FloatingActionButton(icon=icons.SEARCH, on_click=self.search_clicked)])
        return Column(controls=[self.search_view, self.selection])




def main(page: Page):
    page.title = "Chord Viewer"
    page.bgcolor = colors.BLUE_GREY_200
    app = ChordViewApp(page)
    page.add(app)

    page.update()


flet.app(target=main)
