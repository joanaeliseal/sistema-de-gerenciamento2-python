# Cliente - Interações e Pedidos

import socket
from estruturas.boasvindas import exibir_boas_vindas

class Cliente:
    def __init__(self, host="127.0.0.1", porta=5000):
        self.host = host
        self.porta = porta
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        """Conecta o cliente ao servidor."""
        try:
            self.socket_cliente.connect((self.host, self.porta))
            print("Conectado ao servidor com sucesso!")
        except ConnectionRefusedError:
            print("Erro: Não foi possível conectar ao servidor. Verifique se ele está ativo.")
            return False
        return True

    def enviar_mensagem(self, mensagem):
        """Envia uma mensagem ao servidor."""
        try:
            self.socket_cliente.send(mensagem.encode())
        except BrokenPipeError:
            print("Erro: Conexão com o servidor foi perdida.")
            return False
        return True

    def receber_resposta(self):
        """Recebe uma resposta do servidor."""
        try:
            resposta = self.socket_cliente.recv(1024).decode()
            return resposta
        except ConnectionResetError:
            print("Erro: Conexão com o servidor foi encerrada.")
            return None

    def fechar_conexao(self):
        """Fecha a conexão com o servidor."""
        self.socket_cliente.close()

    def iniciar(self):
        """Inicia o cliente, exibe o menu e interage com o servidor."""
        print(exibir_boas_vindas())

        if not self.conectar():
            return

        while True:
            print("\nDigite uma opção:")
            print("1 - Ver o cardápio")
            print("2 - Fazer um pedido")
            print("3 - Sair")
            
            opcao = input("Opção: ")

            if opcao == "1":
                self.enviar_mensagem("VER_CARDAPIO")
                resposta = self.receber_resposta()
                if resposta:
                    print("\n--- Cardápio ---")
                    print(resposta)
            elif opcao == "2":
                prato_codigo = input("Digite o código do prato que deseja pedir: ")
                self.enviar_mensagem(f"FAZER_PEDIDO {prato_codigo}")
                resposta = self.receber_resposta()
                if resposta:
                    print("\n" + resposta)
            elif opcao == "3":
                self.enviar_mensagem("SAIR")
                print("Encerrando conexão com o servidor. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        self.fechar_conexao()


if __name__ == "__main__":
    cliente = Cliente()
    cliente.iniciar()
