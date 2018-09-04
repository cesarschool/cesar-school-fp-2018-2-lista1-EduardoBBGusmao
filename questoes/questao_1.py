## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 1")
    opcao = 'sim'

    while opcao == 'sim' or opcao == 'Sim':
	    salario = float(input("Digite o salário atual?\n"))
	    aumento = float(input("Digite a porcentagem do aumento\n"))

    	salario = salario*(100+aumento)/100
    	print("Esse é o novo salário", salario)
	    opcao = input("Deseja continuar? (Sim/Nao)\n")    


if __name__ == '__main__':
    main()
