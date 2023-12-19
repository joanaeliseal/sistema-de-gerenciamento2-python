import random

from hash_table import TabelaHash


class Restaurante:
    """
    ---------------------------------------
    Métodos da classe: 

    """
    def __init__(self, tamanho):
        
        self.__tabela_cardapio = TabelaHash(tamanho)  # Cria uma instância da classe TabelaHash com o tamanho fornecido
        self.__pedidos = {} 
        self.__pedido_realizado = None  
        self.__cpf_cliente = None  

    def ver_cardapio(self, numero, cpf):
        self.__pedidos[numero] = cpf  
        return self.__tabela_cardapio.put(numero, cpf)  

    # def numeros_nao_comprados(self):
    #     # Método para obter a lista de números não comprados
    #     return [i for i, valor in enumerate(self.__tabela_rifa.get_tabela()) if not valor]
    #     # Retorna uma lista de índices em que o valor correspondente na tabela de hash é False (não comprado)

    def status_pedido(self):
        if self.__pedido_realizado is None: # Verifica se não foi realizado nenhum pedido
            cpf, pedido_realizado = self.realizar_pedido() # Gera um pedido ALEATÓRIO: CONSERTAR ISSO
            self.__pedido_realizado = pedido_realizado
            self.__cpf_cliente = cpf
            return f'{str(pedido_realizado).zfill(2)}-{cpf}'
        else:
            return f'{str(self.__pedido_realizado).zfill(2)}-{self.__cpf_cliente}'

        # """Retorna uma string formatada contendo o número do pedido
        #   e o CPF do cliente, onde o número do pedido é formatado 
        #   para ter pelo menos dois dígitos 
        #   (preenchidos com zeros à esquerda se necessário)."""

    def realizar_pedido(self):
        
        pedido_realizado = random.randint(0, self.__tabela_cardapio.get_tamanho()-1)  
        cpf = self.__tabela_cardapio.get(pedido_realizado) 
        return [cpf, pedido_realizado]  

    def esgotou(self):
        
        return len(self.__pedidos) == self.__tabela_cardapio.get_tamanho()

    def get_tamanho(self):
        # Retorna o tamanho da tabela de hash
        return self.__tabela_cardapio.get_tamanho()
