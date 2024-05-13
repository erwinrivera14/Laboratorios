import math
#área de definición de funciones
def menu():
    print("Elija una opción: ")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    opcion=input()
    return opcion
def ObtenerAreaTriangulo(base,altura):
    #area:(base*altura)/2
    return(base*altura)/2
def ObtenerAreaCuadrado(lado):
    return lado**2
def ObtenerAreaRectangulo(base,altura):
    return base*altura
def ObtenerAreaCirculo(radio):
    return math.pi*radio**2
#área de interacción con el usuario
print("Semana No. 15 - Ejercicio 1")
match (menu()):
    case "a":
        print("El área del triángulo es: ",ObtenerAreaTriangulo(float(input("Ingrese la base de un triángulo: ")),float(input("Ingrese la altura de un triángulo: "))))
    case "b":
        print("El área del cuadrado es: ",ObtenerAreaCuadrado(float(input("Ingrese el lado del cuadrado: "))))
    case "c":   
        print("El área del rectangulo es: ",ObtenerAreaRectangulo(float(input("Ingrese la base de un rectángulo: ")),float(input("Ingrese la altura de un rectángulo: "))))
    case "d":
        print("El área del círculo es: ",round(ObtenerAreaCirculo(float(input("Ingrese el radio del círculo: "))),2))

print("Semana no 15. - Ejercicio 2")
x=0
y=0
def():
    print("Elija una opción")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")