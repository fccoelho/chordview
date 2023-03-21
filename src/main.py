import flet as ft
from flet import (AppBar, Page, Text, ElevatedButton, UserControl,
    View, colors, TextField, FloatingActionButton, icons, margin, Column,
    Row, Dropdown, dropdown, PopupMenuItem, Icon, PopupMenuButton, Container,
    AlertDialog)
from search import search_song
from tabs import build_tabs


class ChordViewApp(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.dlg = AlertDialog(
            title=Text("Not Found!"),
            content = Text(""),
            actions= [ft.TextButton("Ok", on_click=self.close_dialog)],
            on_dismiss=lambda e: 1
        )
        self.appbar_items = [
            PopupMenuItem(text="About"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar = AppBar(
            leading=Icon(icons.AUDIOTRACK),
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
        titles = sorted([t[0] for t in search_song(self.song.value)])
        if not titles:
            self.dlg.content = Text(f"No song containing the word '{self.song.value}'.")
            self.page.dialog = self.dlg
            self.page.dialog.open = True
            self.page.update()
        else:
            self.sdd.value = titles[0]
        self.update()

    def close_dialog(self, e):
        self.dlg.open = False
        self.song.value = "Which song do you want to play?"
        self.page.update()
        self.update()
    def select_song(self, e):
        self.sngname.value = self.sdd.value
        self.update()

    def build(self):
        ''' Build the GUI '''
        titles = sorted([t[0] for t in search_song()])
        self.song = TextField(hint_text="Which song do you want to play?", width=400)
        self.sngname = Text(" ", style="titleLarge")
        self.selection = Row([Text("Selected Song: ", style="titleMedium"), self.sngname])
        self.sdd = Dropdown(width=600, options=[dropdown.Option(t) for t in titles], 
                            on_change=self.select_song, autofocus=True,
                            value=titles[0])
        self.page.appbar = self.appbar
        self.search_view = Row(controls=[self.sdd, self.song, FloatingActionButton(icon=icons.SEARCH, on_click=self.search_clicked)])
        return Column(controls=[self.search_view, self.selection])




def main(page: Page):
    page.title = "Chord Viewer"
    page.bgcolor = colors.BLUE_GREY_200
    app = ChordViewApp(page)
    page.add(app)

    page.update()


ft.app(target=main)
