import random
import time

qtd = int(input('\nQuantos dados você deseja usar? '))

time.sleep(1)
print ('\nRolando os dados:\n')
time.sleep(2)

def dados():
    for i in range(qtd):
        print (random.randint(1, 6))
        time.sleep(1)
    replay = input('\nQuer jogar novamente? (sim/não): ')
    if replay == ('sim'):
        print (dados())
    else:
        print('')        
        print('')

if qtd != 0:
    dados()

