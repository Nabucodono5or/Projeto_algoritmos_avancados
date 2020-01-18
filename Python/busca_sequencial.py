def busca_sequencial_nao_ordenado(lista, elemento):
    res = -1
    for i in lista:
        if i == elemento:
            res = i
    return res


def busca_sequencial_ordenado(lista, elemento):
    res = -1
    for i in lista:
        if i == elemento:
            res = i
            break
        if i > elemento:
            break
    return res


def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim)//2
        if lista[meio] > elemento:
            fim = meio - 1
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            return meio
    return -1
