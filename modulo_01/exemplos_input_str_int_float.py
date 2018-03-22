# uso das funções input() str(), int() e float()
idade = 45
mensagem = "Pedro tem " + idade + " anos"
print(mensagem)
#---------------------------------------
idade = 45
mensagem = "Pedro tem " + str(idade) + " anos"
print(mensagem)
print("Pedro tem", idade, "anos") # note a diferença de usar com print()
#---------------------------------------
print("Digite seu nome: ")
nome = input()
print (nome)
#---------------------------------------
nome = input("Digite seu nome: ") # retorna string
print (nome)
#---------------------------------------
idade = input("Digite sua idade: ") # retorna string
idade += 1 # e agora?
print ("No seu próximo aniversário, você irá completar", idade, "anos!")
#---------------------------------------
idade = int(input("Digite sua idade: ")) 
idade += 1
print ("No seu próximo aniversário, você irá completar", str(idade), "anos!")
print ("No seu próximo aniversário, você irá completar", idade, "anos!")
#---------------------------------------
altura = float(input("Digite sua altura (ex. 1.74): ")) 
mensagem = "Ok. Entendi. Você tem " + str(altura) + " metros de altura!"
print (mensagem)
#---------------------------------------
altura = float(input("Digite sua altura (ex. 1.74): ")) 
print ("Ok. Entendi. Você tem", altura, "metros de altura!")