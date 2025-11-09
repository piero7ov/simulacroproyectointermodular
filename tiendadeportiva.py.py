
"""
Script Flask para mostrar un catálogo de productos desde una base de datos SQLite.

Este programa crea una aplicación web con Flask que se conecta a una base de datos
local llamada `tiendadeportiva.db`, obtiene la lista de productos almacenados en la 
tabla `productos` y genera dinámicamente una página HTML con estilo integrado (CSS inline)
que simula la interfaz principal de una tienda deportiva online.

Estructura general:
-------------------
1. Conexión a la base de datos SQLite usando `sqlite3`.
2. Ejecución de una consulta SQL para obtener todos los productos.
3. Generación dinámica del HTML mediante una cadena que incluye:
   - Cabecera con logotipo, menú de navegación y barra de búsqueda.
   - Sección principal con tarjetas de productos, mostrando:
       • Imagen del producto (ruta almacenada en la base de datos)
       • Nombre del producto
       • Descripción
       • Precio
       • Botón “Añadir al carrito”
   - Pie de página con enlaces secundarios (privacidad, términos y ayuda).
4. Cierre de la conexión a la base de datos.
5. Ejecución del servidor Flask en modo de depuración.

Requisitos:
-----------
- Flask instalado (`pip install flask`)
- Base de datos SQLite llamada `tiendadeportiva.db` con una tabla `productos`
  estructurada al menos con las siguientes columnas:
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    descripcion TEXT,
    imagen TEXT (ruta o URL de la imagen),
    precio REAL

Ruta principal:
---------------
    '/' → Renderiza el listado de productos en formato HTML.

Autor:
-------
Piero Olivares Velasquez

Año:
-----
2025

Ejemplo de ejecución:
---------------------
    $ python tienda_deportiva.py

    * Running on http://127.0.0.1:5000/
    * Debug mode: on

Notas:
------
- El código está diseñado para ejecutarse en un entorno local con base de datos SQLite.
- Todo el contenido HTML y CSS está embebido dentro del script para facilitar la visualización rápida.
- La conexión a la base de datos debería cerrarse tras la consulta, aunque la línea `basededatos.close()` 
  se encuentra después del `return`, por lo que no se ejecuta. Es recomendable moverla antes del `return`.
"""

import sqlite3              # Importa el módulo sqlite3 para manejar la base de datos SQLite
from flask import Flask     # Importa Flask para crear la aplicación web
app = Flask(__name__)       # Crea una instancia de la aplicación Flask

@app.route('/')             # Define la ruta principal de la aplicación
def listar_productos():     # Función para listar productos
    basededatos = sqlite3.connect('tiendadeportiva.db')         # Conecta a la base de datos SQLite llamada 'tiendadeportiva.db'
    cursor = basededatos.cursor()                               # Crea un cursor para ejecutar consultas SQL
    # Construye la cadena HTML para la página web
    cadena = '''                                                
    <!-- Maqueta visual del front de una tienda online deportiva -->
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tienda Deportiva Online</title>
        <style>
            /* Hace que el footer se mantenga al fondo de la página */
            html, body {
                height: 100%;
            }

            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #3857ad, #4bbaee);
                display: flex;
                flex-direction: column;
            }

            main {
                flex: 1;
            }

            header {
                background: linear-gradient(135deg, #0ea5e9, #f97316);
                color: #fff;
                padding: 10px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .logo h1 {
                margin: 0 20px;
            }

            nav ul {
                list-style: none;
                margin: 0;
                padding: 0;
                display: flex;
            }

            nav ul li {
                display: flex;
                margin: 0 15px;
            }

            nav ul li a {
                color: #fff;
                text-decoration: none;
            }

            .search-cart {
                margin-right: 20px;
            }

            .search-cart input[type="text"] {
                padding: 5px;
            }

            .product-list {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                padding: 20px;
            }

            .product-item {
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 10px;
                margin: 15px;
                padding: 15px;
                width: 250px;
                text-align: center;
            }

            .product-item img {
                max-width: 100%;
                height: auto;
            }

            .price {
                color: green;
                font-weight: bold;
            }

            footer {
                background: linear-gradient(135deg, #0ea5e9, #f97316);
                color: #fff;
                text-align: center;
                padding: 10px 0;
                margin-top: 20px;
            }

            footer nav ul {
                display: flex;
                justify-content: center;
                list-style: none;
                padding: 0;
                margin: 10px 0 0 0;
            }

            footer nav ul li {
                margin: 0 10px;
            }

            footer nav ul li a {
                color: #fff;
                text-decoration: none;
            }

        </style>
    </head>
    <body>
        <header>
            <div class="logo">
                <h1>Tienda Deportiva</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="#">Inicio</a></li>
                    <li><a href="#">Productos</a></li>
                    <li><a href="#">Ofertas</a></li>
                    <li><a href="#">Contacto</a></li>
                </ul>
            </nav>
            <div class="search-cart">
                <input type="text" placeholder="Buscar productos...">
                <button>Buscar</button>
                <a href="#" class="cart-icon">Carrito (0)</a>
            </div>
        </header>

        <main>
            <section class="product-list">
   '''      #   fin cadena inicial
    ########## ahora listado de productos ########################################

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    for producto in productos:
        cadena+='''
            <div class="product-item">
                <img src="''' + producto[3] + '''" alt="''' + producto[1] + '''">
                <h2>''' + producto[1] + '''</h2>
                <p>''' + producto[2] + '''</p>
                <span class="price">''' + str(producto[4]) + '''€</span>
                <button>Añadir al carrito</button>
            </div>
    '''
    ########## fin de listado de productos ########################################
    cadena+= '''
        </section>
        </main>

        <footer>
            <p>&copy; 2024 Tienda Deportiva by Piero Olivares Velasquez</p>
            <nav>
                <ul>
                    <li><a href="#">Política de Privacidad</a></li>
                    <li><a href="#">Términos y Condiciones</a></li>
                    <li><a href="#">Ayuda</a></li>
                </ul>
            </nav>
        </footer>
    </body>
    </html>
    '''  # fin cadena final 
    return cadena               # Devuelve la cadena HTML completa como respuesta
    basededatos.close()         # Cierra la conexión a la base de datos
if __name__ == '__main__':      #   Ejecuta la aplicación Flask si este archivo es el programa principal
    app.run(debug=True)         #   Inicia el servidor Flask en modo de depuración  