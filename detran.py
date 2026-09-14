def interpolar(lista, alvo):
    lista = converter_placas(lista) #Converteremos as "Strings Seriadas" para números
    alvo_convertido = placa_para_numero(alvo) #Converteremos o nosso alvo do tipo string em número
    inicio = 0 #Definimos o limite inferior
    fim = len(lista) - 1 #Definimos o limite superior

    while inicio <= fim: # Aqui começa o algoritmo de Busca por Interpolação
        posição_estimada = inicio + (
            (fim - inicio) * (alvo_convertido - lista[inicio]) // (lista[fim] - lista[inicio]) #Fórmula da Interpolação Linear, onde é feito a estimativa de onde a placa está localizada na lista
        )

        #Operações de comparação igual da Busca Binária
        if lista[posição_estimada] == alvo_convertido:
            print (f"A placa {alvo} está na posição {posição_estimada}")
            return
        elif lista[posição_estimada] > alvo_convertido:
            fim = posição_estimada - 1 #Ajuste no limite superior
        else: #lista[posição_estimada] < alvo_convertido
            inicio = posição_estimada + 1 #Ajuste no limite inferior
    
    print (f"A placa {alvo} não está registrada na lista/banco de dados") #Caso a placa não seje encontrada na lista, retornará -1
    return -1

# A partir daqui, são executados algoritmos de conversão das placas mercosul (LLLNLNN) para números
def converter_placas(lista, i = 0): #i -> contador para percorrer a lista de placas
    if i >= len(lista): #Se o contador percorreu por toda lista de placas
        return [] #Retornará a lista convertida
    return [placa_para_numero(lista[i])] + converter_placas(lista, i+1) #Linha de recursividade, onde cada placa da lista será convertida para número acompanhada da função recursiva da próxima placa

def placa_para_numero(placa, n = 0, j = 0): #n -> O somátorio de todos os caracteres string transformado para inteiro ou o próprio inteiro; j -> contador para percorrer todos os caracteres
    placa = placa.upper() #Aqui é só pra garantir que a placa se mantenha no padrão das letras ficarem maiúscula
    if j >= len(placa): #Se o contador percorreu por toda lista de caracteres da placa
        return n #retornará a placa (string) convertida em número (inteiro)
    if placa[j].isdigit(): # Se o caracter for um número
        return placa_para_numero(placa, n * 10 + int(placa[j]), j+1) #retornará a função recursiva com o cálculo de base 10 (0-9) junto do seu incremento (para ir pro próximo caracter)
    else: # Caso o caracter seja uma string
        return placa_para_numero(placa, n * 26 + (ord(placa[j]) - 65), j+1) #retornará a função recursiva com o cálculo de base 26 (A-Z) junto do seu incremento (para ir pro próximo caracter)

def main():
    lista_placa = ["FPM2N55", "EIP3N89", "AZM8I40", "EGT9E69", "PSQ0Z26", "MBM2L92", "TRY3A91"] #Lista de Placas
    buscar = "TRY3A91" #Nosso alvo para buscar a placa no "banco de dados"
    interpolar(sorted(lista_placa), buscar) #Jogamos a lista das placas ordenada e o alvo como parâmetros

if __name__ == "__main__":
    main()