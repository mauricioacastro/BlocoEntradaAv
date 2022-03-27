# Função : Eleitor
# Autor : Maurício Castro
# Data : 27/03/2022

idade = 0

idade = int(input("Informe a idade: "))

if idade < 1:
    print("Idade" ,idade, "esta incorreta")
elif idade > 0 and idade < 10:
    print("Não tem direito a voto." )
elif idade > 17 and idade < 70:
    print("Tem obrigação de votar." )
else :
    print("Não tem obrigação de votar.")