def busca_inter(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    operacoes = 0

    while inicio <= fim and lista[inicio] <= alvo and alvo <= lista[fim]: #finalmente entendi 
        operacoes = operacoes + 1
        if lista[inicio] == lista[fim]:
            if lista [inicio] == alvo:
                print(f"Alvo encontrado na posicao: {inicio} com {operacoes} de operacoes ")
                return inicio
            break

        pos = inicio + ((alvo - lista[inicio]) * (fim - inicio) // (lista[fim] - lista[inicio])) #sao 3 partes iniciais, distancia do alvo para o inicio
    # tamamho da lista com base em indices e disntancia entre valores da lista
    #depois ele pega a distancia do alvo e multiplica com o tamanho da lista em indices
    #pra depois dividir pela distancia do primeiro valor ate o ultimo
    #ai o resultado vai pro pos 

        if lista[pos] == alvo:
            print(f"Encontrado na posicao {pos} com {operacoes} de operacoes")
            return pos
        elif lista[pos] < alvo:
            inicio = pos + 1
        else:
            fim = pos - 1
        
    print(f"Não encontrado, quantidade de operacoes {operacoes}")
    return -1 #represntq um nao encontrado

    

list_numeros = [10,20,30,40,50,60,70,80,90,100]

busca_inter(list_numeros, 67)
