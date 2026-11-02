from flask import Flask, jsonify, request
from SqlPrograma import (
    obtener_autores_db, obtener_autor_db, insertar_autor_db,
    obtener_libros_db, obtener_libro_db, insertar_libro_db,
    actualizar_libro_db, eliminar_libro_db
)

app = Flask(__name__)

# ==========================================
# ENDPOINTS DE AUTORES
# ==========================================
@app.route('/api/autores', methods=['GET'])
def listar_autores():
    autores = obtener_autores_db()
    return jsonify(autores), 200

@app.route('/api/autores', methods=['POST'])
def crear_autor():
    data = request.get_json()
    
    # Validación (Ejercicio 3: 400 Bad Request)
    if not data or not data.get('nombre') or not data.get('nacionalidad'):
        return jsonify({"error": "Faltan campos obligatorios: 'nombre' y/o 'nacionalidad'"}), 400

    nuevo_autor = insertar_autor_db(data['nombre'], data['nacionalidad'])
    return jsonify(nuevo_autor), 201


# ==========================================
# ENDPOINTS DE LIBROS
# ==========================================
@app.route('/api/libros', methods=['GET'])
def listar_libros():
    libros = obtener_libros_db()
    return jsonify(libros), 200

# CORREGIDO: Sintaxis correcta con <int:id_libro>
@app.route('/api/libros/<int:id_libro>', methods=['GET'])
def obtener_libro(id_libro):
    libro = obtener_libro_db(id_libro)
    if not libro:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(libro), 200

@app.route('/api/libros', methods=['POST'])
def crear_libro():
    data = request.get_json()
    
    # Validación (Ejercicio 3: 400 Bad Request)
    if not data or not data.get('titulo') or not data.get('anio') or not data.get('autor_id'):
        return jsonify({"error": "Faltan campos obligatorios: 'titulo', 'anio', 'autor_id'"}), 400

    # Verificar si el autor existe antes de asociarlo
    if not obtener_autor_db(data['autor_id']):
        return jsonify({"error": "El autor_id especificado no existe"}), 404

    nuevo_libro = insertar_libro_db(data['titulo'], data['anio'], data['autor_id'])
    return jsonify(nuevo_libro), 201

# CORREGIDO: Sintaxis correcta con <int:id_libro>
@app.route('/api/libros/<int:id_libro>', methods=['PUT'])
def actualizar_libro(id_libro):
    # Verificar si el libro existe (404 Not Found)
    libro_existente = obtener_libro_db(id_libro)
    if not libro_existente:
        return jsonify({"error": "Libro no encontrado"}), 404

    data = request.get_json()
    if not data or not data.get('titulo') or not data.get('anio') or not data.get('autor_id'):
        return jsonify({"error": "Faltan campos obligatorios para actualizar"}), 400

    libro_actualizado = actualizar_libro_db(id_libro, data['titulo'], data['anio'], data['autor_id'])
    return jsonify(libro_actualizado), 200

# CORREGIDO: Sintaxis correcta con <int:id_libro>
@app.route('/api/libros/<int:id_libro>', methods=['DELETE'])
def eliminar_libro(id_libro):
    libro_existente = obtener_libro_db(id_libro)
    if not libro_existente:
        return jsonify({"error": "Libro no encontrado"}), 404

    eliminar_libro_db(id_libro)
    return jsonify({"mensaje": f"Libro con ID {id_libro} eliminado correctamente"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)