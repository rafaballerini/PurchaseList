# Função Novamente?
def novamente():
    print("Deseja adicionar uma nova lista?")
    try:
        resposta = input ("Digite S para SIM ou N para NÃO: ")[0].upper()
        print()
        if resposta == 'S':
            principal()
        elif resposta == 'N':
            print("Fim.")
        else:
            novamente()
    except IndexError:  # Tratamento de erro
        novamente()

# Função Principal
def principal():

# Declaração das variáveis
    lista_de_compras = []
    contador = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]

# Usuário informa a lista
    print("Informe os produtos da lista de compras")
    for i in range(5):
        print(f'{contador[i]} item: ')   
        descricao = input("Descrição: ")
        continuar = False
        while not continuar:  # Tratamento de erro
            try:
                preco = float(input("Preço: "))
            except ValueError:
                print('Valor inválido! Tente novamente.')
            else:
                continuar = True
        print()
        item = {}
        item["Descrição"] = descricao
        item["Preço"] = preco
        lista_de_compras.append(item)

# Impressão da lista
    print("Lista de Compras: ")
    print()
    for i in range(5):
        print(f'{lista_de_compras[i]["Descrição"]} .......... R${lista_de_compras[i]["Preço"]:.2f}')  # Aperfeiçoamento de código

# Mais caro e mais barato
    produto_caro = {}
    produto_barato = {}
    precos = list()
    descs = list()

    for item in lista_de_compras:
        descs.append(item['Descrição'])
        precos.append(item['Preço'])
    produto_caro["Descrição"] = descs[precos.index(max(precos))]
    produto_caro["Preço"] = max(precos)
    produto_barato["Descrição"] = descs[precos.index(min(precos))]
    produto_barato["Preço"] = min(precos)

    print(f'O produto mais caro é {produto_caro["Descrição"].upper()} por R${produto_caro["Preço"]:.2f}')
    print(f'O produto mais barato é {produto_barato["Descrição"].upper()} por R${produto_barato["Preço"]:.2f}')
    print()

# EXECUÇÃO
principal()
novamente()