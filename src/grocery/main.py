import os
from flask import Flask
from grocery.handler.grocery_handler import groceries_blueprint


app = Flask(__name__)


print("Application startup")
port = 3000

try: 
    port = int(os.environ['PORT'])    
except KeyError:  
    print(f"Setting default port={port}")


app = Flask(__name__)
app.register_blueprint(groceries_blueprint)


if __name__ == '__main__':
    #main('sample_grocery.csv')
    app.run(host="0.0.0.0", debug=True, port=port)
