# operadores lógicos & bit a bit
# &     and bit a bit
# |     or bit a bit
# ~     negation
# ^     exclusive or
# Let’s make it easier:

# & requires exactly two 1s to provide 1 as the result;
# | requires at least one 1 to provide 1 as the result;
# ^ requires exactly one 1 to provide 1 as the result.

# operações são tratadas no nível dos bits dos operados.
# útil para trabalhar com "estados" (e suas fusões/combinações)
# veja um exemplo de possíveis estados de um pacote nos Correios:

atraso = 0x01
multa = 0x02

estado_pacote = atraso | multa # atraso e multa juntas
existe_multa = ( (multa & estado_pacote) != 0 ) # pergunte se existe multa
estado_pacote &= ~multa # agora retire a multa
sem_atraso = ~estado_pacote # como seria o estado sem atraso?

# agora, como desafio, procure informações sobre a função 'bin' 
# use-a para imprimir os bits no exemplo acima