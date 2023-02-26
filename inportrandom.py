from random import randint 
from time import sleep     
computador = randint (0,5)
print('-=-' * 20) #enfeite
jogador = int(input('Qual o número que eu pensei?')) 
print('PROCESSANDO...') 
sleep(3)                
print('-=-' * 20)
if jogador == computador:
    print('Parabéns, você é o bichão mermo!')
else:
    print('Não consegue, né, moises! Eu pensei no número {} e não no {}, humano simplório!'.format(computador, jogador))
