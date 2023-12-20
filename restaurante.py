import random
from estruturas.hash_table import *

class Prato:
    def __init__(self, nome, descricao, preco): 
        self.__nome = nome.strip()
        self.__descricao = descricao
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
            self.__nome = novo_nome

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao_atualizada):
            self.__descricao = descricao_atualizada

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
            self.__preco = novo_preco

    def __str__(self):
        return f'Prato: {self.__nome}. Descrição: {self.__descricao}. Valor: R${self.__preco}.'

 
class Restaurante:
    def __init__(self, cardapio):
        self.__cardapio = cardapio  #Atribui o cardapio do restaurante a hash table que é inicializada como cardapio

    def exibir_menu(self):
        for prato in pratos:
            chave = prato.nome
            descricao_recuperada = cardapio.get(chave)
            print(f"Prato: {chave}. Descrição: {descricao_recuperada}")
  
    def esta_cheio(self):
         if self.__cardapio.len() == self.__cardapio.get_tamanho():
              return True
         

#Inicializando o cardapio como uma hash table
cardapio = TabelaHash(30)

#Criando todos os pratos do restaurante como objetos da classe Prato
pratos = [
    Prato("Spaghetti Carbonara", "Massa com molho à base de ovos, queijo parmesão e bacon", 15.99),
    Prato("Pizza Margherita", "Pizza com molho de tomate, queijo mozzarella e manjericão fresco", 12.99),
    Prato("Risoto de Funghi", "Arroz arbóreo cozido com cogumelos funghi, creme de leite e queijo parmesão", 18.99),
    Prato("Lasanha à Bolonhesa", "Camadas de massa intercaladas com molho de carne à bolonhesa e queijo", 20.99),
    Prato("Tiramisù", "Sobremesa italiana à base de café, queijo mascarpone e cacau", 8.99),
    Prato("Bruschetta", "Fatias de pão italiano grelhado com tomate, azeite de oliva, alho e manjericão", 9.99),
    Prato("Cannoli", "Massa crocante recheada com creme de ricota e frutas cristalizadas", 7.99),
    Prato("Ravioli de Ricota e Espinafre", "Massa recheada com ricota e espinafre, servida com molho de tomate fresco", 16.99),
    Prato("Gelato", "Sorvete italiano em diversos sabores", 6.99),
    Prato("Negroni", "Coquetel italiano feito com gin, vermute e Campari", 10.99),
    Prato("Limoncello", "Licor italiano de limão", 8.99)
]

# Adicionando os pratos ao cardápio
for prato in pratos:
    cardapio.put(prato.nome, prato.descricao)
'''# Verificando se os pratos foram adicionados corretamente 
    chave = prato.nome
    descricao_recuperada = cardapio.get(chave)
    print(f"Prato: {chave}. Descrição: {descricao_recuperada}")
'''

#Inicializando o restaurante com o cardapio criado 
Restaurante(cardapio)

