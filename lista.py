import tkinter as tk

"""
EXPLICAÇÕES:
A classe JogoDaVelha manipula a lógica do jogo com a lista encadeada, e a classe JogoDaVelhaGUI gerencia a interface gráfica
usando Tkinter.
Os cliques nos botões da interface gráfica são vinculados ao método 'on_button_click', que por sua vez chama 'movimento' da classe do jogo.
A função update_board_gui é usada para atualizar a exibição da interface gráfica com o estado atual do tabuleiro.
----------------------------

"""

class ListaException(Exception):
    """Classe de exceção lançada quando uma violação de ordem genérica
       da lista é identificada.
    """

    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)

class Node:
    '''
    Classe de objetos para um nó dinâmico na memória
    '''
    def __init__(self,data):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, newNext):
        self.__next = newNext

    def hasNext(self):
        return self.__next != None
    
    def __str__(self):
        return str(self.__data)
    

class Lista:
    '''
    Esta classe implementa uma estrutura Lista Simplesmente Encadeada
    '''
    # constructor initializes an empty linkd list
    def __init__(self):
        self.__head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.__next = self.__head

class JogoDaVelha:
    def __init__(self):
        self.__board = Lista()
        self.__jogador.atual = 'X'

    def movimento(self, row, col):
        # adicionar a lógica para fazer uma jogada no tabuleiro
        # Certificar de fazer a alternância entre os jogadores (X e O)
        pass

class JogoDaVelhaGUI: # GUI = interface
    def __init__(self, root, jogo):
        self.__root = root
        self.__jogo = jogo
        self.__buttons = [[None, None, None] for _ in range(3)]
        self.__criarGUI()

    def create_gui(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", width=5, height=2,command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        # Manipule o clique do botão
        self.game.make_move(row, col)
        self.update_board_gui()

    def update_board_gui(self):
        current_node = self.game.board.head
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = current_node.data[i][j] if current_node else ""
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha()
    gui = JogoDaVelhaGUI(root, game)
    root.mainloop()


