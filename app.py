# 0. ejecutamos pip install flask flask-sqlalchemy flask-migrate flask-cors
# 1. importamos la libreria flask
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Cliente, Venta, Descuento, Producto, Descuento_Producto, Suscripcion, Detalle, Donacion, Comuna, Region, Vendedor, Despacho
from flask_cors import CORS, cross_origin

# 2 Aplicacion Creada
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False
app.config['DEBUG'] = False
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

# 3. Creamos una ruta para validar nuestra app
@app.route('/')
def index():
    return 'Hola mundo'

# Creamos nuestras funciones

#Funciones Cliente
    # Consultar todos los clientes
@app.route('/Cliente', methods=['GET'])
@cross_origin()
def getClientes():
    cliente = Cliente.query.all()
    cliente = list(map(lambda x: x.serialize(), cliente))
    return jsonify(cliente),200

    # consulta solo un Clientes según su id y me devuelve 1
@app.route('/Cliente/<id>', methods=['GET'])
def getCliente(id):
    cliente = Cliente.query.get('id')
    return jsonify(cliente.serialize()),200

    # borrar Cliente segun id
@app.route('/Cliente/<id>', methods=['DELETE'])
def deleteCliente(id):
    cliente = Cliente.query.get('id')
    cliente.delete(cliente)
    return jsonify(cliente.serialize()),200

    # modificar Cliente
@app.route('/Cliente/<id>', methods=['PUT'])
def updateCliente(id):
    cliente = Cliente.query.get('id')

    rut = request.json.get('rut')
    porcentaje = request.json.get('porcentaje')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    fono = request.json.get('fono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')
    comuna_id = request.json.get('comuna_id')

    cliente.rut = rut
    cliente.porcentaje = porcentaje
    cliente.primer_nombre = primer_nombre
    cliente.segundo_nombre = segundo_nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.direccion = direccion
    cliente.fono = fono
    cliente.correo = correo
    cliente.estado = estado
    cliente.comuna_id = comuna_id

    Cliente.save(cliente)

    return jsonify(cliente.serialize()),200

    # agregar Cliente
    # Session = scoped_session(sessionmaker(bind=engine))
@app.route('/Clientes', methods=['POST'])
def addCliente():
    cliente = Cliente()
    rut = request.json.get('rut')
    porcentaje = request.json.get('porcentaje')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    fono = request.json.get('fono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')
    comuna_id = request.json.get('comuna_id')

    cliente.rut = rut
    cliente.porcentaje = porcentaje
    cliente.primer_nombre = primer_nombre
    cliente.segundo_nombre = segundo_nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.direccion = direccion
    cliente.fono = fono
    cliente.correo = correo
    cliente.estado = estado
    cliente.comuna_id = comuna_id
    
    Cliente.save(cliente)

    return jsonify(cliente.serialize()),200

#Funciones Venta
    # Consultar todas las ventas
@app.route('/Ventas', methods=['GET'])
@cross_origin()
def getVentas():
    venta = Venta.query.all()
    venta = list(map(lambda x: x.serialize(), venta))
    return jsonify(venta),200

# consulta solo un Venta según su id y me devuelve 1
@app.route('/Venta/<id>', methods=['GET'])
def getVenta(id):
    venta = Venta.query.get('id')
    return jsonify(venta.serialize()),200

# borrar Venta segun id
@app.route('/Venta/<id>', methods=['DELETE'])
def deleteVenta(id):
    venta = Venta.query.get('id')
    venta.delete(Venta)
    return jsonify(Venta.serialize()),200

# modificar Venta
@app.route('/venta/<id>', methods=['PUT'])
def updateVenta(id):
    venta = Venta.query.get('id')

    id_venta = request.json.get('id_venta')
    fecha = request.json.get('fecha')
    descuento = request.json.get('descuento')
    subtotal = request.json.get('subtotal')
    iva = request.json.get('iva')
    total = request.json.get('total')
    estado = request.json.get('estado')
    cliente_id = request.json.get('cliente_id')
    vendedor_id = request.json.get('vendedor_id')
    despacho = request.json.get('despacho')

    venta.id_venta = id_venta
    venta.fecha = fecha
    venta.descuento = descuento
    venta.subtotal = subtotal
    venta.iva = iva
    venta.total = total
    venta.estado = estado
    venta.cliente_id = cliente_id
    venta.vendedor_id = vendedor_id
    venta.despacho = despacho
    
    Venta.save(venta)

    return jsonify(venta.serialize()),200

# agregar venta
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/Ventas', methods=['POST'])
def addVenta():
    venta = Venta()

    id_venta = request.json.get('id_venta')
    fecha = request.json.get('fecha')
    descuento = request.json.get('descuento')
    subtotal = request.json.get('subtotal')
    iva = request.json.get('iva')
    total = request.json.get('total')
    estado = request.json.get('estado')
    cliente_id = request.json.get('cliente_id')
    vendedor_id = request.json.get('vendedor_id')
    despacho = request.json.get('despacho')

    venta.id_venta = id_venta
    venta.fecha = fecha
    venta.descuento = descuento
    venta.subtotal = subtotal
    venta.iva = iva
    venta.total = total
    venta.estado = estado
    venta.cliente_id = cliente_id
    venta.vendedor_id = vendedor_id
    venta.despacho = despacho
    
    Venta.save(venta)

    return jsonify(venta.serialize()),200

#Funciones Descuento
    # Consultar todos los Descuentos
@app.route('/Descuento', methods=['GET'])
@cross_origin()
def getDescuentos():
    descuento = Descuento.query.all()
    descuento = list(map(lambda x: x.serialize(), descuento))
    return jsonify(descuento),200

# consulta solo un Descuento según su id y me devuelve 1
@app.route('/Descuento/<id>', methods=['GET'])
def getDescuento(id):
    descuento = Descuento.query.get('id')
    return jsonify(descuento.serialize()),200

# borrar Descuento segun id
@app.route('/Descuento/<id>', methods=['DELETE'])
def deleteDescuento(id):
    descuento = Descuento.query.get('id')
    Descuento.delete(descuento)
    return jsonify(descuento.serialize()),200

# modificar Descuento
@app.route('/Descuento/<id>', methods=['PUT'])
def updateDescuento(id):
    descuento = Descuento.query.get('id')

    nombre = request.json.get('nombre')
    fecha = request.json.get('fecha')
    porcentaje = request.json.get('porcentaje')
    estado = request.json.get('estado')

    descuento.nombre = nombre
    descuento.fecha = fecha
    descuento.porcentaje = porcentaje
    descuento.estado = estado

    Descuento.save(descuento)

    return jsonify(descuento.serialize()),200

# agregar Descuentos
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/Descuento', methods=['POST'])
def addDescuento():
    descuento = Descuento()
    nombre = request.json.get('nombre')
    fecha = request.json.get('fecha')
    porcentaje = request.json.get('porcentaje')
    estado = request.json.get('estado')

    descuento.nombre = nombre
    descuento.fecha = fecha
    descuento.porcentaje = porcentaje
    descuento.estado = estado
    
    Descuento.save(descuento)

    return jsonify(descuento.serialize()),200

#Funciones Producto
    # Consultar todos los Productos
@app.route('/Producto', methods=['GET'])
@cross_origin()
def getProductos():
    producto = Producto.query.all()
    producto = list(map(lambda x: x.serialize(), producto))
    return jsonify(producto),200

# consulta solo un Clientes según su id y me devuelve 1
@app.route('/Producto/<id>', methods=['GET'])
def getProducto(id):
    producto = Producto.query.get('id')
    return jsonify(producto.serialize()),200

# borrar Producto segun id
@app.route('/Producto/<id>', methods=['DELETE'])
def deleteProducto(id):
    producto = Producto.query.get('id')
    Producto.delete(producto)
    return jsonify(producto.serialize()),200

# modificar Producto
@app.route('/Producto/<id>', methods=['PUT'])
def updateProducto(id):
    producto = Producto.query.get('id')

    codigo = request.json.get('codigo')
    nombre = request.json.get('nombre')
    valor_venta = request.json.get('valor_venta')
    stock = request.json.get('stock')
    descripcion = request.json.get('descripcion')
    imagen = request.json.get('imagen')
    estado = request.json.get('estado')

    producto.codigo = codigo
    producto.nombre = nombre
    producto.valor_venta = valor_venta
    producto.stock = stock
    producto.descripcion = descripcion
    producto.imagen = imagen
    producto.estado = estado

    Producto.save(producto)

    return jsonify(producto.serialize()),200

# agregar Producto
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/Productos', methods=['POST'])
def addProductos():
    producto = Producto()
    codigo = request.json.get('codigo')
    nombre = request.json.get('nombre')
    valor_venta = request.json.get('valor_venta')
    stock = request.json.get('stock')
    descripcion = request.json.get('descripcion')
    imagen = request.json.get('imagen')
    estado = request.json.get('estado')

    producto.codigo = codigo
    producto.nombre = nombre
    producto.valor_venta = valor_venta
    producto.stock = stock
    producto.descripcion = descripcion
    producto.imagen = imagen
    producto.estado = estado
    
    Producto.save(producto)

    return jsonify(producto.serialize()),200

#Funciones Descuento_Producto
    # Consultar todos los clientes
@app.route('/Descuento_Producto', methods=['GET'])
@cross_origin()
def getDescuento_Productos():
    descuento_Producto = Descuento_Producto.query.all()
    descuento_Producto = list(map(lambda x: x.serialize(), descuento_Producto))
    return jsonify(descuento_Producto),200

# consulta solo un Descuento_Producto según su id y me devuelve 1
@app.route('/Descuento_Producto/<id>', methods=['GET'])
def getDescuento_Producto(id):
    descuento_Producto = Descuento_Producto.query.get('id')
    return jsonify(descuento_Producto.serialize()),200

# borrar Descuento_Producto segun id
@app.route('/Descuento_Producto/<id>', methods=['DELETE'])
def deleteDescuento_Producto(id):
    descuento_Producto = Descuento_Producto.query.get('id')
    Descuento_Producto.delete(descuento_Producto)
    return jsonify(descuento_Producto.serialize()),200

# modificar Descuento_Producto
@app.route('/Descuento_Producto/<id>', methods=['PUT'])
def updateDescuento_Producto(id):
    descuento_Producto = Descuento_Producto.query.get('id')

    producto_id = request.json.get('producto_id')
    descuento_id = request.json.get('descuento_id')
    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')

    descuento_Producto.producto_id = producto_id
    descuento_Producto.descuento_id = descuento_id
    descuento_Producto.fecha_inicio = fecha_inicio
    descuento_Producto.fecha_termino = fecha_termino

    Descuento_Producto.save(descuento_Producto)

    return jsonify(descuento_Producto.serialize()),200

# agregar Descuento_Producto
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/descuento_Productos', methods=['POST'])
def addDescuento_Producto():
    descuento_Producto = Descuento_Producto()
    producto_id = request.json.get('producto_id')
    descuento_id = request.json.get('descuento_id')
    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')

    descuento_Producto.producto_id = producto_id
    descuento_Producto.descuento_id = descuento_id
    descuento_Producto.fecha_inicio = fecha_inicio
    descuento_Producto.fecha_termino = fecha_termino
    
    Descuento_Producto.save(descuento_Producto)

    return jsonify(descuento_Producto.serialize()),200

#Funciones Suscripcion
    # Consultar todos las Suscripciones
@app.route('/Suscripcion', methods=['GET'])
@cross_origin()
def getSuscripciones():
    suscripcion = Suscripcion.query.all()
    suscripcion = list(map(lambda x: x.serialize(), suscripcion))
    return jsonify(suscripcion),200

# consulta solo un Suscripciones según su id y me devuelve 1
@app.route('/Suscripcion/<id>', methods=['GET'])
def getSuscripcion(id):
    suscripcion = Suscripcion.query.get('id')
    return jsonify(suscripcion.serialize()),200

# borrar Suscripcion segun id
@app.route('/Suscripcion/<id>', methods=['DELETE'])
def deleteSuscripcion(id):
    suscripcion = Suscripcion.query.get('id')
    Suscripcion.delete(suscripcion)
    return jsonify(suscripcion.serialize()),200

# modificar Suscripcion
@app.route('/Suscripcion/<id>', methods=['PUT'])
def updateSuscripcion(id):
    suscripcion = Suscripcion.query.get('id')

    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')
    cliente_id = request.json.get('cliente_id')

    suscripcion.fecha_inicio = fecha_inicio
    suscripcion.fecha_termino = fecha_termino
    suscripcion.cliente_id = cliente_id

    Suscripcion.save(suscripcion)

    return jsonify(suscripcion.serialize()),200

# agregar Suscripcion
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/suscripciones', methods=['POST'])
def addSuscripcion():
    suscripcion = Suscripcion()
    fecha_inicio = request.json.get('fecha_inicio')
    fecha_termino = request.json.get('fecha_termino')
    cliente_id = request.json.get('cliente_id')

    suscripcion.fecha_inicio = fecha_inicio
    suscripcion.fecha_termino = fecha_termino
    suscripcion.cliente_id = cliente_id
    
    Suscripcion.save(suscripcion)

    return jsonify(suscripcion.serialize()),200

#Funciones Detalle
    # Consultar todos los Detalles
@app.route('/Detalle', methods=['GET'])
@cross_origin()
def getDetalles():
    detalle = Detalle.query.all()
    detalle = list(map(lambda x: x.serialize(), detalle))
    return jsonify(detalle),200

# consulta solo un Detalles según su id y me devuelve 1
@app.route('/Detalle/<id>', methods=['GET'])
def getDetalle(id):
    detalle = Detalle.query.get('id')
    return jsonify(detalle.serialize()),200

# borrar Detalle segun id
@app.route('/Detalle/<id>', methods=['DELETE'])
def deleteDetalle(id):
    detalle = Detalle.query.get('id')
    Cliente.delete(detalle)
    return jsonify(detalle.serialize()),200

# agregar Detalle
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/detalles', methods=['POST'])
def addDetalle():
    detalle = Detalle()
    cantidad = request.json.get('cantidad')
    valor = request.json.get('valor')
    descuento = request.json.get('descuento')
    estado = request.json.get('estado')
    venta_id = request.json.get('venta_id')
    producto_id = request.json.get('producto_id')

    detalle.cantidad = cantidad
    detalle.valor = valor
    detalle.descuento = descuento
    detalle.estado = estado
    detalle.venta_id = venta_id
    detalle.producto_id = producto_id
    
    Detalle.save(detalle)

    return jsonify(detalle.serialize()),200

#Funciones Donacion
    # Consultar todas las Donaciones
@app.route('/Donacion', methods=['GET'])
@cross_origin()
def getDonaciones():
    donacion = Donacion.query.all()
    donacion = list(map(lambda x: x.serialize(), donacion))
    return jsonify(donacion),200

# consulta solo un Donaciones según su id y me devuelve 1
@app.route('/Donacion/<id>', methods=['GET'])
def getDonacion(id):
    donacion = Donacion.query.get('id')
    return jsonify(donacion.serialize()),200

# borrar Donacion segun id
@app.route('/Donacion/<id>', methods=['DELETE'])
def deleteDonacion(id):
    donacion = Donacion.query.get('id')
    Donacion.delete(donacion)
    return jsonify(donacion.serialize()),200

# modificar Donacion
@app.route('/Donacion/<id>', methods=['PUT'])
def updateDonacion(id):
    donacion = Donacion.query.get('id')

    valor = request.json.get('valor')
    fecha = request.json.get('fecha')
    cliente_id = request.json.get('cliente_id')

    donacion.valor = valor
    donacion.fecha = fecha
    donacion.cliente_id = cliente_id

    Donacion.save(donacion)

    return jsonify(donacion.serialize()),200

# agregar Donacion
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/donaciones', methods=['POST'])
def addDonacion():
    donacion = Donacion()
    valor = request.json.get('valor')
    fecha = request.json.get('fecha')
    cliente_id = request.json.get('cliente_id')

    donacion.valor = valor
    donacion.fecha = fecha
    donacion.cliente_id = cliente_id

    Donacion.save(donacion)

    return jsonify(donacion.serialize()),200

#Funciones Comuna
    # Consultar todas las Comunas
@app.route('/Comuna', methods=['GET'])
@cross_origin()
def getComunas():
    comuna = Comuna.query.all()
    comuna = list(map(lambda x: x.serialize(), comuna))
    return jsonify(comuna),200

# consulta solo un Comunas según su id y me devuelve 1
@app.route('/Comuna/<id>', methods=['GET'])
def getComuna(id):
    comuna = Comuna.query.get('id')
    return jsonify(comuna.serialize()),200

# borrar Comuna segun id
@app.route('/Comuna/<id>', methods=['DELETE'])
def deleteComuna(id):
    comuna = Comuna.query.get('id')
    Comuna.delete(comuna)
    return jsonify(comuna.serialize()),200

# modificarComuna
@app.route('/Comuna/<id>', methods=['PUT'])
def updateComuna(id):
    comuna = Comuna.query.get('id')

    nombre = request.json.get('nombre')
    fecha_inicio = request.json.get('fecha_inicio')

    comuna.nombre = nombre
    comuna.fecha_inicio = fecha_inicio

    Comuna.save(comuna)

    return jsonify(comuna.serialize()),200

# agregar Comuna
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/comunas', methods=['POST'])
def addComuna():
    comuna = Comuna()
    nombre = request.json.get('nombre')
    fecha_inicio= request.json.get('fecha_inicio')

    comuna.nombre = nombre
    comuna.fecha_inicio = fecha_inicio

    Comuna.save(comuna)

    return jsonify(comuna.serialize()),200

#Funciones Region
    # Consultar todas las Regiones
@app.route('/Region', methods=['GET'])
@cross_origin()
def getRegiones():
    region = Region.query.all()
    region = list(map(lambda x: x.serialize(), region))
    return jsonify(region),200

# consulta solo un Regiones según su id y me devuelve 1
@app.route('/Region/<id>', methods=['GET'])
def getRegion(id):
    region = Region.query.get('id')
    return jsonify(region.serialize()),200

# borrar Region segun id
@app.route('/Region/<id>', methods=['DELETE'])
def deleteRegion(id):
    region = Region.query.get('id')
    Region.delete(region)
    return jsonify(region.serialize()),200

# modificar Region
@app.route('/Region/<id>', methods=['PUT'])
def updateRegion(id):
    region = Region.query.get('id')

    nombre = request.json.get('nombre')

    region.nombre = nombre

    Region.save(region)

    return jsonify(region.serialize()),200

# agregar Region
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/regiones', methods=['POST'])
def addRegion():
    region = Region()
    nombre = request.json.get('nombre')

    region.nombre = nombre
    
    Region.save(region)

    return jsonify(region.serialize()),200

#Funciones Vendedor
    # Consultar todos los Vendedores
@app.route('/Vendedor', methods=['GET'])
@cross_origin()
def getVendedores():
    vendedor = Vendedor.query.all()
    vendedor = list(map(lambda x: x.serialize(), vendedor))
    return jsonify(vendedor),200

# consulta solo un Vendedores según su id y me devuelve 1
@app.route('/Vendedor/<id>', methods=['GET'])
def getVendedor(id):
    vendedor = Vendedor.query.get('id')
    return jsonify(vendedor.serialize()),200

# borrar Vendedor segun id
@app.route('/Vendedor/<id>', methods=['DELETE'])
def deleteVendedor(id):
    vendedor = Vendedor.query.get('id')
    Vendedor.delete(vendedor)
    return jsonify(vendedor.serialize()),200

# modificar Vendedor
@app.route('/Vendedor/<id>', methods=['PUT'])
def updateVendedor(id):
    vendedor = Vendedor.query.get('id')

    rut = request.json.get('rut')
    dv = request.json.get('dv')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    fono = request.json.get('fono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')
    comuna_id = request.json.get('comuna_id')

    vendedor.rut = rut
    vendedor.dv = dv
    vendedor.primer_nombre = primer_nombre
    vendedor.segundo_nombre = segundo_nombre
    vendedor.apellido_paterno = apellido_paterno
    vendedor.apellido_materno = apellido_materno
    vendedor.direccion = direccion
    vendedor.fono = fono
    vendedor.correo = correo
    vendedor.estado = estado
    vendedor.comuna_id = comuna_id

    Vendedor.save(vendedor)

    return jsonify(vendedor.serialize()),200

# agregar Vendedor
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/Vendedores', methods=['POST'])
def addVendedor():
    vendedor = Vendedor()
    rut = request.json.get('rut')
    dv = request.json.get('dv')
    primer_nombre = request.json.get('primer_nombre')
    segundo_nombre = request.json.get('segundo_nombre')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    direccion = request.json.get('direccion')
    fono = request.json.get('fono')
    correo = request.json.get('correo')
    estado = request.json.get('estado')
    comuna_id = request.json.get('comuna_id')

    vendedor.rut = rut
    vendedor.dv = dv
    vendedor.primer_nombre = primer_nombre
    vendedor.segundo_nombre = segundo_nombre
    vendedor.apellido_paterno = apellido_paterno
    vendedor.apellido_materno = apellido_materno
    vendedor.direccion = direccion
    vendedor.fono = fono
    vendedor.correo = correo
    vendedor.estado = estado
    vendedor.comuna_id = comuna_id
    
    Vendedor.save(vendedor)

    return jsonify(vendedor.serialize()),200

#Funciones Despacho
    # Consultar todos los Despachos
@app.route('/Despacho', methods=['GET'])
@cross_origin()
def getDespachos():
    despacho = Despacho.query.all()
    despacho = list(map(lambda x: x.serialize(), despacho))
    return jsonify(despacho),200

# consulta solo un Despachos según su id y me devuelve 1
@app.route('/Despacho/<id>', methods=['GET'])
def getDespacho(id):
    despacho = Despacho.query.get('id')
    return jsonify(despacho.serialize()),200

# borrar Despacho segun id
@app.route('/Despacho/<id>', methods=['DELETE'])
def deleteDespacho(id):
    despacho = Despacho.query.get('id')
    Despacho.delete(despacho)
    return jsonify(despacho.serialize()),200

# modificar Despacho
@app.route('/Despacho/<id>', methods=['PUT'])
def updateDespacho(id):
    despacho = Despacho.query.get('id')

    direccion = request.json.get('direccion')
    fecha_entrega = request.json.get('fecha_entrega')
    hora_entrega = request.json.get('hora_entrega')
    rut_recibe = request.json.get('rut_recibe')
    esta_despacho = request.json.get('direccion')
    venta_id = request.json.get('direccion')
    comuna_id = request.json.get('direccion')

    despacho.direccion = direccion
    despacho.fecha_entrega = fecha_entrega
    despacho.hora_entrega = hora_entrega
    despacho.rut_recibe = rut_recibe
    despacho.esta_despacho = esta_despacho
    despacho.venta_id = venta_id
    despacho.comuna_id = comuna_id

    Despacho.save(despacho)

    return jsonify(despacho.serialize()),200

# agregar Despacho
# Session = scoped_session(sessionmaker(bind=engine))
@app.route('/despachos', methods=['POST'])
def addDespacho():
    despacho = Despacho()
    direccion = request.json.get('direccion')
    fecha_entrega = request.json.get('fecha_entrega')
    hora_entrega = request.json.get('hora_entrega')
    rut_recibe = request.json.get('rut_recibe')
    esta_despacho = request.json.get('direccion')
    venta_id = request.json.get('direccion')
    comuna_id = request.json.get('direccion')

    despacho.direccion = direccion
    despacho.fecha_entrega = fecha_entrega
    despacho.hora_entrega = hora_entrega
    despacho.rut_recibe = rut_recibe
    despacho.esta_despacho = esta_despacho
    despacho.venta_id = venta_id
    despacho.comuna_id = comuna_id
    
    Despacho.save(despacho)

    return jsonify(despacho.serialize()),200


# 3. Creamos una ruta y debug=true para que el servidor se reinicie ante los cambios


# 4. añadimos un validador para saber si estamos ejecutando nuestra aplicacion

# 5. ejecutamos python app.py o python3 app.py

# 6. ejecutamos el comando flask db init

# 7. ejecutamos el comando flask db migrate

# 8. ejecutamos el comando flask db upgrade

# 9. ejecutamos el comando flask run --host=0.0.0.0 en caso que tengamos problemas con el cors
if __name__ == '__main__':
    app.run(port=3000, debug=True)