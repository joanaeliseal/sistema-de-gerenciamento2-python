"""
Este arquivo contém a estrutura de dados do tipo "fila", que vai gerenciar a quantidade de pedidos do restaurante.
"""
from FilaSequencialCircularNumPy import *

if __name__ == "__main__":
    restaurante = Restaurante()

    # Fazendo alguns pedidos
    restaurante.fazer_pedido("Ravioli")
    restaurante.fazer_pedido("Pizza")
    restaurante.fazer_pedido("Tiramisú")

    # Processando os pedidos
    restaurante.processar_pedidos()
    restaurante.atualizar_status_pedido()
    restaurante.desenfileirar()