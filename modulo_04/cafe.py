# processar um café
# param: nome, lista de ingredientes e um tamanho
def processar_cafe( nome_cliente, *ingredientes, tam='P' ):
    mensagem = 'Processando um café [' + tam.upper() + '] para [' + nome_cliente.upper() + ']. Aguarde...'
    print( mensagem )
    if ingredientes:
        print( 'Adicionando ingredientes:' )
        for item in ingredientes:
            print( '+ ' + item )
    print( 'Pronto!' )
