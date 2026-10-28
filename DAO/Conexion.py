import pymysql

class Conexion:
    def __init__(self, host, user, password, db):
        self.db = None
        self.cursor = None
        try:
            self.db = pymysql.connect(
                host=host,
                user=user,
                password=password,
                db=db
            )
            self.cursor = self.db.cursor()
        except Exception as e:
            print("Error de conexión:", e)

    # --------------------------------------------
    def ejecuta_query(self, sql, valores=None):
        try:
            if not self.db or not self.cursor:
                return None
            if valores is not None:
                self.cursor.execute(sql, valores)
            else:
                self.cursor.execute(sql)
            return self.cursor
        except Exception as e:
            print("Error en query:", e)
            return None

    # --------------------------------------------
    def desconectar(self): # Cierra la conexión con la base de datos.
        if self.db:
            self.db.close()
            self.db = None
            self.cursor = None

    def commit(self): # Confirma o guarda los cambios realizados en la base de datos.
        if self.db:
            self.db.commit()

    def rollback(self): # Revierte o deshace los cambios realizados desde el último commit().
        if self.db:
            self.db.rollback()

    # --------------------------------------------
    def obtenerUsuario(self, username):
        try:
            if not self.db or not self.cursor:
                return None
            sql = "SELECT * FROM usuarios WHERE username = %s"
            cursor = self.ejecuta_query(sql, (username,))
            if cursor:
                return cursor.fetchone()
            return None
        except Exception as e:
            print("Error al obtener usuario:", e)
            return None

    # --------------------------------------------
    def agregarUsuario(self, username, password_hash, nombre, apellido, email, tipo_usuario):
        try:
            sql = """INSERT INTO usuarios
            (username, password_hash, nombre, apellido, email, tipo_usuario)
            VALUES(%s, %s, %s, %s, %s, %s)"""

            valores = (username, password_hash, nombre, apellido, email, tipo_usuario)

            self.ejecuta_query(sql, valores)
            self.commit()
            return True
        except Exception as e:
            print("Error al obtener usuario:", e)
            self.rollback()
            return False