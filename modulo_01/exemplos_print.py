# a função print():
# aceita 0 ou + argumentos---pode ser números, strings, listas, etc.
# sintaxe: print( valor, ..., sep='', end='\n'), como default
print("Olá, Python!")
print("Isto é uma string de caracteres (aspas duplas)")
print('Isto também é uma string de caracteres (aspas simples)')

print('A mensagem dizia: "Contacte o administrador"') 
print("A mensagem dizia: 'Contacte o administrador'") 
print("Também pode haver aspas 'simples' e \"duplas\"") # caracteres de escape
print("O path do arquivo: \"C:\\Projetos\\2018\\logo.png\"") # caracteres de escape

print("Linguagens:\nJava\nC++\nJavaScript") # caracteres de escape
print("Alunos:\n\tJosé\n\tPedro") # caracteres de escape

print("Uma linha")
print() # o que isso faz?
print("Uma outra linha")

# argumentos podem ser passados separadamente, por vírgulas
print("Uma", "mensagem", "muito", "importante")

# por default, print() separa os argumentos com espaços, por conta de sep=' '
print("Uma", "mensagem", "muito", "importante", sep='-') # mas, posso mudar isso

# por default, print() inicia a impressão em uma nova linha, por conta de end='\n'
print("Olá")
print("usuário")
print("Olá", end='')
print("usuário")
print("Obrigado", "por", "retornar", "ao", "site", "Usuário", sep="*", end="####\n\n\n\n")
print("Data: 02/02/2002")

# aproveitando pra combinar/concatenar strings
print( "Olá, " + "Ana " + "Silva" + "!" )
# algumas funções utilitárias
print( "ana silva".title() )
print( "ana silva".capitalize() )
print( "ana silva".upper() )
print( "ANA SILVA".lower() )
# funções utilitárias para remover espaços indesejados
print("Linguagem       ".rstrip() + "           Python".lstrip())
print("A" + "   B   ".strip() + "C")