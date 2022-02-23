import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''

    lista_categ = [] #lista onde são adionadas as categorias sem repeti-las
    contador = 0
    while contador < len(dados):
        aux = dados[contador] #auxiliar para evitar repetições
        contador += 1
        if not aux['categoria'] in lista_categ: # evita a repetição de categorias já adicionadas
            lista_categ.append(aux['categoria']) # adiciona a categoria a lista

    return (lista_categ)

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''

    prod_categ = [] #lista pra adicionar os produtos da categoria selecionada
    contador = 0

    while contador < (len(dados)):
        aux = dados[contador]  # auxiliar para usar no if
        contador += 1
        if aux['categoria'] == categoria:  # verifica produtos na categoria selecionada e armazena em uma lista
            prod_categ.append(aux)

    return (prod_categ)

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    # Laço de repetição converte os valores de string para float
    for i in range(len(dados)):
        dados[i]['preco'] = float(dados[i]['preco'])

    prod_categ = listar_por_categoria(dados, categoria)
    prod_caro = {}
    mais_caro = 0
# Laço pra verificar qual o produto mais caro da categoria dada
    for i in range(len(prod_categ)):
        if prod_categ[i]['preco'] > mais_caro:
            prod_caro = prod_categ[i]
            mais_caro = prod_categ[i]['preco']

    return(prod_caro)

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    # Laço de repetição converte os valores de string para float
    for i in range(len(dados)):
        dados[i]['preco'] = float(dados[i]['preco'])

    prod_categ = listar_por_categoria(dados, categoria)
    prod_barato = {}
    mais_barato = produto_mais_caro(dados,categoria)['preco']

# Laço pra verificar qual o produto mais barato da categoria dada
    for i in range(len(prod_categ)):
        if prod_categ[i]['preco'] < mais_barato:
            prod_barato = prod_categ[i]
            mais_barato = prod_categ[i]['preco']

    return (prod_barato)

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''

    # Laço de repetição converte os valores de string para float
    for i in range(len(dados)):
        dados[i]['preco'] = float(dados[i]['preco'])

    # Laço dupo realiza a ordenação da lista de dicionarios com base nos preços.
    n = len(dados)
    for j in range(n - 1):
        indice_minimo = j
        for i in range(j, n):
            if dados[i]['preco'] < dados[indice_minimo]['preco']:
                indice_minimo = i
        if dados[j]['preco'] > dados[indice_minimo]['preco']:
            aux = dados[j]
            dados[j] = dados[indice_minimo]
            dados[indice_minimo] = aux

    dez_mais_caros = []
    for i in range(10):
        dez_mais_caros.append(dados[(i + 1) * -1])

    return dez_mais_caros

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    # Laço de repetição converte os valores de string para float
    for i in range(len(dados)):
        dados[i]['preco'] = float(dados[i]['preco'])

    # Laço dupo realiza a ordenação da lista de dicionarios com base nos preços.
    n = len(dados)
    for j in range(n - 1):
        indice_minimo = j
        for i in range(j, n):
            if dados[i]['preco'] < dados[indice_minimo]['preco']:
                indice_minimo = i
        if dados[j]['preco'] > dados[indice_minimo]['preco']:
            aux = dados[j]
            dados[j] = dados[indice_minimo]
            dados[indice_minimo] = aux

    dez_mais_baratos = []
    for i in range(10):
        dez_mais_baratos.append(dados[i])

    return dez_mais_baratos

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''

    opcao = input('Selecione uma opção\n1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n'
          '4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair\nOpção: ')

    while opcao != '0':
        if opcao == '1':
            categorias = listar_categorias(dados)
            for i in range (len(categorias)):
                print(i+1, categorias[i])

        elif opcao == '2':
            categoria = input('Digite a categoria desejada: ')
            prod_categ = listar_por_categoria(dados, categoria)
            print(f'Os produtos da categoria {categoria} são: ')
            for i in range(len(prod_categ)):
                print(prod_categ[i])

        elif opcao == '3':
            categoria = input('Digite a categoria desejada: ')
            mais_caro = produto_mais_caro(dados, categoria )
            print(f'Produto mais caro da categoria: {categoria}\n{mais_caro}')

        elif opcao == '4':
            categoria = input('Digite a categoria desejada: ')
            mais_barato = produto_mais_barato(dados, categoria)
            print(f'Produto mais barato da categoria: {categoria}\n{mais_barato}')

        elif opcao == '5':
            dez_mais_caros = top_10_caros(dados)
            print('Estes são os dez produtos mais caros: ')
            for i in range(len(dez_mais_caros)):
                print(dez_mais_caros[i])

        elif opcao == '6':
            dez_mais_baratos = top_10_baratos(dados)
            print('Estes são os dez produtos mais baratos: ')
            for i in range(10):
                print(dez_mais_baratos[i])

        else:
            print('Opção invalida, favor selecionar uma opção valida')
        opcao = input('\n\nSelecione uma opção\n1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n'
          '4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair\nOpção: ',)

    # Programa Principal - não modificar!
d = obter_dados()
menu(d)
