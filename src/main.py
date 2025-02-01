import flet as ft
from flet import (AppBar, Page, Text, colors, TextField, FloatingActionButton, 
                 icons, margin, Column, Row, Dropdown, dropdown, PopupMenuItem, 
                 Icon, PopupMenuButton, Container, AlertDialog)
from search import search_song

def close_dialog(e):
    e.page.dialog.open = False
    e.page.update()

def search_clicked(e):
    titles = sorted([t[0] for t in search_song(e.control.value)])
    if not titles:
        dlg = AlertDialog(
            title=Text("Not Found!"),
            content=Text(f"No song containing the word '{e.control.value}'."),
            actions=[ft.TextButton("Ok", on_click=close_dialog)],
        )
        e.page.dialog = dlg
        e.page.dialog.open = True
        e.page.update()
        e.control.value = "Which song do you want to play?"
    else:
        dropdown = e.page.controls[0].controls[0].controls[0]
        dropdown.options = [dropdown.Option(t) for t in titles]
        dropdown.value = titles[0]
    e.page.update()

def select_song(e):
    song_name = e.page.controls[0].controls[2]
    song_name.value = e.control.value
    e.page.update()

def main(page: Page):
    page.title = "Chord Viewer"
    page.bgcolor = colors.BLUE_GREY_200
    
    # Create app bar
    appbar = AppBar(
        leading=Icon(icons.AUDIOTRACK),
        leading_width=100,
        title=Text("Chord View", size=32, text_align="start"),
        center_title=False,
        toolbar_height=75,
        bgcolor=colors.LIGHT_BLUE_ACCENT_700,
        actions=[
            Container(
                content=PopupMenuButton(
                    items=[
                        PopupMenuItem(text="About"),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(text="Settings")
                    ]
                ),
                margin=margin.only(left=50, right=25)
            )
        ],
    )
    
    # Initial song list
    titles = sorted([t[0] for t in search_song()])
    
    # Create UI elements
    songsearch = TextField(hint_text="Type song name", width=400, on_change=search_clicked)
    sngname = Text(" ", style="titleLarge")
    selection = Row([Text("Selected Song: ", style="titleMedium"), sngname])
    sdd = Dropdown(
        width=600,
        options=[dropdown.Option(t) for t in titles],
        on_change=select_song,
        autofocus=True,
        value=titles[0]
    )
    
    # Set up page layout
    page.appbar = appbar
    page.add(
        Column(
            width=600,
            controls=[
                Row(controls=[sdd]),
                Row(
                    controls=[
                        songsearch,
                        FloatingActionButton(icon=icons.SEARCH, on_click=search_clicked)
                    ]
                ),
                selection
            ]
        )
    )
    
    page.update()

ft.app(target=main)
