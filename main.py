import random
import time
from messages.messages import display_messages

print ('Starting Project!')
time.sleep(3)
while True:
    resposta = input('Deseja receber um Conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()