import sys
import logging
from servidor import Server
from estruturas.hash_table import TabelaHash
from estruturas.lista_simples_encadeada import ListaEncadeada

# Constantes de configuração
MESSAGE_SIZE = 2048
HOST = '0.0.0.0'
PORT = 8888

# Gerenciador inicializado
gerenciador = None  # Pode ser configurado como TabelaHash, ListaEncadeada ou outra estrutura

def configurar_gerenciador():
    """Inicializa o gerenciador de dados (TabelaHash ou ListaEncadeada)."""
    global gerenciador
    try:
        # Aqui você pode escolher entre TabelaHash ou ListaEncadeada.
        gerenciador = TabelaHash(10)  # Inicializa a tabela hash com tamanho 10
        # gerenciador = ListaEncadeada()  # Alternativa para lista encadeada
        logging.info("Gerenciador de dados configurado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao configurar o gerenciador de dados: {e}")
        sys.exit(1)

def configurar_servidor():
    """Lê os argumentos do terminal e configura o HOST e PORT."""
    global HOST, PORT
    if len(sys.argv) >= 2:
        try:
            HOST = sys.argv[1]
            if len(sys.argv) == 3:
                PORT = int(sys.argv[2])
                if not (1 <= PORT <= 65535):
                    raise ValueError("Porta fora do intervalo permitido (1-65535).")
        except ValueError as e:
            print(f"Erro nos argumentos: {e}")
            sys.exit(1)

def iniciar_servidor():
    """Inicializa e executa o servidor."""
    try:
        logging.info(f"Iniciando servidor em {HOST}:{PORT}")
        server = Server(HOST, PORT, MESSAGE_SIZE, gerenciador)
        server.start()
    except OSError as e:
        logging.error(f"Erro ao iniciar o servidor: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Configura o log para exibir mensagens no terminal
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Configura o gerenciador de dados
    configurar_gerenciador()

    # Configura o servidor (HOST e PORT)
    configurar_servidor()

    # Inicia o servidor
    iniciar_servidor()
