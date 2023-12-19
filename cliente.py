#!/usr/bin/env python3

import socket
import os
import sys

MAX_MESSAGE_SIZE = 1024
HOST = 'localhost'
PORT = 8888

if len(sys.argv) == 2:
    HOST = sys.argv[1]
elif len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

CODIGOS_SERVIDOR = {
    '200': 'Pedido registrado com sucesso!',
    '201': 'Pedido encontrado com sucesso!',
    '202': 'Item adicionado ao pedido!',
    '203': 'Itens disponíveis listados.',
    '204': 'Pedido finalizado com sucesso!',
    '205': 'Cardápio esgotado.',
    '206': 'Ainda há itens disponíveis.',
    '207': 'Pedido entregue com sucesso!',
    '208': 'Itens no pedido até agora.',
    '400': 'Item inválido.',
    '401': 'Item não está disponível!',
    '402': 'Ainda não é possível entregar o pedido.'
}


def cls():
    os.system('cls' if os.name == 'nt' else 'clear') # função para limpar tela do console


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    mensagem_servidor = client_socket.recv(MAX_MESSAGE_SIZE).decode()
    print(mensagem_servidor)

    def enviar_mensagem(mensagem):
        client_socket.send(mensagem.encode())
        return client_socket.recv(MAX_MESSAGE_SIZE).decode()

    resposta = enviar_mensagem(f"REGISTRAR {input_cliente()}")
    print(CODIGOS_SERVIDOR[resposta])
    resposta = enviar_mensagem("ESGOTOU")

    verifica_se_esgotou(resposta)

    while True:
        choice = mostrar_menu()

        if choice == '1':
            cls()
            if not verifica_se_esgotou(enviar_mensagem("ESGOTOU")):
                adicionar_item_pedido(enviar_mensagem)

        elif choice == '2':
            cls()
            if not verifica_se_esgotou(enviar_mensagem("ESGOTOU")):
                _, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
                print(f'Itens disponíveis: {resposta}')

        elif choice == '3':
            cls()
            codigo, resposta = enviar_mensagem(f"ITENS_PEDIDO").split("-", 1)
            print(CODIGOS_SERVIDOR[codigo])
            print(resposta)

        elif choice == '4':
            cls()
            resposta = enviar_mensagem(f"ENTREGAR_PEDIDO")
            if resposta == "402":
                print(CODIGOS_SERVIDOR['402'])
            else:
                _, entrega = resposta.split("-", 1)
                print(f'\nEntrega realizada!\n\nItens entregues: {entrega}\n')

        elif choice == '5':
            resposta = enviar_mensagem("SAIR")
            if resposta == "204":
                break

        else:
            cls()
            print("Opção inválida! Tente novamente.")

        enviar_mensagem(f"ESGOTOU")

    client_socket.close()


def adicionar_item_pedido(enviar_mensagem):
    codigo, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
    if codigo == "203":
        print("Itens disponíveis: " + resposta)
    item = input_item()
    if item != '':
        codigo = enviar_mensagem(f"ADICIONAR_ITEM {item}")
        print(CODIGOS_SERVIDOR[codigo])
        if codigo == "202":
            verifica_se_esgotou(enviar_mensagem(f"ESGOTOU"))
    else:
        print('Item inválido')


def input_item():
    while True:
        item = input("Digite o item desejado: ")
        if item.isalpha():
            cls()
            return item
        else:
            print("Entrada inválida. Digite apenas letras.")


def input_cliente():
    cliente = input("Digite o nome do cliente: ")
    return cliente


def verifica_se_esgotou(resposta):
    if resposta == "205":
        print("Cardápio esgotado, o pedido não pode ser entregue")
        return True
    else:
        return False


def mostrar_menu():
    print('''
    1 - Adicionar item ao pedido
    2 - Ver itens disponíveis
    3 - Ver itens no pedido
    4 - Entregar pedido
    5 - Sair  
    ''')
    choice = input("Digite a opção desejada: ")
    return choice


if __name__ == '__main__':
    main()
