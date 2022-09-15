from flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app, version="1.0", title="API TESTE",
                       description="A Simple teste API", doc="/docs")

    def run(self,):
        self.app.run(
            port="8090",
            debug=True  #Comentar sempre quando for para produção
        )