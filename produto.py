import os
import colorama 

def menu():
    print()
    print("====== MENU ======")
    print("1- cadastar produtos \n2-listar produtos \n0-Encerrar programa \n")

    escolha= int(input("O que você deseja fazer?  "))
    return escolha 

def cadastrar(arquivo):
    print()
    print("====== CADASTRO DE PRODUTOS ====== \n ")

    nome_produto= input("Nome do produto: ")
    preco= float(input("preço do produto: "))
    quantidade= int(input("quantidade de produtos:"))


    with open (arquivo, "a", encoding="utf-8") as dado:
        dado.write(
            f"{nome_produto}, {preco}, {quantidade} \n"
        )


def listar_produtos(arquivo):
    print()
    print("====== PRODUTOS CADASTRADOS ====== \n")

    with open(arquivo, "r", encoding="utf-8") as dados:
        for linha in dados:
            lista=linha.split(", ")

            print(f"Produto: {lista[0]} ")
            print(f"Preço: {lista[1]}")
            print(f"Quantidade: {lista[2]} ")


arquivo= r"C:\Users\manur\OneDrive\Documentos\EM 1DS\PA\trabalho em grupo\Desenvolvimento-colaborativo-com-git-e-github\produtos.txt"

while True:
    escolha= menu()

    if escolha == 1:
        cadastrar(arquivo)

    if escolha == 2:
        listar_produtos(arquivo)

    if escolha == 0:
        break