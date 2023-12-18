import numpy as np

class FilaException(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da fila é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)
      
class Fila:
    """A classe Fila.py implementa a estrutura de dados "Fila".
       A classe permite que qualquer tipo de dado seja armazenada na fila.

     Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da
             fila
    """
    def __init__(self, tamanho = 10):
        """ Construtor padrão da classe Fila sem argumentos. Ao instanciar
            um objeto do tipo Fila, esta iniciará vazia. 
        """
        self.__max = tamanho
        self.__dado = np.full(self.__max, None)
        self.__frente = 0
        self.__final = -1
        self.__tam = 0
 
    def estaVazia(self):
        """ Método que verifica se a fila está vazia ou não

        Returns:
            boolean: True se a fila estiver vazia, False caso contrário

        Examples:
            f = Fila()
            ...   # considere que temos internamente na fila frente->[10,20,30,40]
            if(f.estaVazia()): #
               # instrucoes
        """
        return True if self.__tam==0 else False

    def estaCheia(self):
        """ Método que verifica se a fila está vazia ou não

        Returns:
            boolean: True se a fila estiver vazia, False caso contrário

        Examples:
            f = Fila()
            ...   # considere que temos internamente na fila frente->[10,20,30,40]
            if(f.estaVazia()): #
               # instrucoes
        """
        return True if self.__tam == self.__max else False

    def __len__(self):
        """ Método que consulta a quantidade de elementos existentes na fila

        Returns:
            int: um número inteiro que determina o número de elementos existentes na fila

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (f.tamanho()) # exibe 4
        """        
        return self.__tam


    def elementoDaFrente(self):
        """ Método que recupera o conteudo armazenado no elemento da frente da fila,
            sem removê-lo.

        Returns:
            object: o conteudo armazenado na frente da fila (tipo primitivo ou objeto).

        Raises:
            FilaException: Exceção lançada quando a fila não possui elementos
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila frente->[10,20,30,40]
            print (f.elementoDaFrente()) # exibe 10
        """
        if self.estaVazia():
            raise FilaException(f'Fila Vazia. Não há elemento a recuperar.')

        carga = self.__dado[self.__frente]
        return carga

    
    def busca(self, valor:any):
        """ Método que recupera a posicao ordenada, dentro da fila, em que se
            encontra um valor passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada

        Args:
            valor: um item de dado que deseja procurar na fila
        
        Returns:
            int: um número inteiro representando a posição, na fila, em que foi
                 encontrado "valor".

        Raises:
            FilaException: Exceção lançada quando o argumento "valor"
                  não está presente na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente->[10,20,30,40]
            print (f.elemento(40)) # exibe 4
        """
        frente = self.__frente
        for i in range(1,self.__tam+1):
            if self.__dado[frente] == valor:
                return i
            frente = (frente + 1)% self.__max
                
        raise FilaException(f'O valor {valor} não está armazenado na fila')

    def elemento(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= self.__tam
            frente = self.__frente
            for i in range(posicao-1):
                frente = (frente + 1) % self.__max

            return self.__dado[frente]
        except AssertionError:
            raise FilaException(f'Posicao inválida para a fila atual com {self.__tam} elementos')

    def enfileirar(self, valor ):
        """ Método que adiciona um novo elemento na frente da fila

        Args:
            valor(qualquer tipo de dado): o conteúdo que deseja armazenar
                  na fila.

        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            f.enfileirar(50)
            print(f)  # exibe [10,20,30,40,50]
        """
        if self.estaCheia():
            raise FilaException(f'Fila cheia. Não é possível inserir elementos')

        self.__tam +=1
        self.__final = (self.__final + 1) % self.__max
        self.__dado[ self.__final ] = valor
        


    def desenfileirar(self):
        """ Método que remove um elemento do final da fila e devolve o conteudo
            existente removido.
    
        Returns:
            qualquer tipo de dado: o conteúdo referente ao elemento removido

        Raises:
            FilaException: Exceção lançada quando se tenta remover algo de uma fila vazia
                    
        Examples:
            f = Fila()
            ...   # considere que temos internamente a fila  frente-> [10,20,30,40]
            dado = f.desenfileirar()
            print(f) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        if self.estaVazia():
            raise FilaException(f'Fila Vazia. Não há elemento a remover.')

        carga = self.elementoDaFrente()
        self.__tam -= 1
        self.__frente = (self.__frente + 1)% self.__max

        return carga
    
    
    def printArray(self):
        print('[ ',end='')
        frente = self.__frente
        for i in range(self.__max):
            print(f'{self.__dado[frente]} ', end='')
            frente = (frente+1) % self.__max
        print(']')

        
    def __str__(self):
        str = 'Frente-> [ '

        frente = self.__frente
        for i in range(self.__tam):
            str += f'{self.__dado[frente]} '
            frente = (frente + 1) % self.__max
        str += ']'
        return str
       

class Restaurante:
    """
    Classe que vai fazer o gerenciamento da quantidade de pedidos do restaurante.
    """
    def __init__(self):
        self.fila_pedidos = Fila()

    def fazer_pedido(self, pedido):
        self.fila_pedidos.enfileirar(pedido)
        print(f"Pedido {pedido} adicionado à fila.")

    # def processar_proximo_pedido(self):
    #     if not self.fila.estaCheia():
    #         pedido = self.fila.get_nowait()
    #         print(f"Preparando pedido: {pedido}")
    #     else:
    #         print("A fila está vazia. Nenhum pedido para processar no momento.")

    def processar_pedidos(self):
        pedidos_processados = 0
        while not self.fila_pedidos.estaVazia():
            pedido = self.fila_pedidos
            print(f"Processando pedido: {pedido}")
            # Aqui você pode adicionar lógica para preparar o pedido, atualizar o status, etc.
            status_atualizado = self.atualizar_status_pedido(pedido, "Em preparo")
            if status_atualizado:
                print(f"Status do pedido {pedido} atualizado para 'Em preparo'.")
            else:
                print(f"Falha ao atualizar o status do pedido {pedido}.")

            # Adicionar mais lógica, como preparação física do pedido, etc.

            # Simulando a conclusão da preparação do pedido
            print(f"Pedido {pedido} preparado com sucesso.")
            # Atualizar o status para "Concluído"
            status_atualizado = self.atualizar_status_pedido(pedido, "Concluído")
            if status_atualizado:
                print(f"Status do pedido {pedido} atualizado para 'Concluído'.")
            else:
                print(f"Falha ao atualizar o status do pedido {pedido}.")

            pedidos_processados +=1
        # Condição de parada adicional quando atingir 10 pedidos
        if pedidos_processados == 10:
            print("Limite de 10 pedidos atingido. Aguarde a liberação dos pedidos em preparo.")

    def atualizar_status_pedido(self, pedido, novo_status):
        # Adicione lógica aqui para atualizar o status do pedido no seu sistema
        # Retorna True se a atualização for bem-sucedida, False caso contrário
        # (por exemplo, se o pedido não for encontrado na base de dados)
        return True
