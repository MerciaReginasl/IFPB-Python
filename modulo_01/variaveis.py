# declarando variáveis
g = 23
salário = 123.45
nome, idade, bolsista = "Ana", 19, False
#1_salário = 123.45 # erro?

print(g)
print(salário)

# atribuindo valores de tipos diferentes
g = True
g = "mensagem A"
print(g)

# escopo global e local em funções
def foo():
  #global g # descomente para referenciar a var "g" global
  g = "mensagem B"
  print(g)

foo() # invocando a função
print(g)

del g # remover variável
#print(g) # <- por que a mensagem "name 'g' is not defined"?