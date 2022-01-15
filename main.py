import time
import random
from messages.messages import display_messages

print ('Starting Project again!!')
time.sleep(2)
while True:
    resposta = input('Deseja receber um Conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()