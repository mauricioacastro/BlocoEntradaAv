# Função : Planejamento financeiro pessoal
# Autor : Maurício Castro
# Data : 07/04/2022

#Questão 03 - AT
#Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo. 
#Se o gasto estiver dentro do percentual recomendado, informe ainda que
#Seus gastos estão dentro da margem recomendada.
#Caso contrário, informe:
#Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max}
#Onde tipo deve ser moradia, educação ou transportes e valor_max deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.

def pontoVirgula(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def diagnosticar(rendaMensal,aluguel,educacao,transporte):
    print(f" RESULTADO:")
    print(f"-"*100)
    p_aluguel = (aluguel/rendaMensal)*100
    m_aluguel = (rendaMensal*0.3)
    if p_aluguel <= 30:
        print(f" MORADIA:")
        print(f" Seus gastos totais com moradia comprometem {p_aluguel:.2f}% de sua renda total. O máximo recomendado é de 30%.")
        print(f" Portanto, seu gasto com moradia no valor de R$ ",pontoVirgula(aluguel)," está dentro da margem recomendada.")
        print(f"-"*100)
    else:
        print(f" MORADIA:")
        print(f" Seus gastos totais com moradia comprometem {p_aluguel:.2f}% de sua renda total. O máximo recomendado é de 30%.")
        print(f" Portanto, idealmente, o máximo de sua renda comprometida deveria ser de R$ ",pontoVirgula(m_aluguel),".")
        print(f"-"*100)
        
    p_educacao = (educacao/rendaMensal)*100
    m_educacao = (rendaMensal*0.2)
    if p_educacao <= 20:
        print(f" EDUCAÇÃO:")
        print(f" Seus gastos totais com educação comprometem {p_educacao:.2f}% de sua renda total. O máximo recomendado é de 20%.")
        print(f" Portanto, seu gasto com educação no valor de R$ ",pontoVirgula(educacao)," está dentro da margem recomendada.")
        print(f"-"*100)
    else:
        print(f" EDUCAÇÃO:")
        print(" ")
        print(f" Seus gastos totais com educação comprometem {p_educacao:.2f}% de sua renda total. O máximo recomendado é de 20%.")
        print(f" Portanto, idealmente, o máximo de sua renda comprometida deveria ser de R$ ",pontoVirgula(m_educacao),".")
        print(f"-"*100)
        
    p_transporte = (transporte/rendaMensal)*100
    m_transporte = (rendaMensal*0.15)
    if p_transporte <= 15:
        print(f" TRANSPORTE:")
        print(f" Seus gastos totais com transporte comprometem {p_transporte:.2f}% de sua renda total. O máximo recomendado é de 15%.")
        print(f" Portanto, seu gasto com transporte no valor de R$ ",pontoVirgula(transporte)," está dentro da margem recomendada.")
        print(f"-"*100)
    else:
        print(f" TRANSPORTE:")
        print(f" Seus gastos totais com transporte comprometem {p_transporte:.2f}% de sua renda total. O máximo recomendado é de 15%.")
        print(f" Portanto, idealmente, o máximo de sua renda comprometida deveria ser de R$ ",pontoVirgula(m_transporte),".")
        print(f"-"*100)

print(" Vamos iniciar um diagnostico financeiro! Presisamos que você entre com alguns dados para avalição: ")

try:
    rendaMensal = round(float(input(f"Por gentileza, digite o valor da renda mensal familiar (exemplo: 5000): R$ ").replace(",",".")),2)    
except ValueError:
    rendaMensal = 'a'

while rendaMensal == 'a' or rendaMensal <= 0:
    try:
        rendaMensal = round(float(input(f"Ops, você não informou um valor válido, digite um valor da renda mensal válido (exemplo: 5000,00): R$ ").replace(",",".")),2)
    except ValueError:
        rendaMensal = 'a'

try:
    aluguel = round(float(input(f"Agora digite o valor do aluguel do imóvel (exemplo: 1760): R$ ").replace(",",".")),2)    
except ValueError:
    aluguel = 'b'

while aluguel == 'b' or aluguel <= 0:
    try:
        aluguel = round(float(input(f"Ops, você não informou um valor válido, digite um valor do aluguel do imóvel válido (exemplo: 1760,00): R$ ").replace(",",".")),2)
    except ValueError:
        aluguel = 'b'

try:
    educacao = round(float(input(f"Digite o valor do gasto com educação (exemplo: 800): R$ ").replace(",",".")),2)    
except ValueError:
    educacao = 'c'

while educacao == 'c' or educacao <= 0:
    try:
        educacao = round(float(input(f"Ops, você não informou um valor válido, digite o valor do gasto com educação válido (exemplo: 800,00): R$ ").replace(",",".")),2)
    except ValueError:
        educacao = 'c'

try:
    transporte = round(float(input(f"Digite o valor do gasto com transporte (exemplo: 300): R$ ").replace(",",".")),2)    
except ValueError:
    transporte = 'd'

while transporte == 'd' or transporte <= 0:
    try:
        transporte = round(float(input(f"Ops, você não informou um valor válido, digite o valor do gasto com transporte válido (exemplo: 300,00): R$ ").replace(",",".")),2)
    except ValueError:
        transporte = 'd'

diagnosticar(rendaMensal,aluguel,educacao,transporte)
