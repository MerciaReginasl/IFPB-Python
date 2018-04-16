# uso de listas
# uma coleção de itens numa ordem particular

usuários = [ 'pedro','ana','caio' ]
print( usuários )

# tamanho da lista
print( 'qte usuários:', len(usuários) )

# tipos diferentes
lista = [ True, 'fusca', 45, 0xA, 0o7, 3E-02 ]
print ( lista )

# obter/consultar
primeiro = lista[0] # primeira posição é 0, em vez de 1!
ultimo = lista[-1]
print( primeiro, ultimo  )
print( lista[1].upper(), 'encontra-se no índice:', lista.index( 'fusca' ) )

# modificar
usuários[2] = 'admin'
mensagem = 'O login "' + usuários[2].upper() + '" já existe.\nTente novamente.'
print( mensagem )

# adicionar
usuários.append( 'daniel' ) # no final
print( 'qte usuários:', len(usuários) )
print( usuários )

estados = [] # vazia
estados.append( 'enviado' )
estados.append( 'processado' )
estados.append( 'pago' )
print( estados )

# adicionar com índice (insert(<indice>, <elemento>))
estados.insert( 0, 'devolvido' ) # outros itens serão 'deslocados' para à direita
print( estados )

# remover pelo índice
del estados[1]
print( estados )
elem = estados.pop( 1 ) # pode usar índice
print( 'removido=', elem )
print( estados )
#del estados[50] # erro

# remover do final
elem = estados.pop()
print( 'removido=', elem )
print( estados )

# remover a (1a) ocorrência do elemento (não sei o índice)
números = []
for i in range( 5, 21, 5 ): números.append( i ) # [5, 10, 15, 20]
números.remove( 10 ) # não retorna elemento como pop() 
print( números )

# e se houver duplicatas, como removê-las?
números.insert( 2, 10 )
números.append( 10 )
print( números ) # [5, 15, 10, 20, 10]
for e in números: # não preciso usar o índice para iterar
     if e == 10: números.remove( e )
print( números )

# estude as formas abaixo (+simples? teste-as em uma <lista> com várias duplicatas)
# a) while <elemento> in <lista>: lista.remove( elemento )
# b) while <lista>.count( elemento ): <lista>.pop( <lista>.index( elemento ) )

# mas, posso querer usar o índice
soma = 0
for i in range( len( números ) ):
    soma += números[ i ]
print( soma )

# e posso querer usar o índice e elemento
for i, e in enumerate( números ):
    print( 'i=', i, 'e=', e  )

# listas também podem conter outras listas
lista2 = [ 100, 200 ]
lista.append( lista2 )
print( lista )

# copiar elemento
lista[ 1 ] = lista[ 2 ]
print( lista )

# funções utilitárias em listas numéricas
números = []
for num in range( 1, 11 ): 
    números.append( num*2 )
print( números )
print( 'min=', min(números), 'max=', max(números), 'soma=',  sum(números) )

# outra forma (+ compacta) de criar a lista anterior:
números = [ num*2 for num in range( 1, 11 ) ]
print( números )
print( 'min=', min(números), 'max=', max(números), 'soma=',  sum(números) )

# obter uma 'fatia' da lista
fatia = números[ 2:6 ] # é criada uma outra lista
print( fatia )
print( números[ :3 ] )
print( números[ 4: ] )
print( números[ -3: ] ) # os três últimos

for n in números[ :4 ] :  print( str(n) + " ", end=" " )
print()

# remover usando sintaxe fatia
del fatia[2:4]
# remover todos os elementos
fatia.clear() #ou del fatia[:] #ou del fatia[0:len(fatia)]
# del fatia # irá desalocar a lista da memória

# copiar
lista_clone = números[ : ] # 2 listas
print( lista_clone )

# cuidado
lista_clone = números # 1 lista com 2 referências
lista_clone.clear() 
print( len( números ) )