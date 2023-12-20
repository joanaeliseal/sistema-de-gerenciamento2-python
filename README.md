<h1 align="center">Sistema de Gerenciamento de Pedidos em Python :spaghetti:</h1>


`Descrição` - Este é um sistema simples de gerenciamento de pedidos desenvolvido em Python. O objetivo principal é fornecer uma aplicação fácil de usar para gerenciar pedidos em um ambiente de negócios.

## Funcionalidades
1. Cardápio do restaurante: possui detalhes com nome, descrição e preço.
2. Realização de Pedidos: Crie novos pedidos, associando clientes e pratos.
3. Consulta de Pedidos: Visualize pedidos em processamento, realizados ou sem estoque e obtenha informações detalhadas sobre cada transação.

## Requisitos
+ [Python 3](https://docs.python.org/3/index.html)
+ [VS Code](https://code.visualstudio.com/download)

## Como usar
1. Instale `Python 3` na sua máquina (caso não tenha).
2. Baixe ou clone o projeto para o seu computador através do comando: git clone https://github.com/joanaeliseal/sistema-de-gerenciamento-python.git
3. Abra o terminal ou prompt de comando e navegue até o diretório do projeto com o comando: cd sistema-de-gerenciamento-pedidos
4. Inicie o programa executando o arquivo `main.py`.
5. Siga as instruções no console para interagir com o sistema.
   
## Projeto Interdisciplinar 
> Esse projeto foi requisitado pelas disciplinas de Estrutura de Dados, Protocolos de Interconexão de Redes de Computadores e Sistemas Operacionais do IFPB (2023.2), ministrada pelos Profº Alex Sandro, Prof° Leonidas Lima e Profº Gustavo Wagner, com o objetivo de implementar os conhecimentos adquiridos nas três disciplinas. Veja o arquivo [Especificações do projeto](https://docs.google.com/document/d/1z6RtA2er4ap2CmnEZaI3qCE_yKTS8TWkFFeoYK7zhYg/edit?pli=1) para conferir os detalhes.

## Arquivos:
| Nome | Descrição |
| ------ | ----------- |
| restaurante.py | Implementa um sistema simples de gerenciamento de pedidos de um restaurante italiano. Contém as classes: Prato, Menu e Restaurante |
| ListaSimplesmenteEncadeada.py | Implementa a estrutura de dados linear que armazena seus elementos em uma sequência. Cada elemento da lista é armazenado em um nó |
| hash_table.py | Implementa a tabela de dispersão, que é um tipo de estrutura de dados que armazena pares chave/valor, onde a chave é usada para acessar o valor associado |
| servidor.py | Servidor TCP que gerencia pedidos de um restaurante. O servidor aceita conexões de clientes, registra clientes novos, cadastra itens no cardápio e realiza pedidos |
| cliente.py | O programa se conecta a um servidor, registra o cliente e, em seguida, permite que o cliente adicione itens ao pedido, verifique os itens disponíveis, veja os itens no pedido e entregue o pedido |
| pratos.txt | Lista de pratos italianos, com seus respectivos nomes, descrições e preços. Cada prato é representado por uma tupla de três elementos: Nome, Descrição e Preço |
| LICENCE | A MIT License concede permissão livre de custos a qualquer pessoa para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender o software |



### 📝 Autores

- [Felipe Brito](https://github.com/FelipeBritoLC)
- [Joana Elise](https://github.com/joanaeliseal)
- [Maira Larissa](https://github.com/Maira-larissa)
