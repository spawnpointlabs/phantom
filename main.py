from cProfile import label
from cgitb import text
from operator import truediv
from tkinter.font import BOLD
from turtle import position, title, window_width
import flet as ft
from pages import library

def main(page: ft.Page):
    
    page.title = "Hello world"
    navrail = ft.NavigationRail(
        
        destinations=[
            ft.NavigationRailDestination(label_content=ft.Text("Library", size=16), icon=ft.icons.GRID_VIEW_OUTLINED, selected_icon=ft.icons.GRID_VIEW_ROUNDED, padding=7),
            ft.NavigationRailDestination(label_content=ft.Text("Search", size=16), icon=ft.icons.SEARCH_OUTLINED, selected_icon=ft.icons.SEARCH, padding=7),
            ft.NavigationRailDestination(label_content=ft.Text("Settings", size=16          ), icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, padding=7),
        ],
        selected_index=0,
        min_width=80,
        min_extended_width=180,
        label_type=ft.NavigationRailLabelType.ALL,
        selected_label_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        extended=True
    )

    page.add(
        ft.Row(

            [
                navrail,
                library.libraryui

            ],
            expand=True
            
        ),

        
    )
    page.update()


ft.app(main)