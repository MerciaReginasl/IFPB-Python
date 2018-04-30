import cafe

# nome qualificado
cafe.processar_cafe('pedro', 'creme', 'chocolate', 'canela', tam='m')
cafe.processar_cafe('ana')

# import específico da função 
from cafe import processar_cafe
processar_cafe('caio', 'creme') # sem qualificar

# import específico da função & alias
from cafe import processar_cafe as pc
pc('marcos', 'leite', 'chocolate') # sem qualificar

# import de módulo & alias
import cafe as c
c.processar_cafe('marcos', 'leite', 'chocolate')