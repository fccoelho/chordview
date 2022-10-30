import flet
from flet import AppBar, Page, Text, ElevatedButton, \
    View, colors, TextField, FloatingActionButton, icons, \
    Row, Dropdown, dropdown

from sqlalchemy import create_engine

db = create_engine("sqlite:///leadsheets.sqlite")


def main(page: Page):
    def search_clicked(e):
        with db.connect() as conn:
            conn.execute("PRAGMA case_sensitive_like=OFF;")
            res = conn.execute(f"SELECT title from song where title like '%{song.value}%'")
            titles = res.fetchall()
        for t in titles:
            sdd.options.append(dropdown.Option(t[0]))
        page.update()
    def select_song(e):
        sngname.value = sdd.value
        page.update()
        # page.add(Row([Text("Selected Song: "),Text(f"{sdd.value}")]))
    song = TextField(hint_text="Which song do you want to play?", width=300)
    sngname = Text(" ", style="titleLarge")
    sel = Row([Text("Selected Song: ", style="titleMedium"), sngname])
    sdd = Dropdown(width=600, options=[], on_change=select_song)
    page.add(Text("Leadsheet Collection", style="displayLarge"))
    page.add(Row([sdd, song, FloatingActionButton(icon=icons.SEARCH, on_click=search_clicked)]),
             sel)

    page.update()




flet.app(target=main)
