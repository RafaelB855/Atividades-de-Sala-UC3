from conexao import Conexao
import random
conexaoBanco = Conexao("ClickMed","localhost","5432","postgres","postgres")
 



lista = [1,2,3,4,1,6,4,4,4,2,6,4,6,1,4,1,]

resultado = {}

for i in lista:
    if i not in resultado.keys():
        resultado[i] = lista.count(i)

print(resultado)

m = max(resultado.values())
y = next(k for k, v in resultado.items() if v == m)

print(y)