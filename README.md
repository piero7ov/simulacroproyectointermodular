---

````markdown
# 🏋️‍♂️ Tienda Deportiva Online — Simulacro Proyecto Intermodular

Proyecto desarrollado con **Flask** y **SQLite3** que simula el **frontend dinámico** de una tienda deportiva online.  
Muestra productos cargados desde una base de datos y los presenta en una interfaz moderna con HTML y CSS integrados.

Repositorio oficial: [https://github.com/piero7ov/simulacroproyectointermodular](https://github.com/piero7ov/simulacroproyectointermodular)

---

## 📋 Descripción del proyecto

El sistema genera automáticamente una página web que lista los productos almacenados en la base de datos `tiendadeportiva.db`.  
Cada producto se muestra con su imagen, nombre, descripción, precio y un botón de compra.

La aplicación está construida sobre el microframework **Flask** y utiliza **SQLite3** como motor de base de datos local, lo que permite una configuración simple y ligera, ideal para simulaciones o pruebas académicas.

---

## 🧩 Características principales

- 💻 Interfaz HTML con diseño responsive y degradados en tonos **azul y naranja**.  
- 🗂️ Conexión a base de datos SQLite (`tiendadeportiva.db`).
- 🏷️ Listado automático de productos desde la tabla `productos`.
- 🛒 Visualización de productos con nombre, descripción, precio e imagen.
- 📱 Diseño adaptable y con estilos CSS embebidos.
- ⚙️ Servidor Flask ejecutable en modo depuración.
- 📄 Código documentado con docstring completo para comprensión académica.

---

## 🗃️ Estructura esperada de la base de datos

El proyecto requiere una base de datos llamada `tiendadeportiva.db` con una tabla `productos` estructurada de la siguiente manera:

| Campo       | Tipo    | Descripción                                   |
|--------------|---------|-----------------------------------------------|
| id           | INTEGER | Clave primaria (autoincremental)              |
| nombre       | TEXT    | Nombre del producto                           |
| descripcion  | TEXT    | Descripción breve del producto                |
| imagen       | TEXT    | Ruta o URL de la imagen del producto          |
| precio       | REAL    | Precio del producto en euros (€)              |

Ejemplo de creación de la tabla:

```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    descripcion TEXT,
    imagen TEXT,
    precio REAL
);
````

---

## 🚀 Ejecución del proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/piero7ov/simulacroproyectointermodular.git
cd simulacroproyectointermodular
```

### 2️⃣ Instalar dependencias

Asegúrate de tener **Flask** instalado:

```bash
pip install flask
```

### 3️⃣ Ejecutar la aplicación

Ejecuta el archivo principal (por ejemplo, `app.py` o `tienda_deportiva.py`):

```bash
python tienda_deportiva.py
```

### 4️⃣ Abrir en el navegador

La aplicación estará disponible en:

```
http://127.0.0.1:5000/
```

---

## 🧠 Estructura del repositorio

```
simulacroproyectointermodular/
│
├── tienda_deportiva.py        # Script principal de la aplicación Flask
├── tiendadeportiva.db         # Base de datos SQLite (debe existir en la raíz)
├── README.md                  # Archivo de documentación (este archivo)
└── /static / templates         # (Opcional) Carpetas para expansión futura
```

---

## 🧑‍💻 Autor

**Piero Olivares Velasquez**
Desarrollador en formación — Proyecto académico intermodular
📍 Perú
💬 [GitHub: @piero7ov](https://github.com/piero7ov)

---

## 📅 Año

2025

---

## ⚠️ Notas importantes

* El contenido HTML y CSS está embebido directamente en el script para simplificar la ejecución sin archivos adicionales.
* La línea `basededatos.close()` debería colocarse **antes del `return cadena`**, ya que actualmente no se ejecuta.
* Ideal para prácticas de desarrollo web con **Flask**, **bases de datos locales** y **generación dinámica de HTML**.

---

## 🧭 Próximos pasos (sugerencias de mejora)

* Separar el HTML y CSS en carpetas `/templates` y `/static`.
* Implementar un carrito de compras funcional.
* Añadir rutas adicionales: detalles de producto, contacto, ofertas, etc.
* Agregar validaciones y manejo de errores con Flask.
* Mejorar el diseño con un framework frontend (Bootstrap o TailwindCSS).

---

✨ *Proyecto educativo diseñado para mostrar la integración entre Flask, SQLite y HTML dinámico.*

