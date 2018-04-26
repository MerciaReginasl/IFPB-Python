# processar um café a partir do tamanho e ingredientes
def processar_cafe( nome_cliente, *ingredientes, tam='P' ):
    mensagem = 'Processando um café [' + tam.upper() + '] para [' + nome_cliente.upper() + ']. Aguarde...'
    print( mensagem )
    if ingredientes:
        print( 'Adicionando ingredientes:' )
        for item in ingredientes:
            print( '+ ' + item )
    print( 'Pronto!' )
