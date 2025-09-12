from random import randint
computador= randint (0, 10)

player= input('advinhe o numero que eu pensei ')

if player==computador:

    print (f'você acertou pensei em {computador:.0f}')
else:
    print (f'você errou, pensei em {computador:.0f} ')