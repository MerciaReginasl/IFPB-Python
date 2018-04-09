# ordenação de listas
departamentos = [ 'vendas', 'compras' , 'administrativo', 'financeiro' ]
departamentos.sort() # lista original é alterada
print( departamentos )

departamentos.sort( reverse=True ) # lista original é alterada
print( departamentos )

departamentos.clear()
departamentos = [ 'vendas', 'compras' , 'administrativo', 'financeiro' ]
print( sorted(departamentos) ) # lista original NÃO é alterada
#print( sorted(departamentos, reverse=True) )
print( departamentos )

# inverte de trás pra frente, sem considerar ordem alfabética
print( departamentos )
departamentos.reverse()
print( departamentos )
departamentos.reverse() # voltará a forma original
print( departamentos )

# operator in
# sintaxe: <elem> in <list>
#          <elem> not in <list>
lista_impares = [ 1, 3, 5, 7, 9 ]
print( 7 in lista_impares )
print( 7 not in lista_impares )
print( 2 in lista_impares )
print( 2 not in lista_impares )

# muito útil em for/while/if
bloqueados = [ 'ana', 'pedro', 'caio', 'silvia']
logins = [ 'pedro', 'silvia']

for l in logins:
    if l in bloqueados:
        print( 'O login ' + l.upper() + ' se encontra bloqueado.' )

# matrizes
matriz = [ ['código', 'descrição', 'preço'], 
           ['35', 'Balde', 6.99] ]
print( matriz[0] )
print( matriz[1] )
print( matriz )

print( matriz[0][1] )
matriz[1][2] = 14.99
print( matriz )

linha = matriz[1]
print( linha )
print( linha[2] )

# varrendo uma matriz
# for externo varre o número de linhas
# for interno varre os itens dentro da linha corrente
matriz = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range( len(matriz) ):
    for j in range( len( matriz[i] ) ):
        print(matriz[i][j], end=' ')
    print()

# usando for-in
for linha in matriz:
    for item in linha:
        print( str(item) + ' ', end='' )
    print()

# sintaxe compacta:
m1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
print( 'm1=',m1 )
m2 = [ [0 for item in range(3)] for linha in range(5) ]
print( 'm2=', m2 )