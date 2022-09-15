
# METODO PRIVADO PARA AJUSTE DE RETORNO DAS ROTAS
def genareteResponse(status, mensagem, conteudo):
    response = {"status": status, "mensagem": mensagem}
    if (conteudo is not None):
        response["carga"] = conteudo
    return response