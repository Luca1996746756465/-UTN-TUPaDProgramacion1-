class Autor:
    def __init__(self, id_autor: int, nombre: str, nacionalidad: str):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self) -> str:
        return f"Autor [ID: {self.id_autor}] {self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro: int, titulo: str, anio_publicacion: int, autor: Autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  

    def __str__(self) -> str:
        return f"Libro [ID: {self.id_libro}] '{self.titulo}' ({self.anio_publicacion}) - Autor: {self.autor.nombre}"

import sqlite3

def inicializar_base_datos():
    """Crea la base de datos 'biblioteca.db' y las tablas 'autores' y 'libros'."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id) ON DELETE CASCADE
        )
    """)

    conexion.commit()
    conexion.close()


def registrar_autor(nombre: str, nacionalidad: str) -> int:
    """Inserta un autor en la base de datos y retorna su ID generado."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    
    cursor.execute(
        "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)", 
        (nombre, nacionalidad)
    )
    
    conexion.commit()
    autor_id = cursor.lastrowid
    conexion.close()
    return autor_id


def registrar_libro(titulo: str, anio: int, autor_id: int):
    """Inserta un libro vinculado a un autor existente."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    
    cursor.execute(
        "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)", 
        (titulo, anio, autor_id)
    )
    
    conexion.commit()
    conexion.close()


def listar_libros():
    """Realiza un SELECT con JOIN entre libros y autores para mostrarlos en consola."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    query = """
        SELECT libros.id, libros.titulo, libros.anio, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()

    print("\n" + "="*60)
    print("               LISTADO DE LIBROS REGISTRADOS")
    print("="*60)
    if not resultados:
        print("No hay libros registrados en el sistema.")
    else:
        for fila in resultados:
            id_l, titulo, anio, nombre_autor, nac_autor = fila
            print(f"ID Libro: {id_l} | Título: '{titulo}' ({anio}) | Autor: {nombre_autor} ({nac_autor})")
    print("="*60)


def listar_autores_simple() -> bool:
    """Función auxiliar para mostrar los autores disponibles y elegir a cuál asociar un libro."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
    autores = cursor.fetchall()
    conexion.close()

    print("\n--- AUTORES DISPONIBLES ---")
    if not autores:
        print("(No hay autores registrados)")
        return False
    
    for a in autores:
        print(f"ID Autor: {a[0]} | Nombre: {a[1]} ({a[2]})")
    print("-" * 30)
    return True


def actualizar_titulo_libro(id_libro: int, nuevo_titulo: str):
    """Actualiza el título de un libro existente mediante UPDATE."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    
    cursor.execute(
        "UPDATE libros SET titulo = ? WHERE id = ?", 
        (nuevo_titulo, id_libro)
    )
    
    conexion.commit()
    conexion.close()


def eliminar_libro(id_libro: int):
    """Elimina un libro de la base de datos por su ID mediante DELETE."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    
    conexion.commit()
    conexion.close()

def menu_interactivo():

    inicializar_base_datos()

    while True:
        print("\n" + "="*45)
        print("     SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("="*45)
        print("1. Registrar un autor")
        print("2. Registrar un libro")
        print("3. Listar todos los libros")
        print("4. Actualizar título de un libro")
        print("5. Eliminar un libro")
        print("0. Salir")
        print("="*45)


        try:
            opcion = int(input("Seleccione una opción (0-5): ").strip())
        except ValueError:
            print(" Error: Debe ingresar obligatoriamente un número entero.")
            continue

        if opcion == 0:
            print("\nSaliendo del sistema de gestión. ¡Hasta luego!")
            break

        elif opcion == 1:
            print("\n--- REGISTRAR NUEVO AUTOR ---")
            nombre = input("Ingrese el nombre del autor: ").strip()
            while not nombre:
                print(" El campo no puede estar vacío.")
                nombre = input("Ingrese el nombre del autor: ").strip()

            nacionalidad = input("Ingrese la nacionalidad: ").strip()
            while not nacionalidad:
                print(" El campo no puede estar vacío.")
                nacionalidad = input("Ingrese la nacionalidad: ").strip()

            id_generado = registrar_autor(nombre, nacionalidad)
            print(f" ¡Autor registrado con éxito! ID asignado: {id_generado}")

        elif opcion == 2:
            print("\n--- REGISTRAR NUEVO LIBRO ---")
            hay_autores = listar_autores_simple()
            if not hay_autores:
                print(" Debe registrar al menos un autor antes de cargar un libro.")
                continue

            while True:
                try:
                    autor_id = int(input("Ingrese el ID del autor correspondiente: ").strip())
                    break
                except ValueError:
                    print(" Error: El ID del autor debe ser un número entero.")

            titulo = input("Ingrese el título del libro: ").strip()
            while not titulo:
                print(" El título no puede estar vacío.")
                titulo = input("Ingrese el título del libro: ").strip()

            while True:
                try:
                    anio = int(input("Ingrese el año de publicación: ").strip())
                    break
                except ValueError:
                    print(" Error: El año debe ser un número entero válido.")

            registrar_libro(titulo, anio, autor_id)
            print(" ¡Libro registrado con éxito!")

        elif opcion == 3:
            listar_libros()

        elif opcion == 4:
            print("\n--- ACTUALIZAR TÍTULO DE LIBRO ---")
            listar_libros()
            
            while True:
                try:
                    id_libro = int(input("\nIngrese el ID del libro que desea modificar: ").strip())
                    break
                except ValueError:
                    print(" Error: Ingrese un ID numérico válido.")

            nuevo_titulo = input("Ingrese el nuevo título: ").strip()
            while not nuevo_titulo:
                print(" El título no puede estar vacío.")
                nuevo_titulo = input("Ingrese el nuevo título: ").strip()

            actualizar_titulo_libro(id_libro, nuevo_titulo)
            print(" ¡Título actualizado correctamente!")

        elif opcion == 5:
            print("\n--- ELIMINAR LIBRO ---")
            listar_libros()
            
            while True:
                try:
                    id_libro = int(input("\nIngrese el ID del libro que desea eliminar: ").strip())
                    break
                except ValueError:
                    print(" Error: Ingrese un ID numérico válido.")

            eliminar_libro(id_libro)
            print(" ¡Libro eliminado correctamente!")

        else:
            print("s Opción inválida. Por favor, elija un número entre 0 y 5.")

if __name__ == "__main__":
    menu_interactivo()

# --- FUNCIONES ADICIONALES PARA LA API DE FLASK ---

def obtener_autores_db() -> list:
    """Retorna la lista de todos los autores en formato de diccionario para la API."""
    conexion = sqlite3.connect("biblioteca.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
    autores = [dict(row) for row in cursor.fetchall()]
    conexion.close()
    return autores

def obtener_autor_db(id_autor: int) -> dict:
    """Retorna un autor específico por su ID."""
    conexion = sqlite3.connect("biblioteca.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (id_autor,))
    row = cursor.fetchone()
    conexion.close()
    return dict(row) if row else None

def insertar_autor_db(nombre: str, nacionalidad: str) -> dict:
    """Inserta un autor y retorna el diccionario completo del autor creado."""
    id_generado = registrar_autor(nombre, nacionalidad)
    return obtener_autor_db(id_generado)

def obtener_libros_db() -> list:
    """Retorna todos los libros con la información detallada de su autor vía JOIN para la API."""
    conexion = sqlite3.connect("biblioteca.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    query = """
        SELECT libros.id, libros.titulo, libros.anio, 
               autores.id as autor_id, autores.nombre as autor_nombre, autores.nacionalidad as autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
    """
    cursor.execute(query)
    resultados = []
    for row in cursor.fetchall():
        resultados.append({
            "id": row["id"],
            "titulo": row["titulo"],
            "anio": row["anio"],
            "autor": {
                "id": row["autor_id"],
                "nombre": row["autor_nombre"],
                "nacionalidad": row["autor_nacionalidad"]
            }
        })
    conexion.close()
    return resultados

def obtener_libro_db(id_libro: int) -> dict:
    """Retorna un libro específico por su ID con su respectivo autor."""
    conexion = sqlite3.connect("biblioteca.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    query = """
        SELECT libros.id, libros.titulo, libros.anio, 
               autores.id as autor_id, autores.nombre as autor_nombre, autores.nacionalidad as autor_nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    """
    cursor.execute(query, (id_libro,))
    row = cursor.fetchone()
    conexion.close()
    if not row:
        return None
    return {
        "id": row["id"],
        "titulo": row["titulo"],
        "anio": row["anio"],
        "autor": {
            "id": row["autor_id"],
            "nombre": row["autor_nombre"],
            "nacionalidad": row["autor_nacionalidad"]
        }
    }

def insertar_libro_db(titulo: str, anio: int, autor_id: int) -> dict:
    """Inserta un libro y retorna su información completa con el autor."""
    registrar_libro(titulo, anio, autor_id)
    # Buscamos el último ID insertado para retornarlo
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT MAX(id) FROM libros")
    ultimo_id = cursor.fetchone()[0]
    conexion.close()
    return obtener_libro_db(ultimo_id)

def actualizar_libro_db(id_libro: int, titulo: str, anio: int, autor_id: int) -> dict:
    """Actualiza un libro completo (título, año y autor) para la API."""
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?",
        (titulo, anio, autor_id, id_libro)
    )
    conexion.commit()
    conexion.close()
    return obtener_libro_db(id_libro)

def eliminar_libro_db(id_libro: int):
    """Elimina un libro por su ID."""
    eliminar_libro(id_libro)