from estruturas.hash_table import TabelaHash


class Prato:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    def __str__(self):
        return f"{self.nome} - {self.descricao}"


class Restaurante:
    def __init__(self):
        self.cardapio = TabelaHash(20)  # Tabela Hash para gerenciar o cardápio
        self.__inicializar_cardapio()

    def __inicializar_cardapio(self):
        """Inicializa o cardápio com pratos e descrições predefinidos."""
        pratos = [
            Prato("Spaghetti Carbonara", "Massa com molho à base de ovos, queijo parmesão e bacon"),
            Prato("Pizza Margherita", "Pizza com molho de tomate, queijo mozzarella e manjericão fresco"),
            Prato("Risoto De Funghi", "Arroz arbóreo cozido com cogumelos funghi, creme de leite e queijo parmesão"),
            Prato("Lasanha A Bolonhesa", "Camadas de massa intercaladas com molho de carne à bolonhesa e queijo"),
            Prato("Tiramisu", "Sobremesa italiana à base de café, queijo mascarpone e cacau"),
            Prato("Bruschetta", "Fatias de pão italiano grelhado com tomate, azeite de oliva, alho e manjericão"),
            Prato("Cannoli", "Massa crocante recheada com creme de ricota e frutas cristalizadas"),
            Prato("Ravioli De Ricota E Espinafre", "Massa recheada com ricota e espinafre, servida com molho de tomate fresco"),
            Prato("Gelato", "Sorvete italiano em diversos sabores"),
            Prato("Negroni", "Coquetel italiano feito com gin, vermute e Campari"),
            Prato("Limoncello", "Licor italiano de limão"),
        ]

        # Adiciona cada prato à tabela hash do cardápio
        for codigo, prato in enumerate(pratos, start=1):
            self.cardapio.put(codigo, prato)

    def exibir_cardapio(self):
        """Exibe o cardápio formatado."""
        itens = self.cardapio.items()
        cardapio_formatado = "\n=== CARDÁPIO ===\n"
        for chave, prato in itens:
            cardapio_formatado += f"{chave}. {prato}\n"
        return cardapio_formatado

    def obter_prato(self, codigo):
        """Obtém o prato pelo código."""
        prato = self.cardapio.get(codigo)
        return prato if prato != -1 else None