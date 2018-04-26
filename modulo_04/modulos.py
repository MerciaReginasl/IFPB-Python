# modularização:
#  - divisão de algo (e.g., programa) grande em partes 
#    menores e mais fáceis de gerenciar
#  - a ideia é agrupar suas funções em um módulo separado e permitir
#    que outros possam "importá-lo" permitindo o reuso
#  - usuário não precisa conhecer dos detalhes de implementação do módulo,
#    mas apenas conhecer os protótipos das rotinas e sua interface de uso
# 

# importar tornando as entidades disponíveis
# ao importar assim, use: nome_modulo.função()
import math 

print('3!=', math.factorial(3))
# print(factorial(3)) # erro

# importar algo específico do módulo
# from <nome_modulo> import <função_0, função_1, função_2>
# desse jeito, não precisa usar o nome qualificado
from datetime import date
hoje = date.today()
print(hoje)

# exemplo data
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

from datetime import datetime
dt = datetime.now() # data & hora
print(dt)
print(dt.strftime("%Y")) # %y/Y - ano
print(dt.strftime("%A")) # %a/A - dia/semana
print(dt.strftime("%b")) # %b/B - mês
print(dt.strftime("%d")) # %d/D - dia/mês
print(dt.strftime("%A, %d de %B de %Y"))

# exemplo data & hora
print(dt.strftime("%c")) # data & hora c/ locale
print(dt.strftime("%x")) # data c/ locale
print(dt.strftime("%X")) # hora c/ locale
print(dt.strftime("%I:%M:%S %P")) # 12H:M:S AM/PM
print(dt.strftime("%H:%M")) #24H:M

# alias: funções
# from <nome_modulo> import <função_0> as <alias>
from math import sqrt as raiz_quadrada
print('raiz_quadrada(9)=', raiz_quadrada(9))

# alias: módulos
# import <nome_modulo> as <alias>
import math as modulo_matematica
print('2**5=', modulo_matematica.pow(2,5))

# from math import *
# Python irá copiar todas as funções para seu programa.
# melhor evitar esta notação: 
#  - se houver math.funcao == minha.funcao,
#    pode haver resultados inesperados
# melhor importar algo específico 
# ou importar o módulo e usar nome qualificado