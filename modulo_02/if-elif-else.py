# sintaxe básica:
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
idade = 11
if idade < 4 :
    desconto = 10.99
elif idade < 8 :
    desconto = 9.99
elif idade < 10 :
    desconto = 8.99
elif idade < 12 :
   desconto = 7.99
elif idade < 14 :
   desconto = 6.99
else: # default (se omitido, pode ser que nenhuma entrada seja executada)
   desconto = 1.99
print("O desconto é de R$ " + str(desconto) + "!")

# testando a negativa
resposta = "b"
if resposta != "c" :
    print ( "A letra '" + resposta, "' não é a correta!", sep='' )

# testando múltiplas condições: and e or
idade_ana = 32
if idade_ana >= 18 and idade_ana <= 70:
    print ( "Obrigado a votar!" ) 

idade_pedro = 82
if ( idade_pedro > 70 ) or ( idade_pedro >= 16 and idade_pedro < 18 ):
    print ( "Voto é facultativo!" ) 

# item está na lista?
lista_convidados = ['maria', 'pedro', 'ana']
nome = input( "Digite seu primeiro nome: " )
if( nome.lower() in lista_convidados ):
    print ("Olá, " + nome.title() + ", seja bem-vindo(a)! Por favor, entre." )

# item não está na lista?
if( nome.lower() not in lista_convidados ):
    print ("Desculpe, " + nome.title() + ", você não foi convidado!" )

# e se lista vazia?
lista_convidados = []
if( lista_convidados ):
    if( nome.lower() in lista_convidados ):
        print ("Olá, " + nome.title() + ", seja bem-vindo(a)! Por favor, entre." )
    else:
        print ("Desculpe, " + nome.title() + ", você não foi convidado!" )
else:
    print ("Tem certeza de que alguém foi convidado?" )

# quando múltiplos testes precisam ser executados
coberturas_pedidas = ['chocolate', 'biscoitos' ]
if 'chocolate' in coberturas_pedidas:
      print ('Adicionando chocolate.')
if 'morango' in coberturas_pedidas:
    print ('Adicionando morango.')
if 'biscoitos' in coberturas_pedidas:
    print ('Adicionando biscoitos.')
if 'castanhas' in coberturas_pedidas:
    print ('Adicionando castanhas.')
print('Seu pedido foi processado. Obrigado.')  

# este if-elif abaixo está correto?
if 'chocolate' in coberturas_pedidas:
    print ('Adicionando chocolate.')
elif 'morango' in coberturas_pedidas:
    print ('Adicionando morango.')
elif 'biscoitos' in coberturas_pedidas:
    print ('Adicionando biscoitos.')
elif 'castanhas' in coberturas_pedidas:
    print ('Adicionando castanhas.')
print('Seu pedido foi processado. Obrigado.')
