import busca_sequencial

lista_ordenada = [1, 3, 4, 5, 7, 9]
lista = [5, 2, 4, 2, 9]
elemento = 5


def main():
    # resultado = busca_sequencial.busca_sequencial_ordenado(lista_ordenada, elemento)
    # resultado = busca_sequencial.busca_sequencial_nao_ordenado(lista, elemento)
    resultado = busca_sequencial.busca_binaria(lista_ordenada, elemento)
    print(resultado)


if __name__ == "__main__":
    main()
