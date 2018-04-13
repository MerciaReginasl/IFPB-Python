# escopo em funções
var = 58
def foo():
    print( 'var=', var ) # a variável 'externa' pode ser acessada dentro da função
foo()

var = 58
def foo2():
    var = 34 # var é local e faz shadowing
    print( 'var=', var ) 
foo2()
print( 'var-externa:', var )

var = 58
def foo3():
    global var
    var = 34 # náo é mais local
    print( 'var=', var ) 
foo3()
print( 'var-externa:', var )