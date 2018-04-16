# tuplas: imutáveis
tipos_conta = ( 'normal', 'poupança', 'universitário' )
# tipos_conta[0] = 'pedro' # erro
# tipos_conta.append('gold') # erro
# del tipos_conta[2] # erro
print( len( tipos_conta ) ) # também se aplica às listas
print( tipos_conta * 2 ) # também se aplica às listas
print( 'normal' in tipos_conta  ) # também se aplica às listas
print( 'gold' not in tipos_conta  ) # também se aplica às listas
tipo_gold = ( 'gold', ) # sintaxe para tupla com 1 elemento
tipos_conta = tipos_conta + tipo_gold # nova tupla combinada--não se aplica às listas
print( tipos_conta )
#tipos_conta = tipos_conta - tipo_gold # erro

# dicionário: key-value, não há garantia de ordem
dic_produtos= { 300 : 'celular',
                100 : 'mochila', 
                200 : 'notebook' }
print( dic_produtos )

p = dic_produtos[ 200 ] # se chave fosse string, seria case-sensitive
p = dic_produtos.get( 200 )
print( p )
print( dic_produtos.keys() ) # retorna lista
print( dic_produtos.values() ) # retorna lista
print( dic_produtos.items() ) # retorna lista de tuplas/pares

# varrendo
for k in sorted( dic_produtos.keys() ):
    print( dic_produtos.get( k ) )

for k,v in dic_produtos.items():
    print( 'k=', k, 'v=', v )

# remover
valor = dic_produtos.pop( 200 ) # pela chave, retorna valor
print( valor )
par = dic_produtos.popitem() # último, retorna o par
print( par )
del dic_produtos[ 300 ] # del
print( dic_produtos )

# adicionar
chaves = [ 600, 400, 500 ]
valores = [ 'ana', 'pedro', 'caio' ]
dic_clientes = {} # dic vazio

for i, ch in enumerate( chaves ):
    dic_clientes[ ch ] = valores[ i ]
print( dic_clientes )

dic_clientes[ 900 ] = 'maria'
print( dic_clientes )

# 1 chave com "múltiplos" valores? Use valor como 1 tupla ou 1 lista
dic_alunos = {}

def cadastrar_nome_nota_v1_tupla( dic, nome, nota ):
    """dicionário: 1 nome -> 1 TUPLA de notas"""
    if aluno_existe( dic, nome ):
        dic[ nome ] += (nota,)
    else:
        dic[ nome ] = (nota,)

def cadastrar_nome_nota_v2_lista( dic, nome, nota ):
    """dicionário: 1 nome -> 1 LISTA de notas"""
    if aluno_existe( dic, nome ):
        dic.get( nome ).append( nota )
    else:
        dic[ nome ] = [nota]

def ler_nome():
    return input( 'nome do aluno: ' )

def ler_nota():
   return float( input( 'nota (ex. 4.7): ' ) )

def aluno_existe( dic, nome ):
    return nome in dic_alunos.keys()

def sair( entrada ):
    return entrada.lower().strip() == 'sair'

def imprimir_dicionario( dic ):
    if( dic ) : print( dic )
    else:
        print( 'Desculpe. Não há alunos ou notas a serem impressos.' )
    
# algoritmo principal
while True :
    # ler o nome como entrada
    nome = ler_nome()
    # sair do programa?
    if sair( nome ) : break
    # ler uma nota como entrada
    nota = ler_nota() 
    # cadastrar no dicionario
    cadastrar_nome_nota_v1_tupla( dic_alunos, nome, nota )

imprimir_dicionario( dic_alunos )