"""
for x in range(10) faz while x < 10, x++
break -> acaba com o ciclo
continue -> ignora o que vem a seguir do continue nessa iteração do ciclo e avança para a proxima
range(2,10,2) faz x de 2 a 10 e faz x+=2
pass, caso tiver um for sem nada, coloco um pass dentro do ciclo para não haver erros
"""

def quadrado(n):
    i = 0
    while i < n:
        j = 0
        while j < n:
            if j+1 < n:
                print("#", end= "")
            else:
                print("#")
            j += 1

        i+=1

def xadrez(n):
    linhas = 0
    while linhas < n:
        linha = 0
        if (linhas % 2) == 0:
            linha = 0
            while linha < n:
                if linha % 2 == 0:
                    print("#", end= "")
                else:
                    print ("_", end="")
                linha+=1
            print("")
            linhas+=1

        else:
            linha = 0
            while linha < n:
                if linha % 2 == 0:
                    print("_", end="")
                else:
                    print("#", end="")
                linha+=1
            print("")
            linhas+=1

def triangulo_horizontal(n):
    linhas = 0
    while linhas < n+1:
        i = 0
        while i < linhas:
            print("#", end="")
            i+=1
        print("")
        linhas+=1
    baixo = n-1
    while baixo > 0:
        i = 0
        while i < baixo:
            print("#", end="")
            i+=1
        print("")
        baixo-=1

triangulo_horizontal(2)
print("")
quadrado(5)
print("")
xadrez(5)