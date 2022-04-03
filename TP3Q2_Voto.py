# Função : Eleitor
# Autor : Maurício Castro
# Data : 29/03/2022

# Questão 02 - TP3
# Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
# Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
# Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
# Não tem direito a voto (menor de 16 anos).

# Fluxo de exceção: 
# O programa deve verificar se a idade da pessoa é maior do que zero.

def idadeEleitoral(idade):    
    if (idade >= 16 and idade < 18) or (idade >= 70):        
        print (f"\nNão tem obrigação de votar.")
    elif idade >=18 and idade < 70:
        print (f"\nTem obrigação de votar.")
    else:        
        print (f"\nNão tem direito a voto.")
print("\n--- TENHO DIREITO A VOTO? ---")

idade = int(input(f"\nInforme a idade: "))

if idade > 0:
   idadeEleitoral(idade)
else:
    print("--- IDADE INVÁLIDA! ---")
    print("--------- FIM ---------")