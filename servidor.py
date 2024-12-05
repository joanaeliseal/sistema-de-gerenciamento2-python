import socket
import threading
from estruturas.lista_simples_encadeada import ListaEncadeada
from estruturas.boasvindas import exibir_boas_vindas
from restaurante import Restaurante


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientes_conectados = []
        self.restaurante = Restaurante()  # Instância do restaurante
        self.pedidos = ListaEncadeada()  # Lista encadeada para gerenciar os pedidos dos clientes

    def iniciar(self):
        """Inicia o servidor para aceitar conexões."""
        try:
            self.socket_servidor.bind((self.host, self.port))
            self.socket_servidor.listen(5)
            print(exibir_boas_vindas())  # Exibe mensagem de boas-vindas no servidor
            print(f"Servidor iniciado em {self.host}:{self.port} e aguardando conexões...")

            while True:
                cliente_socket, endereco = self.socket_servidor.accept()
                self.clientes_conectados.append(cliente_socket)
                print(f"Novo cliente conectado: {endereco}")

                # Inicia uma thread para atender o cliente
                thread_cliente = threading.Thread(target=self.gerenciar_cliente, args=(cliente_socket,))
                thread_cliente.start()

        except Exception as e:
            print(f"Erro ao iniciar o servidor: {e}")
        finally:
            self.socket_servidor.close()

    def gerenciar_cliente(self, cliente_socket):
        """Gerencia a comunicação com um cliente conectado."""
        try:
            while True:
                mensagem = cliente_socket.recv(1024).decode()
                if not mensagem:
                    break

                print(f"Mensagem recebida do cliente: {mensagem}")
                resposta = self.processar_mensagem(mensagem, cliente_socket)
                cliente_socket.send(resposta.encode())

        except Exception as e:
            print(f"Erro ao gerenciar cliente: {e}")
        finally:
            cliente_socket.close()

    def processar_mensagem(self, mensagem, cliente_socket):
        """Processa a mensagem enviada pelo cliente e retorna uma resposta."""
        if mensagem == "207":
            # Retorna o cardápio
            return self.restaurante.exibir_cardapio()

        elif mensagem.startswith("209-"):
            # Realiza um pedido
            _, numero_prato = mensagem.split("-")
            numero_prato = int(numero_prato)
            prato = self.restaurante.obter_prato(numero_prato)

            if prato != -1:
                endereco_cliente = cliente_socket.getpeername()
                self.pedidos.inserir(endereco_cliente, prato)
                return "202"  # Pedido realizado com sucesso
            else:
                return "401"  # Prato não encontrado

        elif mensagem == "211":
            # Retorna os pedidos anteriores do cliente
            endereco_cliente = cliente_socket.getpeername()
            pedidos_cliente = self.pedidos.representacao_no(endereco_cliente)

            if pedidos_cliente:
                return f"\n=== SEUS PEDIDOS ===\n{pedidos_cliente}"
            else:
                return "Nenhum pedido encontrado."

        elif mensagem == "0":
            # Encerra a conexão
            return "Desconectando do servidor..."

        else:
            # Mensagem não reconhecida
            return "Comando inválido. Tente novamente."


# Configuração inicial do servidor
if __name__ == "__main__":
    HOST = "127.0.0.1"  # Endereço IP do servidor (localhost)
    PORT = 5000         # Porta do servidor

    servidor = Servidor(HOST, PORT)
    servidor.iniciar()
