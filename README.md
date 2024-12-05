<h1 align="center">Sistema de Gerenciamento de Pedidos em Python :spaghetti:</h1>

`Descrição` - Este é um sistema simples de gerenciamento de pedidos desenvolvido em Python. O objetivo principal é fornecer uma aplicação fácil de usar para gerenciar pedidos em um restaurante, utilizando estruturas de dados como Tabela Hash e Lista Simples Encadeada.

## Funcionalidades
1. **Cardápio do restaurante**: Exibe pratos com nome, descrição e outros detalhes.
2. **Realização de Pedidos**: Permite criar novos pedidos, associando clientes e pratos.
3. **Consulta de Pedidos**: Visualiza os pedidos realizados e suas informações.
4. **Estrutura de Dados**: Utiliza uma tabela hash e lista encadeada para armazenar dados de maneira eficiente.

## Requisitos
+ [Python 3](https://docs.python.org/3/index.html)
+ [VS Code](https://code.visualstudio.com/download)

## Como usar
1. Instale `Python 3` na sua máquina (caso não tenha).
2. Baixe ou clone o projeto para o seu computador através do comando:
   ```
   git clone https://github.com/joanaeliseal/sistema-de-gerenciamento-python.git
   ```
3. Abra o terminal ou prompt de comando e navegue até o diretório do projeto com o comando:
   ```
   cd sistema-de-gerenciamento-pedidos
   ```
4. Instale as dependências do projeto (se houver) com:
```
pip install -r requirements.txt
```
5. Inicie o programa executando o arquivo `main.py`:
```
python main.py
```
6. Siga as instruções no console para interagir com o sistema.

## Projeto Interdisciplinar 
> Esse projeto foi requisitado pelas disciplinas de Estrutura de Dados, Protocolos de Interconexão de Redes de Computadores e Sistemas Operacionais do IFPB (2023.2), ministrada pelos Profº Alex Sandro, Prof° Leonidas Lima e Profº Gustavo Wagner, com o objetivo de implementar os conhecimentos adquiridos nas três disciplinas. Veja o arquivo [Especificações do projeto](https://docs.google.com/document/d/1z6RtA2er4ap2CmnEZaI3qCE_yKTS8TWkFFeoYK7zhYg/edit?pli=1) para conferir os detalhes.

## Arquivos:
| Nome | Descrição |
| ------ | ----------- |
| `boasvindas.py` | Imprime na tela uma mensagem de boas-vindas ao restaurante. |
| `lista_simples_encadeada.py` | Implementa a estrutura de dados linear que armazena seus elementos em uma sequência. Cada elemento da lista é armazenado em um nó. |
| `hash_table.py` | Implementa a tabela de dispersão (hash table), que é uma estrutura de dados para armazenar pares chave/valor. |
| `restaurante.py` | Contém as classes `Prato`, `Menu` e `Restaurante`. Organiza o cardápio e os pratos do restaurante. |
| `main.py` | Inicializa o cliente e o servidor do programa. Inicia o servidor e gerencia a configuração do ambiente. |
| `servidor.py` | Servidor TCP que gerencia pedidos do restaurante. Aceita conexões de clientes, registra novos pedidos e itens no cardápio. |
| `cliente.py` | Programa cliente que se conecta ao servidor, registra o cliente e interage com o sistema de pedidos. |
| `LICENCE` | A MIT License concede permissão livre de custos a qualquer pessoa para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender o software. |

### 📝 Autores

- [Felipe Brito](https://github.com/FelipeBritoLC)
- [Joana Elise](https://github.com/joanaeliseal)
- [Maira Larissa](https://github.com/Maira-larissa)
