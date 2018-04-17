# escopo em funções
def foo():
    print( 'var=', var ) # a variável 'externa' pode ser acessada dentro da função
var = 58
foo()
print( 'var-externa:', var )

def foo2():
    var = 34 # var é local e faz shadowing
    print( 'var=', var ) 
var = 58
foo2()
print( 'var-externa:', var )

def foo3():
    global var
    var = 34 # não é mais local
    print( 'var=', var ) 
var = 58
foo3()
print( 'var-externa:', var )

def foo4():
    global var # tem "força para definir global"
    var = 34 # não é mais local
    print( 'var=', var ) 
# var = ???
foo4()
print( 'var-externa:', var )