from flask import Flask

app = Flask(__name__)


@app.route('/score/<brand>')
def get_nota(brand):
    # Conect to tabla-notas-mb
    # Extract and transform data
    # Return data transformed
    return f'Notas de {brand}: (Cat1:7, Cat2:3, Cat3:9)'


@app.route('/product')
def guess_proveedor(white_label):
    """
    Devuelve el proveedor mas posible de un producto marca blanca
    """
    # Look for the product in openfoodfacts
    # Extract and transform data
    # Guess the supplier based on labels
    # Connect to ddbb, extract and transform the data
    return 'Los proveedores mas posibles son: (Proveedor1: infoProveedor1)...'


@app.route('/emb/<emb>')
def get_by_emb(emb):
    # Check if emb is in tabla proveedores
    # if it is a white mark, then get scores
    return f'El producto con emb: {emb} pertenece a XXX marca'


@app.route('/add/<producto>')
def add_supplier(producto, info):
    """
    Aniade un producto a la tabla de proveedores
    """
    return 'Producto aniadido'
