# 🔍 Busca por Interpolação

Implementação e comparação entre **Busca Binária** e **Busca por Interpolação**, usando placas de veículos (padrão Mercosul) como caso de estudo.

---

## 📌 Sobre o projeto

Este projeto explora como algoritmos de busca em listas ordenadas se comportam com diferentes tipos de dados, comparando a busca binária tradicional com a busca por interpolação.

## ⚙️ Como funciona

A busca por interpolação estima a posição do elemento usando a fórmula:

```python
pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])
```

Diferente da busca binária, que sempre olha o meio do intervalo, ela "chuta" matematicamente onde o valor deve estar.

## 📊 Comparação

| Algoritmo | Melhor caso | Pior caso | Requisito |
|---|---|---|---|# Busca por Interpolação
Este é um projeto sobre algoritmos de busca.

## Introdução
A busca por interpolação é uma      variação da busca binária.
Ela   estima a posição do elemento ao invés de sempre pegar o meio.



## Vantagens
* Mais rápida em dados uniformes
*  Complexidade O(log log n) no melhor caso
*      Boa para grandes volumes de dados ordenados


## Desvantagens
1. Pode degenerar para O(n)
1. Depende muito da distribuição dos dados
1.    Mais cálculos por iteração


## Conclusão
Não existe algoritmo universalmente melhor,      depende do contexto. v
| Busca Binária | O(log n) | O(log n) | Lista ordenada |
| Busca por Interpolação | O(log log n) | O(n) | Lista ordenada e uniforme |

## ✅ Vantagens da Interpolação

- Extremamente rápida em dados uniformemente distribuídos
- Reduz drasticamente o número de comparações em grandes volumes de dados

## ⚠️ Desvantagens

- Degenera para O(n) em dados irregulares
- Mais cálculos por iteração (custo computacional maior por passo)
- Risco de divisão por zero se os extremos forem iguais

> **Nota:** a escolha do algoritmo ideal depende inteiramente da distribuição dos dados.

## 🚀 Como rodar

```bash
git clone https://github.com/nevext/inter-py.git
cd inter-py
python detran.py
```

## 👥 Autores

- [@nevext](https://github.com/nevext)
- Amigo colaborador

---

*Projeto desenvolvido para fins acadêmicos.*# Busca por Interpolação
Este é um projeto sobre algoritmos de busca.

## Introdução
A busca por interpolação é uma      variação da busca binária.
Ela   estima a posição do elemento ao invés de sempre pegar o meio.



## Vantagens
* Mais rápida em dados uniformes
* Complexidade O(log log n) no melhor caso
* Boa para grandes volumes de dados ordenados


## Desvantagens
1. Pode degenerar para O(n)
1. Depende muito da distribuição dos dados
1. Mais cálculos por iteração


## Conclusão
Não existe algoritmo universalmente melhor,      depende do contexto. # Busca por Interpolação
Este é um projeto sobre algoritmos de busca.

## Introdução
A busca por interpolação é uma      variação da busca binária.
Ela   estima a posição do elemento ao invés de sempre pegar o meio.



## Vantagens
* Mais rápida em dados uniformes
* Complexidade O(log log n) no melhor caso
* Boa para grandes volumes de dados ordenados


## Desvantagens
1. Pode degenerar para O(n)
1.     <span style="color:...">Depende muito da distribuição dos dados
1.    Mais cálculos por iteração


## Conclusão
Não existe algoritmo universalmente melhor,      depende do contexto. 