import os
os.system("cls")

# Area de funciones.

def input_num(pregunta, li, ls):
    while True:
        try:
            n = int(input(pregunta))
            if n >= li and n <= ls:
                return n
            else:
                print(f"Error, debe ingresar una opcion entre {li}y{ls}",1,4)
        except:
            ("Error, debe ingresar solo numeros!")


#Area del programa.

alumnos = {}
ciclo = True
while ciclo:
    print("""
          *** MENU PRINCIPAL ***
          1. Datos de alumno.
          2. Listar alumnos por edades.
          3. Actualizar correo.
          4. Salir.
          """)
    opcion = input_num("Ingrese su opcion:",1,4)
    match opcion:
        case 1:
            print
        case 2:
            print
        case 3:
            print
        case 4:
            ciclo = False
        case _:
            print("Opcion invalida")

print("Fin del Programa.")