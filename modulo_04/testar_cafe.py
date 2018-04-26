import cafe

cafe.processar_cafe('pedro', 'creme', 'chocolate', 'canela', tam='l')
cafe.processar_cafe('ana')

from cafe import processar_cafe
processar_cafe('caio', 'creme') # sem qualificar

# alias
from cafe import processar_cafe as pc
pc('marcos', 'leite', 'chocolate', tam='M') # sem qualificar

# alias: módulo
import cafe as c
c.processar_cafe('marcos', 'leite', 'chocolate', tam='M')
