"""
nao da para acrescentar nada às strings
len(string)
a[3:7] -> print os elementos de a[3] a a[6] ([start:stop:step], o step pode ainda ser negativo, começando assim no final da string)
a.startswith("fdsfsdfds") e a.endswith("asdasd")
astring.split(" ") separa a string quando tem espaço e coloca-as numa lista
"""

def isVocal (s):
    if s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U' or s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u': 
        return True 
    else: 
        return False

def contaVogais(s: str):
    counter = 0
    for i in range(len(s)):
        if isVocal(s[i]):
            counter += 1
    return counter

def listToString(s):
    str = ""

    for x in s:
        str += x
 
    return str

def retiraVogaisRep (s: str):
    aux = []
    
    if len(s) != 1: i = 0
    else: return s #caso for só um elemento da return

    for i in range(len(s)-1):
        if s[i] != s[i+1]: #se for diferente adiciona à lista aux
            aux.append(s[i])
        elif s[i] == s[i+1] and not (isVocal(s[i])): #se forem iguais mas nao vogal adiciona à lista aux
            aux.append(s[i])
        elif s[i] == s[i+1] and isVocal(s[i]) and i+2 == len(s): 
            aux.append(s[i])
        elif s[i] != s[i+1] and i+2 == len(s):
            aux.append(s[i+1])
    if s[len(s)-1] != aux[len(aux)-1]:
        aux.append(s[len(s)-1])
    aux2 = listToString(aux)
    return aux2

def duplicaVogais(s: str):
    i = 0
    aux = []
    count = 0
    
    for i in range(len(s)):
        aux.append(s[i])
        if isVocal(s[i]):
            aux.append(s[i])
            count+=1
    s = listToString(aux)
    return count
            

string = "Ola, tudo bem?"
aux = duplicaVogais(string)
print(aux)