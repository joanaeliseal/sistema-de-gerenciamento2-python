import socket
import os
import sys

MAX_MESSAGE_SIZE = 1024
SERVIDOR_HOST = 'localhost'
SERVIDOR_PORTA = 8888

if len(sys.argv) == 2:
    SERVIDOR_HOST = sys.argv[1]
elif len(sys.argv) == 3:
    SERVIDOR_HOST = sys.argv[1]
    SERVIDOR_PORTA = int(sys.argv[2])

CODIGOS_SERVIDOR = {
    '200': 'Cliente registrado com sucesso!', # resposta padrão
    '201': 'Pedido criado com sucesso!', # criado
    '202': 'Item adicionado ao pedido!', # aceito
    '203': 'Item indisponível.', # não autorizado
    '204': 'Cardápio esgotado!', # nenhum conteudo
    '205': 'Faça uma nova solicitação.', # resetar conteudo ###
    '206': 'Ainda há itens disponíveis.', # conteudo parcial 
    '207': 'Pedido entregue com sucesso!', # recurso entregue com sucesso
    '208': 'O pedido contém os seguintes itens.', # indica que o estado de um recurso já foi relatado em uma resposta anterior.
    '400': 'Item inválido.', # erro do cliente 
    '401': 'Item não está disponível!', # não autorizado
    '402': 'Ainda não é possível entregar o pedido.', # pagamento necessário
    '409': 'Item já está cadastrado.', # o item ja esta cadastrado no cardapio
}



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') # função para limpar tela do console

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVIDOR_HOST, SERVIDOR_PORTA))

    mensagem_servidor = client_socket.recv(MAX_MESSAGE_SIZE).decode()
    print(mensagem_servidor)

    def enviar_mensagem(mensagem):
        client_socket.send(mensagem.encode())
        return client_socket.recv(MAX_MESSAGE_SIZE).decode()

    resposta = enviar_mensagem(f"REGISTRAR {input_celular()}")
    print(CODIGOS_SERVIDOR[resposta])
    resposta = enviar_mensagem("ESGOTOU")

    cardapio_esgotado(resposta)

    while True:
        choice = mostrar_menu()

        if choice == '1':
            limpar_tela()
            if not cardapio_esgotado(enviar_mensagem("ESGOTOU")):
                adicionar_item_pedido(enviar_mensagem)

        elif choice == '2':
            limpar_tela()
            if not cardapio_esgotado(enviar_mensagem("ESGOTOU")):
                _, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
                print(f'Itens disponíveis: {resposta}')

        elif choice == '3':
            limpar_tela()
            codigo, resposta = enviar_mensagem(f"ITENS_PEDIDO").split("-", 1)
            print(CODIGOS_SERVIDOR[codigo])
            print(resposta)

        elif choice == '4':
            limpar_tela()
            resposta = enviar_mensagem(f"ENTREGAR_PEDIDO")
            if resposta == "207":
                print(CODIGOS_SERVIDOR['207'])
            else:
                _, entrega = resposta.split("-", 1)
                print(f'\nEntrega realizada!\n\nItens entregues: {entrega}\n')

        elif choice == '5':
            resposta = enviar_mensagem("SAIR")
            if resposta == "204":
                break

        else:
            limpar_tela()
            print("Opção inválida! Tente novamente.")

        enviar_mensagem(f"ESGOTOU")

    client_socket.close()

def adicionar_item_pedido(enviar_mensagem):
    codigo, resposta = enviar_mensagem("DISPONIVEIS").split("-", 1)
    if codigo == "206":
        print("Itens disponíveis: " + resposta)
    item = input_pedido()
    if item != '':
        codigo = enviar_mensagem(f"ADICIONAR_ITEM {item}")
        print(CODIGOS_SERVIDOR[codigo])
        if codigo == "401":
            cardapio_esgotado(enviar_mensagem(f"ESGOTOU"))
    else:
        print('Item inválido')

def input_pedido():
    while True:
        pedido = input("Digite o prato desejado: ").lower()
        if pedido.isalpha():
            limpar_tela()
            return pedido
        else:
            print("Entrada inválida. Digite apenas letras.")

def input_celular():
    celular = input("Digite seu celular: ")
    while not valida_celular(celular):
        limpar_tela()
        print("celular inválido! Tente novamente.")
        celular = input("Digite seu celular: ")
    return celular

def valida_celular(_celular):
    if len(_celular) == 9 and _celular.isdigit():
        return True
    else:
        return False

def cardapio_esgotado(resposta):
    if resposta == "205":
        print("Cardápio esgotado, o pedido não pode ser entregue")
        return True
    else:
        return False

def mostrar_menu():
    print('''
    1 - Ver cardápio
    2 - Realizar pedido
    3 - Cadastrar item no cardápio
    4 - Sair
    ''')
    choice = input("Digite a opção desejada: ")
    return choice

if __name__ == '__main__':
    main()