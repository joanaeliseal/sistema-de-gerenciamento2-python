import socket
import threading
from restaurante import *
from estruturas.hash_table import *
from estruturas.lista_simples_encadeada import ListaEncadeada
from estruturas.boasvindas import exibir_boas_vindas

class Server:
    def __init__(self, host, port, message_size, restaurante: Restaurante):
        self.__host = host
        self.__port = port
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__restaurante = Restaurante
        self.__max_message_size = message_size
        self.__lock_clientes = threading.Lock()
        self.__lock_pedidos = threading.Lock()
        self.__clientes = ListaEncadeada()
    
    # Inicia o servidor
    def start(self):
        self.__server_socket.bind((self.__host, self.__port))
        self.__server_socket.listen(1)
        print(f"Servidor aguardando conexões em {self.__host}:{self.__port}")
        
        try:
            self.accept_connections()
        except KeyboardInterrupt:
            self.__server_socket.close() # Fecha socket do servidor quando clicar CTRL C

    # Trata as conexões dos clientes
    def accept_connections(self):
        while True:
            client_socket, address = self.__server_socket.accept()
            print("Cliente conectado:", address)

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    # Comunicação com o cliente/ respostas para o cliente
    def handle_client(self, client_socket):
        boasvindas = exibir_boas_vindas()
        client_socket.send(boasvindas.encode())
        celular_registrado = ''

        while True:
            # Tratamento para quando o cliente desconectar
            try:
                msg_client = client_socket.recv(self.__max_message_size).decode()
            except ConnectionResetError:
                print("Cliente", client_socket.getpeername(), "desconectou!")
                break

            if msg_client.startswith("REGISTRAR"):
                celular_registrado = self.registrar_cliente(client_socket, msg_client)

            if msg_client.startswith("PEDIR"):
                self.realizar_pedido(self, client_socket, celular_registrado, msg_client)

            elif msg_client == "OPCOES":
                self.exibir_cardapio(client_socket)

            elif msg_client == "CADASTRAR":
                self.cadastrar_item_cardapio(client_socket, msg_client)

            # Desconecta o cliente
            elif msg_client == "SAIR":
                self.desconectar_cliente(client_socket)
                break

        client_socket.close()

    def registrar_cliente(self, client_socket, msg_client):
        with self.__lock_clientes:
            _, celular = msg_client.split()
            cliente = self.__clientes.buscar(celular)
            if cliente is None:
                self.__clientes.inserir(celular, [])
                resposta = "200"
                client_socket.send(resposta.encode())
                return celular
            else:
                resposta = "201"
                client_socket.send(resposta.encode())
                return celular
            
    def exibir_cardapio(self, client_socket):
        with self.__lock_pedidos:
            mensagem = self.__restaurante.exibir_menu()
            client_socket.send(f"207-{mensagem}".encode())
           

    def cadastrar_item_cardapio(self, client_socket, msg_client):
        with self.__lock_pedidos:
            _, nome, descricao, preco = msg_client.split()

            if cardapio.get(nome) is not None:
                resposta = "409"  # Código para item já cadastrado
            else:
                Prato(nome, descricao, preco)
                cardapio.put(prato.nome, prato.descricao)
                resposta = "202"  # Código para item cadastrado com sucesso

            client_socket.send(resposta.encode())

    def realizar_pedido(self, client_socket, celular_registrado, msg_client):
        with self.__lock_pedidos:
            _, nome_produto = msg_client

            produto = cardapio.get(nome_produto)

            if produto is not None:
                pedidos_cliente = self.__clientes.buscar(celular_registrado)
                pedidos_cliente.append(nome_produto)
                self.__clientes.set_valor(celular_registrado, pedidos_cliente)
                resposta = "202"  # Pedido realizado com sucesso
            else:
                resposta = "401"  # Produto não encontrado ou quantidade inválida

            client_socket.send(resposta.encode())
    
    def verifica_cheia(self,  client_socket):
        with self.__lock_pedidos:
            mensagem = self.__cardapio.esta_cheio()
            client_socket.send(f"207-{mensagem}".encode())
   
    def desconectar_cliente(self, client_socket):
        print("Cliente", client_socket.getpeername(), "desconectou!")
        enviar = "204"
        client_socket.send(enviar.encode())

