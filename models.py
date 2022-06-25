from flask_sqlalchemy import SQLAlchemy
from requests import delete
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= True)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.Numeric(999), nullable= True)
    password = db.Column(db.String(250), nullable=True)
    mail = db.Column(db.String(250), nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "comuna_id": self.comuna_id,
            "password": self.password,
            "mail": self.mail,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(250), nullable= False)
    primer_nombre = db.Column(db.String(250), nullable= False)
    segundo_nombre = db.Column(db.String(250), nullable= False)
    apellido_paterno = db.Column(db.String(250), nullable= False)
    apellido_materno = db.Column(db.String(250), nullable= True)
    direccion = db.Column(db.String(250), nullable= False)
    comuna_id = db.Column(db.Integer, db.ForeignKey('Comuna.id'), nullable= False)
    comuna = db.relationship('Comuna', backref=db.backref('Cliente', lazy='dynamic'))
    correo = db.Column(db.String(250), nullable=True)
    password = db.Column(db.String(250), nullable=True)
    fono = db.Column(db.String(250), nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "rut": self.rut,
            "primer_nombre": self.primer_nombre,
            "segundo_nombre": self.segundo_nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "direccion": self.direccion,
            "comuna_id": self.comuna_id,
            "comuna": self.comuna,
            "fono": self.fono,
            "correo": self.correo,
            "password": self.password
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
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime)
    descuento = db.Column(db.Numeric(99999), nullable=True)
    subtotal = db.Column(db.Numeric(99999), nullable=False)
    iva = db.Column(db.Numeric(999), nullable=False)
    total = db.Column(db.Numeric(9999), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    cliente_id = db.Column(db.Numeric(999), nullable=False)
    vendedor_id = db.Column(db.Numeric(9), nullable=False)
    despacho = db.Column(db.Numeric(9999), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
    descuento = db.relationship('Descuento', backref=db.backref('Descuento_Producto', lazy='dynamic'))
    nombre = db.Column(db.String(250), nullable=False)
    fecha = db.Column(db.DateTime)
    porcentaje = db.Column(db.Numeric(3), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(250), nullable=False)
    nombre = db.Column(db.String(250), nullable=False)
    valor_venta = db.Column(db.Numeric(9999999), nullable=False)
    stock = db.Column(db.Numeric(999), nullable=False)
    descripcion = db.Column(db.String(250), nullable=False)
    imagen = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, primary_key=True)
    producto = db.relationship('Producto', backref=db.backref('Descuentos_Producto', lazy='dynamic'))
    descuento_id = db.Column(db.Integer, db.ForeignKey('Descuentos.id'), nullable= False)
    descuento = db.relationship('Descuento', backref=db.backref('Descuentos_Producto', lazy='dynamic'))
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_termino = db.Column(db.DateTime, nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_termino = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('Cliente.id'), nullable= False)
    cliente = db.relationship('Cliente', backref=db.backref('Suscripcion', lazy='dynamic'))
    def serialize(self):
        return {
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Numeric(999), nullable=False)
    valor = db.Column(db.Numeric(9999999), nullable=False)
    descuento = db.Column(db.Numeric(999), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    venta_id = db.Column(db.Numeric(9999), nullable=False)
    venta = db.Column(db.Numeric(99999), nullable=False)
    producto_id = db.Column(db.Numeric(9999), nullable=False)
    producto = db.Column(db.Numeric(9999), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "valor": self.valor,
            "descuento": self.descuento,
            "estado": self.estado,
            "venta_id": self.venta_id,
            "venta": self.venta,
            "producto_id" : self.producto_id,
            "producto" : self.producto,


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
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Numeric(99999), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('Cliente.id'), nullable= False)
    cliente = db.relationship('Cliente', backref=db.backref('Donacion', lazy='dynamic'))
    

    def serialize(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "fecha": self.fecha,
            "cliente_id": self.cliente_id,
            "cliente": self.cliente,

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
    id = db.Column(db.Integer, primary_key=True)
    comuna = db.relationship('Comuna', backref=db.backref('Cliente', lazy='dynamic'))
    nombre = db.Column(db.String(250), nullable=False)
    fecha_inicio = db.Column(db.Numeric(999), nullable=False)
    

    def serialize(self):
        return {
            "id": self.id,
            "comuna": self.comuna,
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

class Region(db.Model):
    __tablename__ = 'Region'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), primary_key=False)
    

    def serialize(self):
        return {
            "id": self.id,
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
    id = db.Column(db.Integer, primary_key=True)
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
    comuna = db.relationship('Comuna', backref=db.backref('Cliente', lazy='dynamic'))
    

    def serialize(self):
        return {
            "id": self.id,
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
            "comuna" : self.comuna,

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
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(250), nullable=False)
    fecha_entrega = db.Column(db.DateTime, nullable=False)
    hora_entrega = db.Column(db.DateTime, nullable=False)
    rut_recibe = db.Column(db.String(250), nullable=False)
    esta_despacho = db.Column(db.String(1), nullable=False)
    venta_id = db.Column(db.Numeric(9999999), nullable=False)
    venta = db.relationship('Venta', backref=db.backref('Cliente', lazy='dynamic'))
    comuna_id = db.Column(db.Numeric(9999999), nullable=False)
    comuna = db.relationship('Comuna', backref=db.backref('Cliente', lazy='dynamic'))


    def serialize(self):
        return {
            "id": self.id,
            "direccion": self.direccion,
            "fecha_entrega0": self.fecha_entrega,
            "hora_entrega": self.hora_entrega,
            "rut_recibe": self.rut_recibe,
            "esta_despacho" : self.esta_despacho,
            "venta_id" : self.venta_id,
            "venta" : self.venta,
            "comuna_id": self.comuna_id,
            "comuna": self.comuna,

        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()