# Função : Rendimento de aporte mensal
# Autor : Maurício Castro
# Data : 09/04/2022

#Questão 04 - AT
#Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.
#No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.
#No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.
#Ao final de 120 meses, você terá o montante final de R$187.303,05.. 

#A.	Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.

def pontoVirgula(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def hipotese_einstein(valorInicial,rendimento,aporte,periodo):
    print(f" Valor inicial informado: R$ ",pontoVirgula(valorInicial))
    print(f" Rendimento por periodo informado: ",rendimento,"%")
    print(f" Aporte a cada periodo: R$ ",pontoVirgula(aporte))
    print(f" Total de periodos: ",periodo)
    print("")
 
    meses = []
    valorMensal = []
    montante = valorInicial
    for i in range(periodo):
        montante = (montante + (montante*(rendimento/100))) + aporte
        print(f"Após",i+1,"períodos(s), o montante será de R$ ",pontoVirgula(montante),".")
        meses.append(i+1)
        valorMensal.append(round(montante,2))
            
try:
    valorInicial = round(float(input(f"Informe o valor inicial (exemplo: 10000): R$ ").replace(",",".")),2)    
except ValueError:
    valorInicial = 'a'

while valorInicial == 'a' or valorInicial < 0:
    try:
        valorInicial = round(float(input(f"Ops, você não informou um valor válido, digite um valor inicial válido (exemplo: 10000): R$ ").replace(",",".")),2)
    except ValueError:
        valorInicial = 'a'

try:
    rendimento = round(float(input(f"Informe a porcentagem de rendimento por período (exemplo: 0.54): ").replace(",",".")),2)    
except ValueError:
    rendimento = 'b'

while rendimento == 'b' or (rendimento <= 0 and rendimento >= 100):
    try:
        rendimento = round(float(input(f"Ops, você não informou um valor válido, digite um valor da porcentagem do rendimento mensal válido (exemplo: 0.54): ").replace(",",".")),2)
    except ValueError:
        rendimento = 'b'

try:
    aporte = round(float(input(f"Informe o valor de aporte de cada período (exemplo: 1000): R$: ").replace(",",".")),2)    
except ValueError:
    aporte = 'c'

while aporte == 'c':
    try:
        aporte = round(float(input(f"Ops, você não informou um valor válido, digite um valor do aporte mensal válido (exemplo: 1000,00): R$ ").replace(",",".")),2)
    except ValueError:
        aporte = 'c'        

try:
    periodo = int(input(f"Informe o total de período (exemplo: 120): "))
except ValueError:
    periodo = 'd'

while aporte == 'd' or periodo <= 0:
    try:
        periodo = int(input(f"Ops, você não informou um valor válido, digite um valor válido de meses (exemplo: 42): "))
    except ValueError:
        periodo = 'd'
hipotese_einstein(valorInicial,rendimento,aporte,periodo)