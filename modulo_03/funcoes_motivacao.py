# funções / sub-rotinas ou sub-programas
# muitos programas possuem um algoritmo principal que chama
# sub-programas menores---divisão em partes menores e independentes

# +--------------------------------------------------------
# motivação: algoritmo principal (com problemas): maior de três números
# você consegue identificar pontos fracos no código abaixo?
# +--------------------------------------------------------
print('Bem-vindo(a) ao programa: \"Maior de três números\"\nA partir de três entradas, o programa informará o maior.' )

n1 = float( input( 'digite o número:' ) )
n2 = float( input( 'digite o número:' ) )
n3 = float( input( 'digite o número:' ) )

if n1 >= n2:
    if n1 > n3:
        print('maior=', n1 )
    else:
        print('maior=', n3 )
else:
    if n2 > n3:
        print('maior=', n2 )
    else:
        print('maior=', n3 )

print('Aguarde. Encerrando o programa... Até logo!')

# sintaxe básica:
# def function_name([args])
#   function_body

# declaração
def rodape():
    print( '::: Python in Action :::' )

rodape() # invocação (declaracao deve vir antes)
print( rodape() ) # mas, não há retorno
print( rodape ) # apenas endereço

# com parâmetros
def rodape_autor_pag( titulo, autor, pag ):
    print( ':::', titulo, ':::', autor, 'pág:',  pag )

rodape_autor_pag( 'Python in Action', 'David Beazley', 42 ) # passagem de argumentos para parâmetros
#rodape_autor_pag( 42, 'David Beazley', 'Python in Action' ) # ops!
rodape_autor_pag( pag=42, autor='David Beazley', titulo='Python in Action' ) # a ordem nao importa, neste caso

# com valor default: devem aparecer nas últimas posições
def rodape_autor_pag_def( titulo, autor, pag=1 ):
    print( ':::', titulo, ':::', autor, 'pág:',  pag )

rodape_autor_pag_def( 'Python in Action', 'David Beazley' ) 

# o parâmetro com valor default tornará a passagem de argumento opcional
def formatar_endereco( rua, num, bairro, cep, complemento='' ):
    print( 'R. ' + rua + ', ' + str(num) + ', Bairro:', bairro, '- CEP:', cep, complemento )

formatar_endereco( 'Damasco', 213, 'Sta Rosa', '58416-510' ) # complemento é opcional
formatar_endereco( 'Damasco', 213, 'Sta Rosa', '58416-510', '(Prox. a Madeireira Alves)'  )  

# com retorno
def somar( a, b ):
   resultado = a + b
   return resultado

print( somar( 3, 5 ) )
r = somar( 3, 5 )
print( r )

# modificando listas em funcoes
nums = [ i for i in range( 1, 11 ) ]
def remover_pares( lista_numeros ):
    for n in lista_numeros: 
        if n % 2 == 0: lista_numeros.remove( n )
    return lista_numeros

print( 'remover_pares=' , remover_pares( nums ) )

# como evitar que lista original seja modificada?
nums = [ i for i in range( 1, 11 ) ]
copia = remover_pares( nums[:] ) # passe uma cópia, em vez da original
print( 'copia-remover_pares=' , copia )
print( 'original-remover_pares=' , nums )

# quantidade variada de argumentos
def mostrar_preferencias( nome, *preferencias ):
    print( nome.title(), 'prefere: ' )
    for p in preferencias: 
        print( '\t-' , p  )

mostrar_preferencias( 'ana', 'música', 'livros' )
mostrar_preferencias( 'pedro', 'skate', 'surf', 'natação', 'ioga', 'capoeira' )

print()

# algoritmo com sub-programas
def mensagem_entrada():
    print('Bem-vindo(a) ao programa: \"Maior de três números\".\nA partir de três entradas, o programa informará o maior.' )

def ler_numero():
    return float( input( 'digite o número:' ) )

def maior_numero( num1, num2 ):
    return num1 if num1 >= num2 else num2

def imprimir_maior( num ):
    print('maior=', num )

def mensagem_saida():
    print('Aguarde. Encerrando o programa... Até logo!')

mensagem_entrada()

n1 = ler_numero()
n2 = ler_numero()
n3 = ler_numero()

maior = maior_numero( n1, n2 )
maior = maior_numero( maior, n3 )

imprimir_maior( maior )
# poder-se-ia reduzir mais: imprimir_maior( maior_numero( n3, maior_numero(n1,n2) ) )
mensagem_saida()

# outra alternativa:
def maior_lista_numeros( *numeros ):
    maior = numeros[ -1 ]
    for i in range( len(numeros) - 1):
        if numeros[ i ] > maior: maior = numeros[ i ]
    return maior
    
mensagem_entrada()

n1 = ler_numero()
n2 = ler_numero()
n3 = ler_numero()

maior = maior_lista_numeros( n1, n2, n3 )
imprimir_maior( maior )
mensagem_saida()