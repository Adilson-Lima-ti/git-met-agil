import random
from messages.messages import display_messages

while True:
    resposta = input('Deseja receber um Conselho? S/N: ')
    if (resposta == 'S' or resposta == 's'):
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()