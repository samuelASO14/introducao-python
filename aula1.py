import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nomes=["Alice","Joao","Ana","Jose","Carlos","Janaina","Caio","Cristiane"]
nomes_com_c=[]
nomes_com_j=[]
for nome in nomes:
    if nome.startswith("C"):
        nomes_com_c.append(nome)
    elif nome.startswith("J"):
        nomes_com_j.append(nome)

print(nomes_com_c)
print(nomes_com_j)

idades=[17,18,25,43,15,29,36,50]
idades_maiores18 = []
idades_menores18 = []
for idade in idades:
    if idade > 18:
        idades_maiores18.append(idade)
    elif idade<=18:
        idades_menores18.append(idade)
print(idades_maiores18)
print(idades_menores18)

salarios=[2000,5000,1500,2100,5000,1500,2000,2000]
contagem={}    #dicionario vazio
for salario in salarios:
    if salario in contagem:
        contagem[salario]=contagem[salario]+1
    else: 
        contagem[salario]=1
print(contagem)

letras =["A","B","C","C","A","B","A"]
contagem_categorias={}
for letra in letras:
    if letra in contagem_categorias:
        contagem_categorias[letra]=contagem_categorias[letra]+1
    else:
        contagem_categorias[letra]=1

#print(contagem_categorias)

print("oi lazaro")

frutas=["maça","banana","pera","limão","banana","manga",]
contagem_caregorias={}
for fruta in frutas:
    if fruta in contagem_categorias:
        contagem_categorias[fruta]=contagem_categorias[fruta]+1
    else:
        contagem_categorias[fruta]=1

print(contagem_categorias)

numero=1
while numero<=10:
    if numero%5==0:
        print(f"Numero {numero} é divisivel por 5")
    numero+=1

numero=1
while numero<=20:
    if numero%2==0:
        print(f"Numero {numero} é par")
    else:
        print(f"Numero {numero} é impar")
    numero+=1