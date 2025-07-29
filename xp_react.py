from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import Input, Label, Button

class ListaProdutos(Widget):
    
    produtos = reactive({
        "prg001": {
            "nome":"Sapato",
            "preco": 240.00,
            "quatidade": 20
        }
    })

    def render(self) -> str:
        listage = str()

        for cod, dados in self.produtos.items():
            listagem += f'{cod}: {dados['nome']},  {dados['preco']},  {dados['quantidade']}\n'
            
            return listagem
        
class XP_React(App):
    def compose(self) -> ComposeResult:
        yield ListaProdutos()
        yield Label("cód:")
        yield Input(id="tx_cod")
        yield Label("nome:")
        yield Input(id="tx_nome")
        yield Label("valor")
        yield Input(id="tx_valor")
        yield Label("quantidade:")
        yield Input(id="tx_quantidade")
        yield Button("Cadastrar", id="bt_cadastrar")
        yield ListaProdutos(id="lst_produtos")

    def on_button_pressed(self, evento: Button.Pressed):
        if evento.button.id == 'bt_cadastrar':
            # pegamos a referência para o widget ListaProdutos
            lista = self.query_one("#lst_produtos", ListaProdutos)

            produtos_atualizados = lista.produtos.copy()

            codigo = self.query_one("#tx_cod", Input).value
            nome = self.query_one("#tx_nome", Input).value
            preco = self.query_one("#tx_valor", Input).value
            quant = self.query_one("#tx_quantidade", Input).value

            self.limpar_formulario()

            produtos_atualizados[codigo] = {
                "nome": "teste nome",
                "preco": 1234.56,
                "quantidade": 100
            }

            # aqui modificamos a propriedade reativa do componente
            # atribuindo a propriedade o novo dict com os produtos
            lista.produtos = produtos_atualizados

            self.query_one("#tx_cod", Input).focus()

if __name__ == '__main__':
    app = XP_React()
    app.run