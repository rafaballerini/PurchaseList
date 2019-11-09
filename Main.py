# Função Novamente?
def novamente():
    print("Deseja adicionar uma nova lista?")
    resposta = input ("Digite S para SIM ou N para NÃO: ")
    if resposta == 'S':
        print()
        principal()
    elif resposta == 'N':
        print()
        print("Fim.")
    else:
        print()
        novamente()

# Função Principal
def principal():

# Declaração das variáveis
    lista_de_compras = []
    contador = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    i = 0

# Usuário informa a lista
    print("Informe os produtos da lista de compras")
    while i < 5:
        print(contador[i],"item: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        print()
        item = {}
        item["Descrição"] = descricao
        item["Preço"] = preco
        lista_de_compras.append(item)
        i+=1

# Impressão da lista
    i = 0
    print("Lista de Compras: ")
    print()
    while i < 5:
        print(lista_de_compras[i]["Descrição"],"........R$","%.2f" % lista_de_compras[i]["Preço"])
        i+=1

# Mais caro e mais barato
    i = 0
    produto_caro = {}
    produto_barato = {}
    while i < 5:
        if i == 0:
            produto_caro = lista_de_compras[i]
            produto_barato = lista_de_compras[i]
        else:
            if float(lista_de_compras[i]["Preço"]) > produto_caro["Preço"]:
                produto_caro = lista_de_compras[i]
            elif float(lista_de_compras[i]["Preço"]) < produto_barato["Preço"]:
                produto_barato = lista_de_compras[i]
        i+=1
    print("O produto mais caro é",produto_caro["Descrição"],"por","%.2f" % produto_caro["Preço"])
    print("O produto mais barato é",produto_barato["Descrição"],"por","%.2f" % produto_barato["Preço"])
    print()

# EXECUÇÃO
principal()
novamente()
