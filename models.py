from flask_sqlalchemy import SQLAlchemy
from requests import delete
db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Numeric(11), nullable=False)
    porcentaje = db.Column(db.Numeric(3), nullable=False)
    primer_nombre = db.Column(db.String(250), nullable=False)
    segundo_nombre = db.Column(db.String(250), nullable=True)
    apellido_paterno = db.Column(db.String(250), nullable=False)
    apellido_materno = db.Column(db.String(250), nullable=True)
    direccion = db.Column(db.String(250), nullable=False)
    fono = db.Column(db.Numeric(3), nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    comuna_id = db.Column(db.Numeric(3), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "rut": self.rut,
            "porcentaje": self.porcentaje,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "corro": self.correo,
            "estado": self.estado,
            "comuna_id": self.comuna_id,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Venta(db.Model):
    __tablename__ = 'Venta'
    id_venta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    descuento = db.Column(db.Numeric(999999), nullable=True)
    subtotal = db.Column(db.Numeric(999999), nullable=False)
    iva = db.Column(db.Numeric(999999), nullable=False)
    total = db.Column(db.Numeric(999999), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    cliente_id = db.Column(db.Numeric(3), nullable=False)
    vendedor_id = db.Column(db.Numeric(3), nullable=False)
    despacho = db.Column(db.Numeric(999), nullable=False)
    

    def serialize(self):
        return {
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "descuento": self.descuento,
            "subtotal": self.subtotal,
            "iva": self.iva,
            "total" : self.total,
            "estado" : self.estado,
            "vendedor_id": self.vendedor_id,
            "despacho": self.despacho,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Descuento(db.Model):
    __tablename__ = 'Descuento'
    id_descuento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    fecha = db.Column(db.DateTime)
    porcentaje = db.Column(db.Numeric(999), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    

    def serialize(self):
        return {
            "id_descuento": self.id_descuento,
            "nombre": self.nombre,
            "fecha": self.fecha,
            "porcentajo": self.porcentaje,
            "estado": self.estado,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Producto(db.Model):
    __tablename__ = 'Producto'
    id_producto = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(250), nullable=False)
    nombre = db.Column(db.String(250), nullable=False)
    valor_venta = db.Column(db.Numeric(9999999), nullable=False)
    stock = db.Column(db.Numeric(999), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    imagen = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    

    def serialize(self):
        return {
            "id_producto": self.id_producto,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "valor_venta": self.valor_venta,
            "stock": self.stock,
            "descripcion": self.descripcion,
            "imagen": self.imagen,
            "estado": self.estado,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Descuento_Producto(db.Model):
    __tablename__ = 'Descuento_Producto'
    producto_id = db.Column(db.Integer, primary_key=True)
    descuento_id = db.Column(db.Integer, nullable=False)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_termino = db.Column(db.DateTime, nullable=False)
    

    def serialize(self):
        return {
            "producto_id": self.producto_id,
            "descuento_id": self.descuento_id,
            "fecha-inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Suscripcion(db.Model):
    __tablename__ = 'Suscripcion'
    id_suscripcion = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_termino = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, nullable=False)
    def serialize(self):
        return {
            "id_suscripcion": self.id_suscripcion,
            "fecha_inicio": self.fecha_inicio,
            "fecha_termino": self.fecha_termino,
            "cliente_id": self.cliente_id,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Detalle(db.Model):
    __tablename__ = 'Detalle'
    id_detalle = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Numeric(999), nullable=False)
    valor = db.Column(db.Numeric(9999999), nullable=False)
    descuento = db.Column(db.Numeric(999), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    venta_id = db.Column(db.Numeric(999), nullable=False)
    producto_id = db.Column(db.Numeric(999), nullable=False)
    def serialize(self):
        return {
            "id_detalle": self.id_detalle,
            "cantidad": self.cantidad,
            "valor": self.valor,
            "descuento": self.descuento,
            "estado": self.estado,
            "venta_id": self.venta_id,
            "producto_id" : self.producto_id,


        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Donacion(db.Model):
    __tablename__ = 'Donacion'
    id_donacion = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Numeric(9999999), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Numeric(9999999), nullable=False)
    

    def serialize(self):
        return {
            "id_donacion": self.id_donacion,
            "valor": self.valor,
            "fecha": self.fecha,
            "cliente_id": self.cliente_id,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Comuna(db.Model):
    __tablename__ = 'Comuna'
    id_comuna = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    fecha_inicio = db.Column(db.Numeric(999), nullable=False)
    

    def serialize(self):
        return {
            "id_comuna": self.id_comuna,
            "nombre": self.nombre,
            "fecha_inicio": self.fecha_inicio,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Region(db.Model):
    __tablename__ = 'Region'
    id_region = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), primary_key=False)
    

    def serialize(self):
        return {
            "id_region": self.id_region,
            "nombre": self.nombre,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Vendedor(db.Model):
    __tablename__ = 'Despacho'
    id_vendedor = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(11), nullable=False)
    dv = db.Column(db.String(1), nullable=False)
    primer_nombre = db.Column(db.String(250), nullable=False)
    segundo_nombre = db.Column(db.String(250), nullable=True)
    apellido_paterno = db.Column(db.String(250), nullable=False)
    apellido_materno = db.Column(db.String(250), nullable=True)
    direccion = db.Column(db.String(250), nullable=False)
    fono = db.Column(db.Numeric(9), nullable=False)
    correo = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    comuna_id = db.Column(db.Numeric(999), nullable=False)
    

    def serialize(self):
        return {
            "id_vendedor": self.id_vendedor,
            "rut": self.rut,
            "dv": self.dv,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno" : self.apellido_paterno,
            "apellido_materno" : self.apellido_materno,
            "direccion": self.direccion,
            "fono": self.fono,
            "correo": self.correo,
            "estado": self.estado,
            "comuna_id": self.comuna_id,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Despacho(db.Model):
    __tablename__ = 'Vendedor'
    id_despacho = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(250), nullable=False)
    fecha_entrega = db.Column(db.DateTime, nullable=False)
    hora_entrega = db.Column(db.DateTime, nullable=False)
    rut_recibe = db.Column(db.String(250), nullable=False)
    esta_despacho = db.Column(db.String(1), nullable=False)
    venta_id = db.Column(db.Numeric(9999999), nullable=False)
    comuna_id = db.Column(db.Numeric(9999999), nullable=False)


    def serialize(self):
        return {
            "id_despacho": self.id_despacho,
            "direccion": self.direccion,
            "fecha_entrega0": self.fecha_entrega,
            "hora_entrega": self.hora_entrega,
            "rut_recibe": self.rut_recibe,
            "esta_despacho" : self.esta_despacho,
            "venta_id" : self.venta_id,
            "comuna_id": self.comuna_id,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
