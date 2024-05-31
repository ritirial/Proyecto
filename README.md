# TC3049 - Diseño y Arquitectura de Software | Proyecto Final

Proyecto final aplicando los conocimientos:

- Layer Architecture
- Unit testing
- Principios SOLID
- Design Patterns


## Configuración

### Montar un ambiente virtual

    py -m venv venv


### Entrar al ambiente virtual

Instrucciones para sistemas Unix:

    source venv/bin/activate

Instrucciones para sistemas Windows:

    venv/Scripts/activate


### Instalar dependencias

Mientrar el ambiente virtual este activo, ejecuta:

    pip install -r requirements.txt

Instala el contenido de src para utilizar en pruebas unitarias:

    pip install -e src


## Ejecución

Desde el directorio raíz, ejecuta:

    py src/main.py


## Contenido

### API

Se implementaron los siguientes endpoints en la aplicación

Recibir la lista de datos en la BD.

    GET /item

Agregar un nuevo dato a la BD.

    POST /item

Eliminar un dato en la BD de acuerdo a su SKU.

    DELETE /item/{SKU}

Mostrar un elemento de la lista de acuerdo a su SKU, y convirtiendo el valor de Price.

    GET /item/{SKU}/convert?currency={currency_key}

Reiniciar los datos de la BD con el archivo .CSV inicial.

    GET /reset


### Unit Testing

Desde el directorio raíz, ejecuta:

    pytest

Las pruebas unitarias implementadas son:

1. <b>test_csv.py</b>: Realiza una prueba de lectura del archivo csv y comprueba que se genera una lista no vacía. 
2. <b>test_currency.py</b>: Realiza una prueba de conexión con la API de conversión de monedas, validando que se recibe un numero mayor a 0.
3. <b>test_item_add.py</b>: Realiza una prueba de la función add() del repositorio.
4. <b>test_item_remove.py</b>: Realiza una prueba de la función delete() del repositorio.
5. <b>test_get_list_route.py</b>: Comprueba que la ruta GET '/item' utiliza el archivo template correcto.


## Layer Architecture

La aplicación Grocery Listy Application fue desarrollada siguiendo una arquitectura por capas, la cual indica que un proyecto puede ser dividido en capas como la capa de presentación, la capa de lógica de negocios y la capa de acceso a los datos.

- La capa de Presentación viene definida por el directorio "template", el cual contiene los archivos html que otorgan interactividad y visualización de contenido al usuario.
- La capa de Lógica de Negocios está compuesta por el directorio "handler", el cual contiene las rutas de la API y el manejo de los módulos externos como la API de conversión de moneda.
- La capa de Acceso a los Datos está formada por el directorio "repository", y contiene las funciones respectivas al manejo de querys para acceder a la información, que en este proyecto se conecta a una Base de Datos Postgres en el dispositivo local."


## SOLID

Los principios SOLID identificados en el proyecto son:

- <b> Single Resposibility Principle </b>: Este principio se encuentra presente en la especificación de los métodos que componen a las clases repository, ya que estos solo conocerán funciones como la consulta, creación y eliminación de datos, pero no tendrán conocimiento de funciones como la conversión de moneda, puesto que estas no afectan al almacenamiento de datos.

- <b> Open Closed Principle </b>: Este principio está presente separar la funcionalidad de consulta de monedas del resto de rutas mediante un archivo currency_client.py, ya que la dependencia de una API diferente y los processos de parseo de la respuesta HTTP recibida por dicha API no son relevantes para las rutas que requieran hacer uso de dicha función. Ests solo necesitan conocer el resultado de la conversión.

- <b> Dependency Inversion Principle </b>: Este principo está presente en la defnidión de la clase abstracta AbstractRepository del archivo grocery_repository.py, a la cual la clase SqlAlchemyRepository le hace herencia y, permitirá que cualquier ruta que requiera las funciones de AbstractRepository pueda acceder a ellas desde una instancia de SqlAlchemyRepository.


## Design Patterns

Los patrones de diseño implementados consisten en:

1. Creational Builder Pattern: En el archivo grocery_item.py, se utiliza este patrón de diseño debido a la cantidad de atributos de la clase Item, por lo que se cumple el objetivo de reducir el error al generar instancias de esta clase.
2. 
3. 
4. 
5. 

## Preguntas

1. ¿Cuales son el top 5 de caracteristicas de arquitectura del diseño actual de tu proyecto?.

    - <b>Maintainability</b>: Debido a su separación de funcionalidades, es posible agregar nuevas funcionalidades sin causar cambios que puedan romper el resto de funciones del proyecto.
    - <b>Usability</b>: Debido a la implementación de la interfaz grafica con formularios y botones, se simplifica el uso de la lógica de negocio del proyecto para los clientes finales.
    - <b>Configurability</b>: Debido a la separación de credenciales y archivos criticos, se apoya al proceso de modificación de ajustes del proyecto si se llegara a requerir.
    - <b>Supportability</b>: La logica de negocio implementa captura de errores durante la ejecución de las rutas con la finalidad apoyar el proceso de solución de errores.
    - <b>Accessibility</b>: El uso de etiquetas html y attributos de apoyo en los archivos templates permite ayudar a herramientas como los lectores de pantalla para ofrecer apoyo a clientes con necesidades especiales. 

2. ¿Si la aplicacion migrara a una arquitectura de microservicios, ¿Cuales serian el top 5 de caracteristicas de arquitectura?

R:

## Otros medios

Enlace del video: <a>video</a>