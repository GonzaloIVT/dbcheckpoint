"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Productos, Negocios
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET', "POST"])
def handle_hello():
    if request.method == "GET":
        all_people = User.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))

        return jsonify(all_people), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "usuario" not in body:
            return "Especificar usuario", 400
        if "password" not in body:
            return "Especificar password", 400
        
        onePeople = User.query.filter_by(email=body["email"]).first()
        if onePeople:
            if (onePeople.password == body["password"] ):
                return(jsonify({"mensaje":True}))
            else:
                return(jsonify({"mensaje":False}))
        else:
            return("el mail no existe")



@app.route('/productos', methods=["POST", "GET"])
def obtener_productos():
    if request.method == "GET":
        all_productos = Productos.query.all()
        all_productos = list(map(lambda x: x.serialize(), all_productos))

        return jsonify(all_productos), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "nombre" not in body:
            return "Especificar nombre", 400
        if "categoria" not in body:
            return "Especificar categoria", 400
        if "codigo" not in body:
            return "Especificar codigo", 400

@app.route('/negocios', methods=["POST", "GET"])
def obtener_negocios():
    if request.method == "GET":
        all_negocios = Productos.query.all()
        all_negocios = list(map(lambda x: x.serialize(), all_negocios))

        return jsonify(all_negocios), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "nombre" not in body:
            return "Especificar nombre negocio", 400
        if "trabajadores" not in body:
            return "Especificar trabajador", 400
        

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
