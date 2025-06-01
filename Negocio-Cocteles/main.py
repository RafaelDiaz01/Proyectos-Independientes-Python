#Kevin Rafael Díaz López
#Código para mostrar el panel principal de la aplicación Python.
import inicio_sesion

print("\t----Bienvenido a Nuestra Aplicación----")

while True:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    if not inicio_sesion.validar(usuario, password): # Llama a la función para validar.
        break

input("¿Qué deseas ordenar hoy? ")