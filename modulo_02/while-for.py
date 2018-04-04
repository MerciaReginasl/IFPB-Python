# sintaxe geral
# while conditional_expression:
    # instruction
    # o corpo do while deve garantir que a condição venha a se tornar falsa
    # ou teremos um loop infinito
# for <var> in <iterable>:
    # instruction

x = 0
while x < 10:
    print( x, end = '' )
    x += 1 # veja o incremento

# exemplo de loop infinito
# x = 0
# while x < 10:
#     print( x, end = '' )

print()
for x in range( 0, 10 ):
    print( x, end = '' )

print()
for x in range( 0, 10, 2 ):
    print( x, end = '' )

print()
# break & continue
x = 0
while x < 10:
    if x == 4: break
    #if x == 4: 
    #   x += 1
    #   continue
    print( x, end = '' )
    x += 1

print()
for x in range( 0, 10 ):
    if x == 4: break
    #if x == 4: continue
    print( x, end = '' )

print()
# loop sobre uma lista
lista_carros = ['fusca','bmw','audi']
for c in lista_carros:
    print( c.upper() )

# loop sobre uma lista, mas obtendo-se o indice
for i, c in enumerate( lista_carros ):
    print( 'i=', i, 'carro=', c.upper() )

# exemplo laço controlado por sentinela
# bom quando não se conhece de antemão o número de repetições
# este tipo de loop usa a própria entrada para identificar o final do laço
soma, quantidade = 0, 0
número = float( input( 'Digite um número (ou -1 para sair): ' ) )

while número != -1 : # o -1 é a 'flag/sinal' de parada
    quantidade += 1
    soma += número
    número = float( input( 'Digite outro número (-1 para sair): ' ) )
print( 'No total,', quantidade, 'número(s) foi(foram) inserido(s)' )
print( 'A soma calculada é:', soma )

# while-else
# mesmo com condição inicial falsa, será executado 1 vez
# se laço terminar normalmente, será executado 1 vez
# se houver break, não será executado
i = 10
while i < 5:
    #if i == 3: break
    print( i )
    i += 1
else: 
    print('else-while:', i)

# for-else
# mesmo com condição inicial falsa, será executado 1 vez. variável retém valor
# se laço terminar normalmente, será executado 1 vez
# se houver break, não será executado
for i in range(1,1):
#for i in range(5):
    #if i == 3: break
    print( i )
else: # else executado quando loop termina 'normalmente' i.e., sem break
      # se houver break, não será executado
    print('else-for', i)

# # útil, por ex., quando
# for <var> in <iterable>:
# while <condição>:
#     if <achou_item>:
#     processar_item()
#     break
# else:
#     item_nao_encontrado()
preferencias_usuario = ['futebol', 'python', 'vinho', 'rock', 'carros' ] 
pref = 'python'

for l in preferencias_usuario:
    if l == pref: 
        posição = preferencias_usuario.index( pref ) 
        print( 'posição=', posição )
        break
else:
   preferencias_usuario.append( pref.lower() )
print(preferencias_usuario)