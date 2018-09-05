## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    print("questao 5")
    CigarrosPorDia = int(input("Digite quantos cigarros por dia o fumante fuma: \n"))
    Anosfumados = float(input("Digite há quantos anos o fumante fuma: \n"))

    TotalDeCigarros = CigarrosPorDia*(Anosfumados*365)
    DiasPerdidos = (TotalDeCigarros*10/60)/24

    print("Esse fumante já perdeu: ", DiasPerdidos, " dias.")

    
if __name__ == '__main__':
    main()
