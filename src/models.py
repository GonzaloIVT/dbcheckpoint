from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(120), unique=False, nullable=False)
    theme = db.Column(db.String(120), unique=False, nullable=True)
    font_preferene = db.Column(db.String(120), unique=False, nullable=True)
    negocio = db.Column(db.Integer, unique=True, nullable=False)

    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            "role": self.role,
            "theme": self.theme,
            "font_preference": self.font_preference,
            "negocio": self.negocio
            # do not serialize the password, its a security breach
        }

class Productos(db.Model):
    __tablename__ = "producto"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=False, nullable=True)
    codigo_barras = db.Column(db.String(120), unique=True, nullable=True)
    id_categoria = db.Column(db.Integer, unique=False, nullable=True)
    precio_venta = db.Column(db.Float(50), unique=False, nullable=True)
    image = db.Column(db.String(50), unique=False, nullable=True)
    stock = db.Column(db.Integer, unique=False, nullable=True)
    fecha_ingreso = db.Column(db.String(50), unique=False, nullable=False)
    proveedor = db.Column(db.String(50), unique=False, nullable=False)
    costo_compra = db.Column(db.Float(50), unique=False, nullable=False)
    factura_proveedor = db.Column(db.Integer, unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "codigo_barras": self.codigo_barras,
            "id_categoria": self.id_categoria,
            "precio_venta": self.precio_venta,
            "image": self.image,
            "stock": self.stock,
            "fecha_ingreso": self.fecha_ingreso,
            "proveedor": self.proveedor,
            "costo_compra": self.costo_compra,
            "factura_proveedor": self.factura_proveedor
            # do not serialize the password, its a security breach
        }

class Negocios(db.Model):
    __tablename__ = "negocio"
    id = db.Column(db.Integer, primary_key=True)
    nombre_negocio = db.Column(db.String(120), unique=False, nullable=False)
    trabajadores = db.Column(db.String(120), unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "nombre_negocio": self.nombre_negocio,
            "trabajadores": self.trabajadores
            
        }


