""""
a.append -> adiciona no final -> aloca espaço automaticamente
a.count(x) -> conta o numero de vezes que x aparece na lista
a.insert(i, x) -> insere x na posição i da lista
a.remove(x) -> remove a primeira aparição de x
a.clear -> remove tudo da lista
a.index (x, [start, end]) -> dá o index de x dado um intervalo
a.sort() -> dá sort à lista
a.pop(n), tira o elemento da posição n
a.remove(x) retira o elemento x da lista
"""

#troca numa lista a, os elementos das posicoes i e j
def swap(a, i, j):
    save = a[i]
    a[i] = a[j]
    a[j] = save

#calcula a soma de uma lista
def soma_lista(a, N):
    soma = 0
    i = 0
    while i < N:
        soma += a[i]
        i+=1
    return soma

#dado uma lista vazia, calcula os quadrados até N numeros naturais
def quadrados(a, N):
    i = 0
    valor = 0
    while i < N:
        lista.append(valor ** 2)
        valor+=1
        i+=1
    return lista

def quadrados2(a, N):
    for i in range(N):
        a.append(i ** 2)

lista = []
#swap(lista, 0, 3)
#lista.reverse()
quadrados2(lista, 4)

print(lista)