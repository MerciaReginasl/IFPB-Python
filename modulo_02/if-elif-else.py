# sintaxe 
# if true_or_false_condition:
#   perform_operation_if_true != 0
# else:
#   perform_operation_if_false == 0
# always_executed_operation

x, y = 10, 100

# if
if x < y :
    print( "x < y", x < y )

#if-else
if x < y :
    print( "x < y", x < y )
else:
    print( "x > y", x > y )

# if-else's aninhados
if x < y :
    print( "x < y", x < y )
else:
    if x == y : 
        print( "x == y", x == y )
    else:
        print( "x > y", x > y )

# "conditional statement" -- forma resumida
mensagem = "x < y" if x < y else "x > y ou x == y"
print (mensagem)

# if-elif-else
if x < y :
    print( "x < y", x < y )
elif x > y :
    print( "x > y", x > y )
else:
    print( "x == y", x == y )

# if-elif-else (cont.)
opção = int( input("Digite um número inteiro entre [1..5]: ") )
if opção == 1 :
    print( "Você digitou:", opção )
elif opção == 2 :
    print( "Você digitou:", opção )
elif opção == 3 :
    print( "Você digitou:", opção )
elif opção == 4 :
    print( "Você digitou:", opção )
elif opção == 5 :
    print( "Você digitou:", opção )
else: # default (se omitido, pode ser que nenhuma entrada seja executada)
    print( "Opção inválida!" ) 