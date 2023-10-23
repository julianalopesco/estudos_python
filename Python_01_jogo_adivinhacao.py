import random


print("**********************************")
print(" Bem vindo ao jogo de adivinhação!")
print("**********************************")

#variáveis iniciais
num_secreto = random.randrange(1,101) #função que gera um número aleatório
total_tentativas = 0
rodada = 1
pontos = 1000

#escolha do nível
print("Escolha seu nível de dificuldade: \n[1]Fácil \n[2]Médio \n[3]Difícil")

nivel = int(input("Escolha o nível: "))

if(nivel == 1):
    total_tentativas = 20 
elif(nivel ==2): 
    total_tentativas = 10 
else:
    total_tentativas = 5 

#jogo
while (rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas)) #interpolação de string

    chute_str = input("Digite um número entre 1 e 100: ") # a função input sempre retorna uma string
    print("Você digitou ", chute_str)
    #converte a string em int
    chute = int (chute_str)

    if(chute < 1 or chute >100): #limitando as entradas
        print("Você deve digitar um número entre 1 e 100!")
        continue 

    acertou = chute == num_secreto #colocando a condição dentro da variável
    maior = chute > num_secreto
    menor = chute < num_secreto

    if(acertou):
        print("Você acertou! \nVocê fez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("Você errou, o seu número é maior que o número secreto")
        elif(menor):
            print("Você errou, o seu número é menor que o número secreto")
        pts_perdidos = abs(num_secreto - chute) #descontando pontos de acordo com o chute. abs: o chute é um num absoluto
        pontos = pontos - pts_perdidos
    rodada = rodada + 1 #incrementa a variável
print("Fim do jogo. O número era: ", num_secreto)