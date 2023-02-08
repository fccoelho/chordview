import flet
from flet import AppBar, Page, Text, ElevatedButton, \
    View, colors, TextField, FloatingActionButton, icons, \
    Row, Dropdown, dropdown
from db import get_engine

def search_song(query: str):
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute("PRAGMA case_sensitive_like=OFF;")
        res = conn.execute(f"SELECT title from song where title like '%{query}%'")
        titles = res.fetchall()
    return titles

def main(page: Page):
    def search_clicked(e):
        titles = search_song(sngname.value)
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
