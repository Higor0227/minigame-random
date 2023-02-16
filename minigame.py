import random

start = int(input('Você ataca! Digite 1 para rolar o dado e obter um valor de 1 a 10: '))
dado1a10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if start == 1:
    ataque = random.choice(dado1a10)
    defesa = random.choice(dado1a10)
    hp = ataque - defesa
else:
    print('Ok.')
    exit()

if ataque > defesa:
    print('Congrats! You rolled the dice and get {} of attack against {} of defense. Your final HP is {}.'.format(attack, defense, hp))
elif ataque < defesa:
    print('What a shame! You rolled the dice and get {} of attack against {} of defense. Your final HP is {}.'.format(ataque, defesa, hp))
elif ataque == defesa:
    print('That is a Tie!. Seu ataque foi de {}, contra uma defesa de {}. Seu hp final é de {}.'.format(ataque, defesa, hp))
