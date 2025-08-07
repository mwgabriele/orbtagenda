from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import (Static, Label, Input, Button, Header, Footer,
                            TextArea, ListView, ListItem, Log, DirectoryTree,
                            Pretty, Rule, DataTable, Welcome)
from textual.binding import Binding
from textual.message import Message

class TelaInicial(Screen):
    BINDINGS = [
        Binding(key="escape", action="app.switch_screen('tela_inicial')", description="Voltar")
    ]

    CSS_PATH =  "style.tcss"
    TITLE = "Orbita Agenda"
    SUB_TITLE = "versão 0.0.2"

    def compose(self):
        yield Header()
        yield Footer()
        yield Label("Nome do evento: ")
        yield Input(id="tx_nome")
        yield Label("Email de cadastro: ")
        yield Input(id="tx_email")
        yield Label("Data do evento: ")
        yield Input(id="tx_data")
        yield Button("Limpar", id="bt_limpar")
        yield Button("Cadastrar", id="bt_cadastrar")
        yield Button("Lista", id="bt_lista")

        
    def LimparFormulario(self) -> None:
        for um_input in self.query('Input'):
                um_input.value = ''

    def on_button_pressed(self, evento: Button.Pressed):

        if evento.button.id == 'bt_lista':
            self.push_screen(TelaListagem())

        if evento.button.id == 'bt_limpar':

            for um_input in self.query('Input'):
                um_input.value = ''

        if evento.button.id == 'bt_cadastrar':

            nome = self.query_one('#tx_nome', Input).value
            email = self.query_one('#tx_email', Input).value
            data = self.query_one('#tx_data', Input).value

            OrbtAgenda.AGENDA[email] = {"nome": nome, "data": data}

            self.notify(f"{nome} em {data} cadastrado!")
            self.LimparFormulario()
            self.query_one("#tx_nome", Input).focus()

            #if evento.button.id == 'bt_cadastrar' and 

class TelaListagem(TelaInicial):
    