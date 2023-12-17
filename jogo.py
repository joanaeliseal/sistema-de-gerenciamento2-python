import tkinter as tk
from lista import Lista, ListaException, Node
"""
EXPLICAÇÕES:
A classe JogoDaVelha manipula a lógica do jogo com a lista encadeada, e a classe JogoDaVelhaGUI gerencia a interface gráfica
usando Tkinter.
Os cliques nos botões da interface gráfica são vinculados ao método 'on_button_click', que por sua vez chama 'movimento' da classe do jogo.
A função update_board_gui é usada para atualizar a exibição da interface gráfica com o estado atual do tabuleiro.
----------------------------

"""
class JogoDaVelha:
    def __init__(self):
        self.__board = []
        self.__jogador_atual = 'X'

    def get_elemento(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return None
        else:
            self.__jogador.atual = self.__head
            for i in range(row):
                if self.__jogador.atual is None:
                    return None
                else:
                    return self.__board[row][col]
                self.__jogador.atual = self.__jogador.atual.next
            return self.__jogador.atual.data[col]

    def movimento(self, row, col):
        # Verifica se a posição está vazia
        if self.__board.get_elemento(row, col) is None:
            # Faz a jogada na posição desejada
            self.__board.set_elemento(row, col, self.__jogador_atual)
            
            # Verifica se o jogo acabou (vencedor ou empate)
            if self.verificar_vencedor() or self.verificar_empate():
                print("Jogo terminou!")
                self.imprimir_tabuleiro()
                return True

            # Alternância entre jogadores
            self.__jogador_atual = 'O' if self.__jogador_atual == 'X' else 'X'
            return True
        else:
            print("Posição já ocupada. Escolha outra.")
            return False
        
    def verificar_vencedor(self):
        # Verificar linhas, colunas e diagonais
        for i in range(3):
            if self.__board.get_elemento(i, 0) == self.__board.get_elemento(i, 1) == self.__board.get_elemento(i, 2) != ' ':
                print(f"Jogador {self.__jogador_atual} venceu!")
                return True
            if self.__board.get_elemento(0, i) == self.__board.get_elemento(1, i) == self.__board.get_elemento(2, i) != ' ':
                print(f"Jogador {self.__jogador_atual} venceu!")
                return True

        if self.__board.get_elemento(0, 0) == self.__board.get_elemento(1, 1) == self.__board.get_elemento(2, 2) != ' ':
            print(f"Jogador {self.__jogador_atual} venceu!")
            return True
        if self.__board.get_elemento(0, 2) == self.__board.get_elemento(1, 1) == self.__board.get_elemento(2, 0) != ' ':
            print(f"Jogador {self.__jogador_atual} venceu!")
            return True

        return False

    def verificar_empate(self):
        # Verificar se todas as posições estão ocupadas
        for i in range(3):
            for j in range(3):
                if self.__board.get_elemento(i, j) == ' ':
                    return False
        print("O jogo empatou!")
        return True

    def imprimir_tabuleiro(self):
        for row in self.__board.tabuleiro:
            print('|'.join(row))

class JogoDaVelhaGUI: # GUI = interface
    def __init__(self, root, jogo):
        self.root = root
        self.jogo = jogo
        self.buttons = [[None, None, None] for _ in range(3)]
        self.criarGUI()

    def criarGUI(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", width=10, height=7,command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        # Manipule o clique do botão
        self.game.make_move(row, col)
        self.update_board_gui()

    def update_board_gui(self):
        self.__jogador.atual = self.game.board.head
        for i in range(3):
            for j in range(3):
                if self.__jogador.atual is not None:
                    self.buttons[i][j]["text"] = self.__jogador.atual.data[i][j] if self.__jogador.atual else ""
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha()
    gui = JogoDaVelhaGUI(root, game)
    root.mainloop()