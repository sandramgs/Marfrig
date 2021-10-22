import sqlite3

from sqlite3 import Error

def conectar_db():
    try:
        conn = sqlite3.connect('db/datos.db')
        return conn
    except Error as err:
        print(err)
        return None

def ejecutar_sentencia(_sql, lista_parametros):
    try:
        conn = conectar_db()
        if conn:
            objeto_cursor = conn.cursor()
            filas = objeto_cursor.execute(_sql, lista_parametros).rowcount
            objeto_cursor.close()
            conn.commit()
            conn.close()

            return filas
        else:
            print("No se pudo establecer la conexión a la base de datos. Ver errores.")
            return -1
    except Error as err:
        print("Error al ejecutar sentencia SQL: " + str(err))
        return -1


def ejecutar_consulta(_sql, lista_parametros):
    try:
        conn = conectar_db()
        if conn:
            conn.row_factory = fabrica_diccionarios 

            objeto_cursor = conn.cursor()

            if lista_parametros:
                objeto_cursor.execute(_sql, lista_parametros)
            else:
                objeto_cursor.execute(_sql)
            
            filas = objeto_cursor.fetchall()
            objeto_cursor.close()
            conn.close()

            return filas
        else:
            print("No se pudo establecer conexión con la base de datos. Ver errores.")
            return None
    except Error as err:
        print("Error al ejecutar consulta: " + str(err))
        return None


def fabrica_diccionarios(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    
    return d