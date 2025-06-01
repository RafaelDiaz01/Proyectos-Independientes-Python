# Kevin Rafael Díaz López - 31/05/2025
# Código para mostrar el inicio de sesión de la aplicación.
def validar (usuario, password):
    bandera = True
    if usuario == "admin" and password == "123":
        print("Acceso correcto, bienvenido al sistema\n")
        bandera = False
    else:
        print("Usuario o contraseña incorrectos, inténtelo de nuevo")
        print("----------------------------------------------------\n")
    return bandera
