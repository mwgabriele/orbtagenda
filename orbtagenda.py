from textual.app import App
from textual.screen import Screen
from textual.widgets import (Static, Label, Input, Button, Header, Footer,
                            TextArea, ListView, ListItem, Log, 
                            Pretty, Rule, DataTable, Welcome)
from textual.containers import Horizontal
from textual.binding import Binding

from OrbtScreens import *

class TelaListagem(Screen):
    def compose(self):
        yield Pretty(OrbtAgenda.AGENDA)

class OrbtAgenda(App):

    BINDINGS = [
        Binding(key="d", action="push_screen('tela_lista')", description="Lista"),
        Binding(key="ctrl+q", action="quit", description="Sair"),
        Binding(key="escape", action="quit", description="Sair", show=False)
    ]

    AGENDA = {
        "nome@email.com": {
            "nome": "Nome do evento", "data": "data do evento"
            }
    }

if __name__ == "__main__":
    app = OrbtAgenda()
    app.run()