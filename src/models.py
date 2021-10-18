from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(120), unique=False, nullable=False)
    theme = db.Column(db.String(120), unique=False, nullable=True)
    font_preference = db.Column(db.String(120), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email,
            "role": self.role,
            "theme": self.theme,
            "font_preference": self.font_preference,

            # do not serialize the password, its a security breach
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit(self)
    




class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=False, nullable=True)
    codigo_barras = db.Column(db.String(120), unique=True, nullable=True)
    id_categoria = db.Column(db.Integer, unique=False, nullable=True)
    precio_venta = db.Column(db.Float(50), unique=False, nullable=True)
    image = db.Column(db.String(300), unique=False, nullable=True)
    stock = db.Column(db.Integer, unique=False, nullable=True)
    fecha_ingreso = db.Column(db.String(50), unique=False, nullable=False)
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
            "costo_compra": self.costo_compra,
            "factura_proveedor": self.factura_proveedor
            # do not serialize the password, its a security breach
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit(self)





class Negocios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_negocio = db.Column(db.String(120), unique=False, nullable=False)
    trabajadores = db.Column(db.String(120), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    rel_negocios_users = db.relationship("Users")
    

    def serialize(self):
        return {
            "id": self.id,
            "nombre_negocio": self.nombre_negocio,
            "trabajadores": self.trabajadores

        }




class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("users.id"))
    tipo_comprobante = db.Column(db.String(120), unique=False, nullable=False)
    numero_comprobante = db.Column(db.String(120), unique=False, nullable=False)
    fecha = db.Column(db.String(50), unique=False, nullable=False)
    impuesto = db.Column(db.Float, unique=False, nullable=False)
    total = db.Column(db.Float, unique=False, nullable=False)
    rel_ventas_users = db.relationship("Users")

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "tipo_comprobante": self.tipo_comprobante,
            "numero_comprobante": self.numero_comprobante,
            "fecha": self.fecha,
            "impuesto": self.impuesto,
            "total": self.total
        }




class Detalleventa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #id_venta = db.Column(db.Integer, db.ForeignKey("ventas.id"))
    #id_articulo = db.Column(db.Integer, db.ForeignKey("productos.id"))
    cantidad = db.Column(db.Integer, unique=False, nullable=False)
    precio = db.Column(db.Integer, unique=False, nullable=False)
    #rel_detalleventas_ventas = db.relationship("Ventas")
    #rel_detalleventas_productos = db.relationship("Productos")
    
    

    def serialize(self):
        return {
            "id": self.id,
            #"id_venta": self.id_venta,
            #"id_articulo": self.id_articulo,
            "cantidad": self.cantidad,
            "precio": self.precio
        }




class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.Integer, db.ForeignKey("users.id"))
    descripcion = db.Column(db.String(120), unique=False, nullable=True)
    rel_users_role = db.relationship("Users", uselist=False)
    
    

    def serialize(self):
        return {
            "id": self.id,
            "nombre_rol": self.nombre_rol,
            "descripcion": self.descripcion
        }




class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_cat = db.Column(db.String(120), unique=False, nullable=True)
    descripcion_cat = db.Column(db.String(120), unique=False, nullable=True)
    

    def serialize(self):
        return {
            "id": self.id,
            "nombre_cat": self.nombre_cat,
            "descripcion_cat": self.descripcion_cat
        }
        


class Ingreso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.String(120), unique=False, nullable=False)
    proveedor = db.Column(db.String(120), unique=False, nullable=False)
    tipo_comprobante_ing = db.Column(db.String(120), unique=False, nullable=False)
    numero_comprobante_ing = db.Column(db.String(120), unique=False, nullable=False)
    fecha_ing = db.Column(db.String(50), unique=False, nullable=False)
    impuesto_ing = db.Column(db.Float, unique=False, nullable=False)
    total_ing = db.Column(db.Float, unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "proveedor": self.proveedor,
            "tipo_comprobante_ing": self.tipo_comprobante_ing,
            "numero_comprobante_ing": self.numero_comprobante_ing,
            "fecha_ing": self.fecha_ing,
            "impuesto_ing": self.impuesto_ing,
            "total_ing": self.total_ing
        }





class Detalleingreso(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    id_ingreso = db.Column(db.Integer, unique=False, nullable=False)
    id_articulo = db.Column(db.Integer, unique=False, nullable=False)
    cantidad_di = db.Column(db.Integer, unique=False, nullable=False)
    precio_di = db.Column(db.Integer, unique=False, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "id_ingreso": self.id_ingreso,
            "id_articulo": self.id_articulo,
            "cantidad_di": self.cantidad_di,
            "precio_di": self.precio_di
        }




class Metodopago(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_pago = db.Column(db.String(120), unique=False, nullable=True)
    nombre_metpag = db.Column(db.String(120), unique=False, nullable=True)
    otros_datos = db.Column(db.String(120), unique=False, nullable=True)
    

    def serialize(self):
        return {
            "id": self.id,
            "num_pago": self.num_pago,
            "nombre_metpag": self.nombre_metpag,
            "otros_datos": self.otros_datos
        }
