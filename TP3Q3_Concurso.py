# Função : Eleitor
# Autor : Maurício Castro
# Data : 29/03/2022

# Questão 03 - TP3
# Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10. 
#Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.

# Fluxo de exceção: 
# O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

def fantasia(participantes):
    for i in range(participantes):
        nome = input(f"\nNome do participante: ")
        nota = float(input("Nota do participante: "))
        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida - deve estar entre 0 e 10.\nNota do participante: "))
            
        if i==0:
            nomeVencedor = nome
            notaVencedor = nota
        elif nota > notaVencedor:
            nomeVencedor = nome
            notaVencedor = nota
    
    print(f"\nO(A) vencedor(a) foi: {nomeVencedor}, com a nota {notaVencedor}")
    print("--------- FIM ---------")
print("\n--- CONCURSO DE FANTASIAS ---")

fantasia(5)