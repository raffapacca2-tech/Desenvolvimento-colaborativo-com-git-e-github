from colorama import Fore, Style, init

init(autoreset=True)


class cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class menu:
    def __init__(self):
        self.Clientes = []
    def exibir_menu(self):
        print(Fore.BLUE.BRIGHT + "=== Menu de Cadastros ===")
        print("1. Cadastrar Cliente")
        print("3. Sair")
