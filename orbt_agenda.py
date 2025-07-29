from textual.app import App
from textual.widgets import Label, Input, Button, Static, Pretty
from textual.screen import Screen
from textual.containers import Vertical, Horizontal

class TelaListagem(Screen):
    def compose(self):
        yield Pretty(OrbtAgenda.AGENDA)

class OrbtAgenda(App):

    AGENDA = {
        "nome@email.com": {"nome": "Nome do evento", "data": "data do evento",}
    }

    CSS = '''

    #title {
    content-align-horizontal: center;
    text-align: center;
}

    #tx_version {
    content-align-horizontal: center;
    color: gray;
}

    Label {
    content-align-horizontal: center;
    text-align: center;
}

    #container_botoes {
    content-align: center middle;
    align-horizontal: center;
}

    Button {
    border: aqua;
}

'''

    def compose(self):
        yield Static (
"""
--------------------------
Orbita Agenda
--------------------------
""", id="title")
        yield Horizontal()
        yield Static ("Versão: 0.0.1", id="tx_version")
        yield Label("Nome do evento: ")
        yield Input(id="tx_nome")
        yield Label("Email de cadastro: ")
        yield Input(id="tx_email")
        yield Label("Data do evento: ")
        yield Input(id="tx_data")
        yield Vertical(
            Button ("Limpar", id="bt_limpar"),
            Button("Cadastrar", id="bt_cadastrar"),
            Button("Lista", id="bt_lista"),
            id="container_botoes"
        )

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
            self.limpar_formulario()
            self.query_one("#tx_nome", Input).focus()

if __name__ == "__main__":
    app = OrbtAgenda()
    app.run()