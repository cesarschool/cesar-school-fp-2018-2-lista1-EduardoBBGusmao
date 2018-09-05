## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
import math
def main():
    print("questao 3")
    

    raio = float(input("Digite o raio de uma circunferência:\n"))

    area = math.pi*raio**2
    comprimento = math.pi*2*raio
    print("Essa circunferência tem raio: ", raio, "\nDiametro: ", raio*2, "\nÁrea: ", area, "\nComprimento: ", comprimento)


    
if __name__ == '__main__':
    main()
