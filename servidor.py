import socket
import threading
from estruturas.hash_table import *
from estruturas.lista_simples_encadeada import ListaEncadeada
from estruturas.boasvindas import exibir_boas_vindas

#Estruturação do restaurante
class Prato:
    def __init__(self, nome, descricao): 
        self.__nome = nome.strip()
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
            self.__nome = novo_nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao_atualizada):
            self.__descricao = descricao_atualizada


    def __str__(self):
        return f'Prato: {self.__nome}. Descrição: {self.__descricao}.'

#Inicializando o cardapio como uma hash table
cardapio = TabelaHash(30)

# Criando todos os pratos do restaurante como objetos da classe Prato
pratos = [
    Prato("Spaghetti Carbonara", "Massa com molho à base de ovos, queijo parmesão e bacon"),
    Prato("Pizza Margherita", "Pizza com molho de tomate, queijo mozzarella e manjericão fresco"),
    Prato("Risoto De Funghi", "Arroz arbóreo cozido com cogumelos funghi, creme de leite e queijo parmesão"),
    Prato("Lasanha A Bolonhesa", "Camadas de massa intercaladas com molho de carne à bolonhesa e queijo"),
    Prato("Tiramisu", "Sobremesa italiana à base de café, queijo mascarpone e cacau"),
    Prato("Bruschetta", "Fatias de pão italiano grelhado com tomate, azeite de oliva, alho e manjericão"),
    Prato("Cannoli", "Massa crocante recheada com creme de ricota e frutas cristalizadas"),
    Prato("Ravioli De Ricota E Espinafre", "Massa recheada com ricota e espinafre, servida com molho de tomate fresco"),
    Prato("Gelato", "Sorvete italiano em diversos sabores"),
    Prato("Negroni", "Coquetel italiano feito com gin, vermute e Campari"),
    Prato("Limoncello", "Licor italiano de limão")
]

# Adicionando os pratos ao cardápio
for prato in pratos:
    cardapio.put(prato.nome, prato.descricao)

 
class Restaurante:
    def __init__(self, cardapio):
        self.__cardapio = cardapio  #Atribui o cardapio do restaurante a hash table que é inicializada como cardapio

    def exibir_menu(self):
        for chave, descricao_recuperada in self.__cardapio.items():
            yield f"Prato: {chave}. Descrição: {descricao_recuperada}"
    
    def registro_pedido(self, nome_produto):
        pedido = self.__cardapio.get(nome_produto)
        if pedido == -1:
            return "401"  # Produto não encontrado 
        else:
            return "202"  # Pedido realizado com sucesso






#Estruturação do servidor

class Server:
    def __init__(self, host, port, message_size, restaurante: Restaurante):
        self.__host = host
        self.__port = port
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__restaurante =  Restaurante(cardapio)
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
                self.realizar_pedido(client_socket, celular_registrado, msg_client)

            elif msg_client == "OPCOES":
                self.exibir_cardapio(client_socket)

            elif msg_client.startswith("PEDIDOS"):
                self.ver_pedidos_anteriores(client_socket, celular_registrado)

            # Desconecta o cliente
            elif msg_client == "SAIR":
                self.desconectar_cliente(client_socket)
                break

        client_socket.close()
        print(self.__clientes.representacao_nos())

    def registrar_cliente(self, client_socket, msg_client):
        with self.__lock_clientes:
            _, celular = msg_client.split()
            cliente = self.__clientes.buscar(celular)
            if cliente is None:
                self.__clientes.inserir(celular, 'Cadastro do cliente')
                resposta = "200"
                client_socket.send(resposta.encode())
                return celular
            else:
                resposta = "201"
                client_socket.send(resposta.encode())
                return celular
            
    def exibir_cardapio(self, client_socket):
        with self.__lock_pedidos:
            mensagem = '\n'.join(self.__restaurante.exibir_menu())
            client_socket.send(f"207-{mensagem}".encode())
           

    def ver_pedidos_anteriores(self, client_socket, celular_registrado):
        with self.__lock_pedidos:
            num = celular_registrado
            resposta = self.__clientes.representacao_no(num)
            client_socket.send(resposta.encode())

    def realizar_pedido(self, client_socket, celular_registrado, msg_client):
        with self.__lock_pedidos:
            num = celular_registrado
            _, pedido_rest = msg_client.split("-", 1)
            mensg = self.__restaurante.registro_pedido(pedido_rest)
            if mensg == "401":
                client_socket.send(mensg.encode())
            if mensg == "202":
                self.__clientes.inserir(num, pedido_rest)
                client_socket.send(mensg.encode())
    
 
    def desconectar_cliente(self, client_socket):
        print("Cliente", client_socket.getpeername(), "desconectou!")
        enviar = "204"
        client_socket.send(enviar.encode())
