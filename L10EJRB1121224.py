#Erwin Rivera 1121224 
print("Semana No. 10: Ejercicio 1")
num = int(input("Ingresar un número entre 1 y 12: "))
if num < 1 or num >12:
    print("Error, el número a ingresar debe de ser entre 1 y 12")
else:
    if num == 1:
        print("Mes, enero")
    elif num == 2:
        print("Mes: febrero")
    elif num == 3:
        print("Mes: marzo")
    elif num == 4:
        print("Mes: abril")
    elif num == 5:
        print("Mes: mayo")
    elif num == 6:
        print("Mes: junio")
    elif num == 7:
        print("Mes: julio")
    elif num == 8:
        print("Mes: agosto")
    elif num == 9:
        print("Mes: septiembre")
    elif num == 10:
        print("Mes: octubre")
    elif num == 11:
        print("Mes: noviembre")
    elif num == 12:
        print("Mes: diciembre")    

print()
print("Semana No. 10: Ejercicio 2")
A=int(input("Ingrese un número mayor a cero: "))
B=int(input("Ingrese un segundo número mayor a cero: "))
C=int(input("Ingrese un tercer número mayor a cero: "))

if A<0 and B<0 and C<0:
    print("Número inválido")
else: 
    if A>B:
        if A>C:
            print("A es mayor a C y B")
        else: 
            if A==C:
                print("A y C son mayores a B")
            else:
                print("C es mayor a A y B")
    else:
        if A==B:
            if A>C:
                print("A y B son mayores a C")
            else:
                if A==C:
                    print("A, B y C son iguales")
                else: 
                    print ("C es mayor a A y B")
        else:
            if B>C:
                print("B es mayor a A y C")
            else: 
                if B==C:
                    print("B y C son mayores a A")
                else: 
                    print("C es mayor a A y B")

print()
print("Semana No. 10: Ejercicio 3")
dia=int(input("Ingrese el día de su nacimiento: "))
mes=int(input("Ingrese el mes de su nacimiento en numeros del 1 al 12: "))
año=int(input("Ingrese el año en que nació: "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "aries"

elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    signo = "tauro"

elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
    signo = "geminis"

elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    signo = "cancer"

elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    signo = "leo"

elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
    signo = "virgo"

elif (mes == 9 and dia >= 24) or (mes == 10 and dia <= 23):
    signo = "libra"

elif (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
    signo = "escorpio"

elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
    signo = "sagitario"

elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    signo = "capricornio"

elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
    signo = "acuario"

elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
    signo = "piscis"
    
else:
    signo = "Fecha de nacimiento inválida"

print("Tu signo zodiacal es: ", signo)