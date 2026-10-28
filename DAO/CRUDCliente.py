from DAO.Conexion import Conexion

host = 'localhost'
user = 'userempresa'
password = 'V3ntana.13'
db = 'empresa'

# =========================
def mostrartipos():
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT id, nombre FROM TIPO"
        cursor = con.ejecuta_query(sql)

        return cursor.fetchall() if cursor else []

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()

# =========================
def agregar(c):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """
        INSERT INTO CLIENTE 
        (run, nombre, apellido, direccion, fono, correo, montoCredito, deuda, TIPO_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        valores = (
            c.run,
            c.nombre,
            c.apellido,
            c.direccion,
            c.fono,
            c.correo,
            c.montoCredito,
            c.deuda,
            c.tipo
        )

        con.ejecuta_query(sql, valores)
        con.commit()
        return True

    except Exception as e:
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# =========================
def editar(c):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """
        UPDATE CLIENTE SET 
            run=%s,
            nombre=%s,
            apellido=%s,
            direccion=%s,
            fono=%s,
            correo=%s,
            montoCredito=%s,
            deuda=%s,
            TIPO_id=%s
        WHERE USER_ID=%s
        """

        valores = (
            c.run,
            c.nombre,
            c.apellido,
            c.direccion,
            c.fono,
            c.correo,
            c.montoCredito,
            c.deuda,
            c.tipo,
            c.id
        )

        con.ejecuta_query(sql, valores)
        con.commit()

        return True

    except Exception:
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# =========================
def eliminar(id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "DELETE FROM CLIENTE WHERE USER_ID=%s"

        con.ejecuta_query(sql, (id,))
        con.commit()

        return True

    except Exception:
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# =========================
def mostrartodos():
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """
        SELECT 
            c.USER_ID,
            c.run,
            c.nombre,
            c.apellido,
            c.direccion,
            c.fono,
            c.correo,
            c.montoCredito,
            c.deuda,
            t.nombre
        FROM CLIENTE c
        INNER JOIN TIPO t ON c.TIPO_id = t.id
        """

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall()

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()


# =========================
def consultaparticular(id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT * FROM CLIENTE WHERE USER_ID=%s"
        cursor = con.ejecuta_query(sql, (id,))

        return cursor.fetchone()

    except Exception:
        return None

    finally:
        if con:
            con.desconectar()
            

# =========================
def consultaparcial(cant):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT * FROM CLIENTE LIMIT %s"
        cursor = con.ejecuta_query(sql, (cant,))

        return cursor.fetchall()

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()


