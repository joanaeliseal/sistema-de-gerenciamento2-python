import socket
import threading

# Configurações do servidor
HOST = '192.168.15.12'   # Endereço IP da sua máquina
PORT = 12345               # Número da porta

# Configurações do cliente
CLIENT_HOST = '192.168.15.184'  # Endereço IP do computador do seu cliente
CLIENT_PORT = 54321                # Número da porta do cliente

def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print("Aguardando por mensagens...")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"Recebido de {addr}: {data.decode('utf-8')}")

def cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            mensagem = input("Digite uma mensagem: ")
            s.sendto(mensagem.encode('utf-8'), (CLIENT_HOST, CLIENT_PORT))

if __name__ == "__main__":
    servidor_thread = threading.Thread(target=servidor)
    servidor_thread.start()

    cliente()
