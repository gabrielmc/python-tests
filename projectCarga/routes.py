from flask import Flask, request, abort
from http import HTTPStatus
from projectCarga.src.utils import utilities
from projectCarga.src.services.services import *

app = Flask("API-Monitora")
app_infos = dict(version='1.0', title='API Cargas',
 description='Essa API tem o intuito de ser o exemplo para carregamento de dados',
 contact_email='gabriel.cerqueira@inema.ba.gov.br', doc='/documentacao')

"""
Requisições GET / POST / PUT / DELETE
With application/json mimetype.
"""
@app.route("/monitora", methods=["GET"])
def get_cargas():
    cargas = selectAllService()
    if cargas is None:
        return utilities.genareteResponse(HTTPStatus.NOT_FOUND, "Cargas não encontradas !", None)
    return utilities.genareteResponse(HTTPStatus.OK, "Cargas", cargas)


@app.route("/monitora/id/<string:_id>", methods=["GET"])
def get_cargabyId(_id):
    carga = selectByIdService(_id)
    if carga is None:
        return utilities.genareteResponse(HTTPStatus.NOT_FOUND, "Carga não encontrada !", None)
    return utilities.genareteResponse(HTTPStatus.OK, "Carga", carga)


@app.route("/monitora/create", methods=["POST"])
def post_carga():
    body = request.get_json()
    if body is None:
        return utilities.genareteResponse(HTTPStatus.BAD_REQUEST, "Parâmetro nome obrigatório !", None)
    if not body.get('nome'):
        abort(400)
    if not body.get('carga'):
        abort(400)
    new_carga = {"nome": body.get("nome"), "carga": body.get("carga"), "data": body.get("data")}
    status = inserirService(new_carga)
    return utilities.genareteResponse(HTTPStatus.OK, "Carga efetuada", status)


@app.route("/monitora/edit/<string:id>", methods=["PUT"])
def edit_carga(id):
    if id is None:
        return utilities.genareteResponse(HTTPStatus.FORBIDDEN, "[ID] Inválido !", None)
    data = request.get_json(force=True)
    if not data.get('nome'):
        abort(400)
    carga = updateService(id, data)
    return utilities.genareteResponse(HTTPStatus.OK, "Carga editada", carga)


@app.route("/monitora/delete/<string:_id>", methods=["DELETE"])
def delete_carga(_id):
    if _id is None:
        return utilities.genareteResponse(HTTPStatus.FORBIDDEN, "[ID] Inválido !", None)
    status = deleteByIdService(_id)
    return utilities.genareteResponse(HTTPStatus.OK, "Carga removida !", status)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    # Com o debug=True, ao salvar, recarrega automaticamente a rota com a modificação.
    # app.run() #Exemplo sem debug e sem definição de porta sendo auto: 172.0.0.1
