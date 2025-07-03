"""
---------------------------------------------------------------------------------------------------------
       REQUISITOS
----------------------------------------------------------------------------------------------------------
1 - o user deve digitar a qntd de gastos permanentes
2 - deve digitar o seu salário 
3 - o sistema vai realizar o quanto sobra
4 - o quanto o user pode investir doq sobrou 
5 - o sistema deve guardar os dados bibli (shelve)
6 - EXTRA (o user pode add o quanto ele deseja juntar e em quanto tempo, e o sistema realiza o calcúlo.)
----------------------------------------------------------------------------------------------------------
"""
import shelve 

print("------------------------------")
print("--------PLANEJAMENTO--------- ")
print("------------------------------")


qntd = int(input("quantos gastos permanentes você tem no mês? (ex: 5) "))

# cria uma lista para armazenar os valores
gastos_permanentes = []

# laço que repete 'qntd' vezes
for i in range(qntd):
    valor = float(input(f"digite o valor do {i+1} gasto permanente: R$ "))
    gastos_permanentes.append(valor) #add na lista

# a funçao sum soma todos dados de uma lista 
soma = sum(gastos_permanentes)
print(f"o total dos seus gastos é de {soma}")


# calculo pra ver oq restou
salario = float(input("qual o valor do seu salário?\n "))
sobra = salario - soma
print(f"o que restou do seu salário é {sobra}\n")

#opção de investimento
resposta = input("deseja ver possibilidade de investimentos? (S/N)\n").lower()

if resposta == 's':
    meta = input("possui alguma meta em especifico? (S/N)\n").lower()
    if meta == 's':
       valor_Juntar = float(input("qual o valor que você precisa juntar? R$ "))
       meses = int(input("em quantos meses deseja juntar esse valor? \n"))
       valor_mensal_necessario = valor_Juntar / meses

       print(f"você precisa guardar R$ {valor_mensal_necessario:.2f} por mês.")

if valor_mensal_necessario <= sobra:
    print(f" com sua sobra mensal de R$ {sobra:.2f}, é possível atingir essa meta.\n")
else:
    print(f" você precisaria guardar R$ {valor_mensal_necessario:.2f} por mês, mas o que resta do seu salário é de apenas R$ {sobra:.2f}, de modo com que não é possível você juntar em {meses} meses")
