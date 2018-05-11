# programa jogo do número secreto
# o usuário dever tentar adivinhar o número secreto

# mensagem de boas vindas
print( 'Bem-vindo(a) ao jogo do número secreto!')
print( 'Você deve tentar adivinhar o número secreto\nentre 1..5. Boa sorte!')

# número secreto
numero_secreto = 2
# capturar o palpite do usuário
palpite = int(input('Digite um número (entre 1..5): '))

# enquanto o palpite do usuário não for o número secreto,
# emita mensagens de erro e deixe o usuário tentar novamente
while palpite != numero_secreto:
    print( 'Desculpe. O número', palpite, 'não é o número secreto!')
    print( 'Mas, não desanime! Por favor, tente novamente.')
    # capturar um novo palpite ou loop será infinito
    palpite = int(input('Entre com um outro número (entre 1..5): '))

# se conseguiu sair do laço, então o palpite estava correto
print('Você acertou! O seu palpite:', palpite, 'está correto. Parabéns!')
print('Fim de jogo.')