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
from models import db, Users, Productos, Negocios, Ventas, Detalleventa, Role, Categoria, Ingreso, Detalleingreso, Metodopago
#from models import Person
import datetime
from flask_jwt_extended import  JWTManager, create_access_token, jwt_required, get_jwt_identity


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)
jwt = JWTManager(app)

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
        all_people = Users.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))

        return jsonify(all_people), 200

    if request.method == "POST":
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "username" not in body:
            return "Especificar usuario", 400
        if "password" not in body:
            return "Especificar password", 400
        
        user = Users()
        user.save()

        
        onePeople = Users.query.filter_by(email=body["email"]).first()
        if onePeople:
            if (onePeople.password == body["password"] ):
                access_token = create_access_token(identity=onePeople.email)
                data = {
                    "info_user": onePeople.serialize(),
                    "token": access_token,
                }
                return(jsonify(data))
            else:
                return(jsonify({"mensaje":False})),401
        else:
            return("el email no existe"),401
        if onePeople: 
            return jsonify({"status": False, "msg": "Email  already in use"}), 400

@app.route("/users/<int:id>", methods=["PUT"])
def put_users(id):

    username= request.json.get("username")
    name= request.json.get("name")
    last_name= request.json.get("last_name")
    password= request.json.get("password")
    email= request.json.get("email")
    role= request.json.get("role")

    user= Users.query.get(id)
    user.name = name
    user.last_name = last_name
    user.password = password
    user.email = email
    user.role = role
    user.update()

    return jsonify(Users.serialize()),200

@app.route("/users/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    
    user=Users.query.get(id)

    if not user: return jsonify({"status": False, "msg": "Usuario no existe"}),400

    user.delete()

    return jsonify({"status": True, "msg": "Usuario borrado"}),200





"""@api.route("/private", methods=['GET'])
@jwt_required()
def profile():
    if request.method == 'GET':
        identity = get_jwt_identity()
        oneSeller = PerfilVendedor.query.filter_by(email=identity).first()
        return jsonify({ "identity": identity, "info_user": oneSeller.serialize()}), 200"""









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
        if "codigo_barras" not in body:
            return "Especificar codigo", 400
        if "nombre" not in body:
            return "Especificar nombre", 400
            
        return jsonify({ "msg": "ok"}), 200
        #if "categoria" not in body:
        #    return "Especificar categoria", 400
    
    productos= Productos()
    productos.save()

@app.route("/productos/<int:id>", methods=["PUT"])
def modificar_producto(id):

    nombre= request.json.get("nombre")
    codigo_barras= request.json.get("codigo_barras")
    id_categoria= request.json.get("id_categoria")
    precio_venta= request.json.get("precio_venta")
    image= request.json.get("image")
    stock= request.json.get("stock")
    fecha_ingreso= request.json.get("fecha_ingreso")
    costo_compra= request.json.get("costo_compra")
    factura_proveedor= request.json.get("factura_proveedor")

    producto= Productos.query.get(id)
    producto.nombre = nombre
    producto.codigo_barras = codigo_barras
    producto.id_categoria = id_categoria
    producto.precio_venta = precio_venta
    producto.image = image
    producto.stock = stock
    producto.fecha_ingreso = fecha_ingreso
    producto.costo_compra = costo_compra
    producto.factura_proveedor = factura_proveedor
    producto.update()

    return jsonify(Productos.serialize()),200

@app.route("/productos//<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    
    producto=Productos.query.get(id)

    if not producto: return jsonify({"status": False, "msg": "Producto no existe"}),400

    producto.delete()

    return jsonify({"status": True, "msg": "Producto borrado"}),200



@app.route('/ventas', methods=["POST", "GET"])
def obtener_ventas():
    if request.method == "GET":
        all_ventas = Ventas.query.all()
        all_ventas = list(map(lambda x: x.serialize(), all_ventas))

        return jsonify(all_ventas), 200

    if request.method == "POST":
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "tipo_comprobante" not in body:
            return "Especificar tipo_comprobante", 400
        if "numero_comprobante" not in body:
            return "Especificar numero_comprobante", 400
        if "fecha" not in body:
            return "Especificar fecha", 400
        if "impuesto" not in body:
            return "Especificar impuesto", 400
        if "total" not in body:
            return "Especificar total", 400

        return jsonify({ "msg": "ok"}), 200
        
@app.route("/ventas/<int:id>", methods=["PUT"])
def modificar_venta(id):

    tipo_comprobante= request.json.get("tipo_comprobante")
    numero_comprobante= request.json.get("numero_comprobante")
    metodo_pago= request.json.get("metodo_pago")
    fecha= request.json.get("fecha")
    impuesto= request.json.get("impuesto")
    total= request.json.get("total")

    venta= Ventas.query.get(id)
    venta.tipo_comprobante = tipo_comprobante
    venta.numero_comprobante = numero_comprobante
    venta.fecha = fecha
    venta.impuesto = impuesto
    venta.total = total
    venta.update()

    return jsonify(Ventas.serialize()),200

@app.route("/ventas//<int:id>", methods=["DELETE"])
def eliminar_venta(id):
    
    venta=Ventas.query.get(id)

    if not venta: return jsonify({"status": False, "msg": "Venta no existe"}),400

    venta.delete()

    return jsonify({"status": True, "msg": "Venta borrada"}),200



@app.route('/detalleventa', methods=["POST", "GET"])
def obtener_detalleventa():
    if request.method == "GET":
        all_detalleventa = Detalleventa.query.all()
        all_detalleventa = list(map(lambda x: x.serialize(), all_detalleventa))

        return jsonify(all_detalleventa), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "cantidad" not in body:
            return "Especificar cantidad", 400
        if "precio" not in body:
            return "Especificar precio", 400

@app.route("/detalleventa/<int:id>", methods=["PUT"])
def modificar_detalleventa(id):

    cantidad= request.json.get("cantidad")
    precio= request.json.get("precio")
    

    detalleventa= Detalleventa.query.get(id)
    detalleventa.tipo_comprobante = tipo_comprobante
    detalleventa.numero_comprobante = numero_comprobante
    
    detalleventa.update()

    return jsonify(Detalleventa.serialize()),200

@app.route("/detalleventa/<int:id>", methods=["DELETE"])
def eliminar_datelleventa(id):
    
    detalleventa = Detalleventa.query.get(id)

    if not detalleventa: return jsonify({"status": False, "msg": "Detalleventa no existe"}),400

    detalleventa.delete()

    return jsonify({"status": True, "msg": "Detalleventa borrada"}),200



@app.route('/categoria', methods=["POST", "GET"])
def obtener_categoria():
    if request.method == "GET":
        all_categoria = Categoria.query.all()
        all_categoria = list(map(lambda x: x.serialize(), all_categoria))

        return jsonify(all_categoria), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "nombre_cat" not in body:
            return "Especificar nombre_cat", 400
        if "descripcion_cat" not in body:
            return "Especificar descripcion", 400
        
        return jsonify({ "msg": "ok"}), 200

@app.route("/categoria/<int:id>", methods=["PUT"])
def modificar_categoria(id):

    nombre_cat= request.json.get("nombre_cat")
    descripcion_cat= request.json.get("descripcion_cat")
    

    categoria= Categoria.query.get(id)
    categoria.nombre_cat = nombre_cat
    categoria.descripcion_cat = descripcion_cat
    
    categoria.update()

    return jsonify(Categoria.serialize()),200

@app.route("/categoria/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    
    categoria = Categoria.query.get(id)

    if not categoria: return jsonify({"status": False, "msg": "Categoria no existe"}),400

    categoria.delete()

    return jsonify({"status": True, "msg": "Categoria borrada"}),200



@app.route('/ingreso', methods=["POST", "GET"])
def obtener_ingreso():
    if request.method == "GET":
        all_ingreso = Ingreso.query.all()
        all_ingreso = list(map(lambda x: x.serialize(), all_ingreso))

        return jsonify(all_ingreso), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "proveedor" not in body:
            return "Especificar proveedor", 400
        if "tipo_comprobante_ing" not in body:
            return "Especificar tipo_comprobante_ing", 400
        if "numero_comprobante_ing" not in body:
            return "Especificar numero_comprobante", 400
        if "fecha_ing" not in body:
            return "Especificar fecha", 400
        if "impuesto_ing" not in body:
            return "Especificar impuesto", 400
        if "total_ing" not in body:
            return "Especificar total", 400

        return jsonify({ "msg": "ok"}), 200

@app.route("/ingreso/<int:id>", methods=["PUT"])
def modificar_ingreso(id):

    proveedor= request.json.get("proveedor")
    tipo_comprobante_ing= request.json.get("tipo_comprobante_ing")
    numero_comprobante_ing= request.json.get("numero_comprobante_ing")
    fecha_ing= request.json.get("fecha_ing")
    impuesto_ing= request.json.get("impuesto_ingt")
    total_ing= request.json.get("total_ing")
    

    ingreso= Categoria.query.get(id)
    ingreso.proveedor = proveedor
    ingreso.tipo_comprobante_ing = tipo_comprobante_ing
    ingreso.numero_comprobante_ing = numero_comprobante_ing
    ingreso.fecha_ing = fecha_ing
    ingreso.impuesto_ing = impuesto_ing
    ingreso.total_ing = total_ing
    
    ingreso.update()

    return jsonify(Ingreso.serialize()),200

@app.route("/ingreso/<int:id>", methods=["DELETE"])
def eliminar_ingreso(id):
    
    ingreso = Ingreso.query.get(id)

    if not ingreso: return jsonify({"status": False, "msg": "Ingreso no existe"}),400

    ingreso.delete()

    return jsonify({"status": True, "msg": "Ingreso borrado"}),200



@app.route('/detalleingreso', methods=["POST", "GET"])
def obtener_detalleingreso():
    if request.method == "GET":
        all_detalleingreso = Detalleingreso.query.all()
        all_detalleingreso = list(map(lambda x: x.serialize(), all_detalleingreso))

        return jsonify(all_detalleingreso), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "cantidad_di" not in body:
            return "Especificar cantidad_di", 400
        if "precio_di" not in body:
            return "Especificar precio_di", 400
            
        return jsonify({ "msg": "ok"}), 200
    
@app.route("/detalleingreso/<int:id>", methods=["PUT"])
def modificar_detalleingreso(id):

    id_articulo= request.json.get("id_articulo")
    cantidad_di= request.json.get("cantidad_di")
    precio_di= request.json.get("precio_di")
    
    detalleingreso= Detallingreso.query.get(id)
    detalleingreso.id_articulo = id_articulo
    detalleingreso.cantidad_di = cantidad_di
    detalleingreso.precio_di = precio_di
    
    detalleingreso.update()

    return jsonify(Detalleingreso.serialize()),200

@app.route("/detalleingreso/<int:id>", methods=["DELETE"])
def eliminar_detalleingreso(id):
    
    detalleingreso = Detalleingreso.query.get(id)

    if not detalleingresoo: return jsonify({"status": False, "msg": "Detalleingreso no existe"}),400

    detalleingreso.delete()

    return jsonify({"status": True, "msg": "Detalleingreso borrado"}),200














@app.route('/role', methods=["POST", "GET"])
def obtener_role():
    if request.method == "GET":
        all_role = Role.query.all()
        all_role = list(map(lambda x: x.serialize(), all_role))

        return jsonify(all_role), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "nombre_rol" not in body:
            return "Especificar nombre_rol", 400


@app.route('/metodopago', methods=["POST", "GET"])
def obtener_metodopago():
    if request.method == "GET":
        all_metodopago = Metodopago.query.all()
        all_metodopago = list(map(lambda x: x.serialize(), all_metodopago))

        return jsonify(all_metodopago), 200

    else:
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if "num_pago" not in body:
            return "Especificar num_pago", 400
        if "nombre_metpag" not in body:
            return "Especificar nombre_metpag", 400
        if "otros_datos" not in body:
            return "Especificar otros_datos", 400

        return jsonify({ "msg": "ok"}), 200


@app.route('/negocios', methods=["POST", "GET"])
def obtener_negocios():
    if request.method == "GET":
        all_negocios = Negocios.query.all()
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
