import os
import DAO.CRUDCliente
from DTO.Cliente import Cliente
from DTO.Usuario import Usuario
from getpass import getpass # Oculta la contraseña en el input

# ================= TIPOS =================
TIPOS = {
    1: "Cliente Normal",
    2: "VIP",
    3: "Empresa"
}

# === MENÚ USUARIOS ===
def menu_usuarios():
    os.system('cls')
    print("================================")
    print("         MENÚ USUARIOS          ")
    print("================================")
    print("1. INICIAR SESIÓN")
    print("2. REGISTRAR USUARIO")
    print("3. SALIR")
    print("================================")

# ============== LOGIN ==============
def ingresoUsuarios():
    os.system('cls')

    username = input("Usuario: ")

    while True:
        pass1 = getpass("Password: ")
        pass2 = getpass("Repetir: ")
        if pass1 == pass2:
            break

    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    correo = input("Correo: ")

    print("1.- Administrador")
    print("2.- Vendedor")

    tipo = input("Tipo: ")
    tipo = "Administrador" if tipo == "1" else "Vendedor"

    Usuario.registrar_usuario(username, pass1, nombre, apellidos, correo, tipo)

    print("\nUsuario registrado")
    input("\nPresione ENTER para continuar...")

# ================= MENÚ =================
def menuprincipal():
    os.system('cls')
    print("================================")
    print("       MENÚ PRINCIPAL          ")
    print("================================")
    print("1. (C) INGRESAR CLIENTE")
    print("2. (R) MOSTRAR CLIENTES")
    print("3. (U) MODIFICAR CLIENTE")
    print("4. (D) ELIMINAR CLIENTE")
    print("5. SALIR")
    print("================================")

# ================= INGRESAR =================
def ingresardatos():
    os.system('cls')

    print("=================================")
    print("      INGRESAR CLIENTE          ")
    print("=================================")

    run = input("RUN: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    fono = input("Fono: ")
    correo = input("Correo: ")

    datos = DAO.CRUDCliente.mostrartipos()

    print("---------------------------------")
    for d in datos:
        print(f"{d[0]} - {d[1]}")
    print("---------------------------------")

    # VALIDACIÓN FUERTE (IMPORTANTE)
    tipo = 0
    while tipo not in TIPOS:
        try:
            tipo = int(input("Tipo cliente (1-3): "))
        except:
            tipo = 0

    monto = int(input("Monto crédito: "))

    cliente = Cliente(run, nombre, apellido, direccion, fono, correo, monto, 0, tipo)

    ok = DAO.CRUDCliente.agregar(cliente)

    print("\nCliente ingresado correctamente" if ok else "\nError al ingresar cliente")
    input("\nENTER...")


# ================= MOSTRAR =================
def mostrartodo():
    os.system('cls')

    print("==============================================")
    print("              LISTA CLIENTES                 ")
    print("==============================================")

    print("{:<3} {:<12} {:<10} {:<10} {:<15} {:<10} {:<20} {:<10} {:<8} {:<20}".format(
        "ID","RUN","NOMBRE","APELLIDO","DIRECCION","FONO","CORREO","CREDITO","DEUDA","TIPO"
    ))

    print("-" * 140)

    datos = DAO.CRUDCliente.mostrartodos()

    TIPOS = {
        "Cliente Normal": "1 - Cliente Normal",
        "VIP": "2 - VIP",
        "Empresa": "3 - Empresa"
    }

    for d in datos:
        tipo_nombre = TIPOS.get(d[9], f"0 - {d[9]}")

        print("{:<3} {:<12} {:<10} {:<10} {:<15} {:<10} {:<20} {:<10} {:<8} {:<20}".format(
            d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], tipo_nombre
        ))

    input("\nENTER...")

# ================= MODIFICAR =================
def modificarcliente():
    os.system('cls')

    mostrartodo()

    idc = int(input("\nID a modificar: "))
    datos = DAO.CRUDCliente.consultaparticular(idc)

    if not datos:
        print("Cliente no encontrado")
        input("ENTER...")
        return

    tipo = 0
    while tipo not in TIPOS:
        try:
            tipo = int(input(f"Tipo [{datos[9]}]: "))
        except:
            tipo = datos[9]

    cliente = Cliente(
        datos[1],
        input(f"Nombre [{datos[2]}]: ") or datos[2],
        input(f"Apellido [{datos[3]}]: ") or datos[3],
        input(f"Dirección [{datos[4]}]: ") or datos[4],
        input(f"Fono [{datos[5]}]: ") or datos[5],
        input(f"Correo [{datos[6]}]: ") or datos[6],
        int(input(f"Monto crédito [{datos[7]}]: ") or datos[7]),
        int(input(f"Deuda [{datos[8]}]: ") or datos[8]),
        tipo
    )

    cliente.id = datos[0]

    DAO.CRUDCliente.editar(cliente)

    print("\nCliente modificado correctamente")
    input("\nENTER...")

# ================= ELIMINAR =================
def eliminarcliente():
    os.system('cls')

    clientes = DAO.CRUDCliente.mostrartodos()
    
    if not clientes:
        print("\nNo hay clientes registrados. La base de datos está vacía.")
        input("\nENTER...")
        return

    mostrartodo()

    idcliente = int(input("\nID a eliminar: "))

    while True:
        confirmar = input(f"\n¿Está seguro que desea eliminar el cliente {idcliente}? (S/N): ").strip().upper()

        if confirmar == "S":
            DAO.CRUDCliente.eliminar(idcliente)
            print("\nCliente eliminado correctamente")
            break
        elif confirmar == "N":
            print("\nEliminación cancelada")
            break
        else:
            print("\nDebe ingresar solamente S o N.")

    input("\nENTER...")

# ================= MENÚ =================
while True:
    menu_usuarios()
    op = int(input("Opción: "))

    if op == 1:
        user = input("Usuario: ")
        clave = getpass("Clave: ")
        usuario = Usuario.login(user, clave)

        if not usuario:
            print("Login incorrecto")
            input("Presione ENTER para intentarlo de nuevo...")
            continue
        print(f"\nBienvenido {usuario.nombre}")
        input("Presione ENTER para continuar...")

        while True:
            menuprincipal()
            op2 = int(input("Opción: "))

            if op2 == 1:
                ingresardatos()
            elif op2 == 2:
                mostrartodo()
            elif op2 == 3:
                modificarcliente()
            elif op2 == 4:
                eliminarcliente()
            elif op2 == 5:
                break
            else:
                print("Opción inválida")
                input("Presione ENTER para continuar...")
    elif op == 2:
        ingresoUsuarios()
    else:
        break