def interpolar(lista, alvo_convertido, alvo):
    inicio = 0 #Definimos o limite inferior
    fim = len(lista) - 1 #Definimos o limite superior
    rodada = 0

    if fim < 0 or alvo_convertido < lista[inicio] or alvo_convertido > lista[fim]: #caso não tenha placa na lista ou o alvo não esteja dentro do intervalo
        print (f"A placa {alvo} não está registrada na lista/banco de dados")
        return -1
    
    while inicio <= fim: # Aqui começa o algoritmo de Busca por Interpolação
        rodada += 1
        if lista[fim] == lista[inicio]: #caso exista apenas uma placa na lista/banco de dados
            if lista[inicio] == alvo_convertido:
                print(f"A placa {alvo} está na posição {inicio}, com {rodada} rodada.")
                return inicio
            break

        posição_estimada = inicio + (
            ((fim - inicio) * (alvo_convertido - lista[inicio])) // (lista[fim] - lista[inicio]) #Fórmula da Interpolação Linear, onde é feita a estimativa de onde a placa está localizada na lista
        )

        if posição_estimada < inicio or posição_estimada > fim: #caso a posição do indice estiver fora do intervalo da lista
            break

        #Operações de comparação igual da Busca Binária
        if lista[posição_estimada] == alvo_convertido:
            print (f"A placa {alvo} está na posição {posição_estimada}, com {rodada} rodada.")
            return posição_estimada
        elif lista[posição_estimada] > alvo_convertido:
            fim = posição_estimada - 1 #Ajuste no limite superior
        else: #lista[posição_estimada] < alvo_convertido
            inicio = posição_estimada + 1 #Ajuste no limite inferior
    print (f"A placa {alvo} não está registrada na lista/banco de dados, com {rodada} rodada.") #Caso a placa não seja encontrada na lista, retornará -1
    return -1

def placa_para_numero(placa):
    placa = placa.upper() #Aqui é só pra garantir que a placa se mantenha no padrão das letras ficarem maiúsculas
    n = 0 #Somátorio da placa convertida em número
    for caracter in placa:
        if caracter.isdigit(): #Se o caracter for um número
            n = n * 10 + int(caracter) #Cálculo da base 10 (0-9)
        else: #Se o caracter for um char/string
            n = n * 26 + (ord(caracter) - 65) #Cálculo da base 26 (A-Z)
    return n


def main():
    lista_placa = ["AZZ9Z99", "BAA0A00", "CAA0A01", "DAA0A02", "EAA0A03", "FAA0A04", "ZZZ9Z99"] #Lista de Placas
    buscar = "FAA0A04" #Nosso alvo para buscar a placa no "banco de dados"
    print(sorted(lista_placa))
    lista_numerica = [placa_para_numero(placa) for placa in lista_placa] #para toda placa na lista de placas, chamará a função "placa_para_número" a partir do índice 0
    alvo_convertido = placa_para_numero(buscar) #O alvo/a placa a ser buscada vai ser convertida em número
    interpolar(sorted(lista_numerica), alvo_convertido, buscar) #Jogamos a lista das placas ordenada e o alvo como parâmetros
    print (sorted(lista_numerica))

if __name__ == "__main__":
    main()