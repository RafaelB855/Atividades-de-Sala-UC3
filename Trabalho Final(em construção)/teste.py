from conexao import Conexao
import random
conexaoBanco = Conexao("ClickMed","localhost","5432","postgres","postgres")
 



lista = [1,2,3,4,1,6,4,4,4,2,6,4,6,1,4,1]

# lista2 = lista
# print (lista.set)

resultado = {}

for i in lista:
    if i not in resultado.keys():
        resultado[i] = lista.count(i)
    # for i in resultado.values():
    #     if  i%2 == 0:
    #     resultado.popitem(i)

print(resultado)

m = max(resultado.values())
y = next(k for k, v in resultado.items() if v == m)

# print(y)

# listafinal= []
# listasemifinal = []

# listadoença=["dasdas1","dasdsa2",3]

# listasintomas=[156,"dsadsad3"]

# coisas = (listasintomas[1], listadoença[1] ,listasintomas[0], listadoença[2])

# listafinal.append(coisas)

# print(listafinal)

# rafa= "rafa"

# rafa2 = rafa.upper()
# print(rafa,rafa2)