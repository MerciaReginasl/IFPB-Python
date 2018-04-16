# tuplas: imutáveis
tipos_conta = ( 'normal', 'poupança', 'universitário' )
# tipos_conta[0] = 'pedro' # erro
# tipos_conta.append('gold') # erro
# del tipos_conta[2] # erro
print( len(tipos_conta) ) # também se aplica às listas
print( tipos_conta * 2 ) # também se aplica às listas
print( 'normal' in tipos_conta  ) # também se aplica às listas
print( 'gold' not in tipos_conta  ) # também se aplica às listas
tipo_gold = ( 'gold', ) # sintaxe para 1 elemento
tipos_conta = tipos_conta + tipo_gold # nova tupla combinada--não se aplica às listas
print( tipos_conta )
#tipos_conta = tipos_conta - tipo_gold # erro