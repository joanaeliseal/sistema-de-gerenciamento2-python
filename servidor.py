#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'     # Endereco IP do Servidor
PORT = 8000          # Porta que o Servidor escuta

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv = (HOST, PORT)
sock.bind(serv)
while True:
	try:
		msg, cliente = sock.recvfrom(1024)
	except: break
	print(cliente, 'mensagem:', msg.decode())
	sock.sendto(msg, cliente)
sock.close()
	
if __name__ == "__main__":
    servidor_thread = threading.Thread(target=servidor)
    servidor_thread.start()

    cliente()
