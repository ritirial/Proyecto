from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from grocery.repository.currency_client import get_currency
from grocery.model.grocery_item import ItemBuilder
from grocery.repository.grocery_repository import SqlAlchemyRepository


groceries_blueprint = Blueprint('groceries_blueprint', __name__)

#repository contiene todo el manejo de querys en la BD
repository = SqlAlchemyRepository()


#Rutas que la aplicación usa

#Redirigir a /item
#GET http://localhost:3000/
@groceries_blueprint.route('/')
def root():
    return redirect(url_for('groceries_blueprint.items'))


#Reinciar BD y redirigir a /item
#GET http://localhost:3000/reset
@groceries_blueprint.route('/reset')
def reset():
    repository.reset_database()
    return redirect(url_for('groceries_blueprint.items'))


#Mostrar un elemento de la lista de acuerdo a su SKU, y convirtiendo el valor de Price
#GET http://localhost:3000/item

#Agregar un nuevo dato a la BD 
#POST http://localhost:3000/item
@groceries_blueprint.route('/item', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        try:
            items = repository.get()
            return render_template('index.html', items=items)
        except Exception as e:
            print(f"Repository error {e}")
            return f"Error retrieving grocery list"
    elif request.method == 'POST': 
        sku = request.form.get('sku')
        name = request.form.get('name')
        desc = request.form.get('description')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        exp_date = request.form.get('expdate')
        
        new_item = ItemBuilder().with_sku(sku).with_name(name).with_description(desc).with_quantity(quantity).with_price(price).with_exp_date(exp_date).build()
        repository.add(new_item)
        #recarga la vista llamando al metodo GET
        return redirect(url_for('groceries_blueprint.items'))


#Eliminar un dato en la BD de acuerdo a su SKU
#DELETE http://localhost:3000/item/{SKU}
@groceries_blueprint.route('/item/<sku>', methods=['DELETE'])
def remove_item(sku):
    repository.delete(sku)
    return jsonify({'message': 'Item removed successfully'}), 200


#Mostrar un elemento de la lista de acuerdo a su SKU, y convirtiendo el valor de Price
#GET http://localhost:3000/item/{SKU}/convert?currency={currency_key}
@groceries_blueprint.route('/item/<sku>/convert')
def get_converted(sku):
    try:
        currency_key = request.args.get('currency')
        item = repository.get_item(sku)
        print(item.__dict__)
        #
        conversion = item.Price * get_currency(currency_key)
        converted = {
            'SKU': item.SKU,
            'Name': item.Name,
            'Description': item.Description,
            'Quantity': item.Quantity,
            'Price_original': item.Price,
            'Price_converted': conversion,
            'Currency': currency_key,
            'Expiration_date': item.Expiration_date
        }
        return render_template('item.html', item=converted)
    except Exception as e:
        print(f"Repository error: {e}")
        return f"sku={sku} not found"
