# Função : Dados um valor de renda mensal total
# Autor : Maurício Castro
# Data : 07/04/2022

#Questão 04 - AT
#Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.
#No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.
#No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.
#Ao final de 120 meses, você terá o montante final de R$187.303,05.. 

#A.	Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.

#Exemplo de saída do programa:
#Valor inicial: R$ 10000
#Rendimento por período (%): 0.54
#Aporte a cada período: R$ 1000
#Total de períodos: 120 

#Após 1 períodos(s), o montante será de R$11054.00.
#Após 2 períodos(s), o montante será de R$12113.69.
#Após 3 períodos(s), o montante será de R$13179.11.
#Após 4 períodos(s), o montante será de R$14250.27.
#Após 5 períodos(s), o montante será de R$15327.22.
#(...)
#Após 115 períodos(s), o montante será de R$177406.76.
#Após 116 períodos(s), o montante será de R$179364.76.
#Após 117 períodos(s), o montante será de R$181333.33.
#Após 118 períodos(s), o montante será de R$183312.53.
#Após 119 períodos(s), o montante será de R$185302.42.
#Após 120 períodos(s), o montante será de R$187303.05.


def impressao():
    print(f"Valor inicial: R${valor}")
    print(f"Rendimento por período (%):{rendimento}")
    print(f"Aporte a cada período: R${aportePeriodo}")
    print(f"Total de períodos:{periodo}")

def taxa():
    aTaxa = valor * rendimento / 100
    return aTaxa

valor = float(input("Informe o valor inicial: R$"))
rendimento = float(input("Informe a porcentagem de rendimento por período (%):"))
aportePeriodo = float(input("Informe o valor de aporte de cada período: R$:"))
periodo = int(input("Informe o total de período:"))
cont = 0
valorTaxado = 0

impressao()
taxa()

while cont < periodo:
    cont += 1
    valor += taxa()
    valor += aportePeriodo
    print(f"Após {cont} períodos, o montante será de R${valor:.2f}.")

print("FIM")