# Função : Calcule a divisão de uma conta de bar 
# Autor : Maurício Castro
# Data : 30/03/2022

#Questão 01 - TP3
# Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de pessoas que 
#estavam consumindo e a taxa de serviço que será paga ao garçom.
# Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.

# Fluxo de exceção: 
# O programa deve verificar se o número total de pessoas é maior do que zero.
# O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
# Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.

def pontoVirgula(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    d = c.replace('v','.')
    return d

def calcular_conta(qntPessoas,consumo,percentual):   
    contaPessoa = consumo / qntPessoas    
    servico = round(consumo * (percentual/100),2)    
    totalConta = round((consumo/qntPessoas) + (servico/qntPessoas),2)    
    servicoPessoa = round((servico / qntPessoas),2)
    
    if qntPessoas == 1:
        print(f"\nO valor de consumo foi R$",pontoVirgula(consumo),".")
        print(f"\nVocê informou que pagará",percentual,"% pela taxa de serviço, totalizando R$",pontoVirgula(servico),)
        print(f"\nO valor total da sua conta ficou R$",pontoVirgula(totalConta),".")
    else:
        print(f"\nO valor de consumo foi R$",pontoVirgula(consumo)," e você solicitou dividir em ",qntPessoas," pessoas.")
        print(f"\nVocê informou que pagará",percentual,"% pela taxa de serviço, totalizando R$",pontoVirgula(servico),)
        print(f"\nO valor da taxa de serviço para cada pessoa foi R$",pontoVirgula(servicoPessoa),)
        print(f"\nO valor de consumo para cada pessoa foi de R$",pontoVirgula(contaPessoa),)
        print(f"\nO valor total da conta para cada pessoa ficou R$",pontoVirgula(totalConta),)
    print("--- FIM ---")
    
print("\n--- CONTA DE CONSUMO ---")

try:
    qntPessoas = int(input(f"\nPor favor, digite o número de pessoas em que será dividido a conta: "))
except ValueError:
    qntPessoas = 0
if qntPessoas > 0:  
    try:
        consumo = round(float(input(f"\nPor favor, digite o valor da conta (exemplo: 50.20): ").replace(",",".")),2)
    except ValueError:
        consumo = 0       
    if consumo > 0:
        try:
            percentual = int(input(f"\nQual a porcentagem que deseja pagar pela taxa de seviço (Entre 0% e 100%)? "))
        except ValueError:
            percentual = 101        
        if percentual >= 0 and percentual <= 100:
            calcular_conta(qntPessoas,consumo,percentual)            
        else:
            print("--- VALOR INVÁLIDO! ---")
            print("--------- FIM ---------")                      
    else:        
        print("--- VALOR INVÁLIDO! ---")
        print("-------- FIM ----------")           
else:    
    print("--- VALOR INVÁLIDO! ---")
    print("--------- FIM ---------")