def busca_inter(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    operacoes = 0

    while inicio <= fim and lista[inicio] <= alvo and alvo <= lista[fim]:  
        operacoes = operacoes + 1
        if lista[inicio] == lista[fim]:
            if lista [inicio] == alvo:
                print(f"Alvo encontrado na posicao: {inicio} com {operacoes} de operacoes ")
                return inicio
            break

        pos = inicio + ((alvo - lista[inicio]) * (fim - inicio) // (lista[fim] - lista[inicio])) 
    

        if lista[pos] == alvo:
            print(f"Encontrado na posicao {pos} com {operacoes} de operacoes")
            return pos
        elif lista[pos] < alvo:
            inicio = pos + 1
        else:
            fim = pos - 1
        
    print(f"Não encontrado, quantidade de operacoes {operacoes}")
    return -1 

    

list_numeros = [5, 8, 12, 16, 20, 25, 30, 40, 70, 100]
busca_inter(list_numeros, 40)
