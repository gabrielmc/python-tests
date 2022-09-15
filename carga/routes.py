from flask import Flask, request, abort
from http import HTTPStatus
from Service.services import inserirService, selectAllService, selectByIdService, updateService, deleteByIdService

app = Flask("API-Monitora")

app_infos = dict(version='1.0', title='API Cargas',
                 description='Essa API tem o intuito de ser o exemplo para carregaemnto de dados',
                 contact_email='gabriel.cerqueira@inema.ba.gov.br', doc='/documentacao', prefix='/eee')

"""
Requisições GET / POST / PUT / DELETE
With application/json mimetype.
"""
@app.route("/monitora", methods=["GET"])
def get_cargas():
    cargas = selectAllService()
    if (cargas is None):
        return genareteResponse(HTTPStatus.NOT_FOUND, "Cargas não encontradas !", None)
    return genareteResponse(HTTPStatus.OK, "Cargas", cargas)


@app.route("/monitora/id/<string:_id>", methods=["GET"])
def get_cargabyId(_id):
    carga = selectByIdService(_id)
    if (carga is None):
        return genareteResponse(HTTPStatus.NOT_FOUND, "Carga não encontrada !", None)
    return genareteResponse(HTTPStatus.OK, "Carga", carga)


@app.route("/monitora/create", methods=["POST"])
def post_carga():
    body = request.get_json()
    if (body is None):
        return genareteResponse(HTTPStatus.BAD_REQUEST, "Parâmetro nome obrigatório !", None)
    if not body.get('nome'):
        abort(400)
    if not body.get('carga'):
        abort(400)
    new_carga = {"nome": body.get("nome"), "carga": body.get("carga"), "data": body.get("data")}
    status = inserirService(new_carga)
    return genareteResponse(HTTPStatus.OK, "Carga efetuada", status)


@app.route("/monitora/edit/<string:id>", methods=["PUT"])
def edit_carga(id):
    if (id is None):
        return genareteResponse(HTTPStatus.FORBIDDEN, "[ID] Inválido !", None)
    data = request.get_json(force=True)
    if not data.get('nome'):
        abort(400)
    carga = updateService(id, data)
    return genareteResponse(HTTPStatus.OK, "Carga editada", carga)


@app.route("/monitora/delete/<string:_id>", methods=["DELETE"])
def delete_carga(_id):
    if (_id is None):
        return genareteResponse(HTTPStatus.FORBIDDEN, "[ID] Inválido !", None)
    status = deleteByIdService(_id)
    return genareteResponse(HTTPStatus.OK, "Carga removida !", status)


# METODO PRIVADO PARA AJUSTE DE RETORNO DAS PESQUISAS
def genareteResponse(status, mensagem, conteudo):
    response = {"status": status, "mensagem": mensagem}
    if (conteudo is not None):
        response["carga"] = conteudo
    return response


if __name__ == "__main__":
    # Com essa opção como True, ao salvar, o "site" recarrega automaticamente.
    debug = True
    app.run(host='172.16.7.6', port=5000, debug=debug)
    # app.run() #Exemplo sem debug e sem definição de porta sendo auto: 172.0.0.1
