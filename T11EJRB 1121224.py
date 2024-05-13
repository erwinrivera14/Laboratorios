print("Erwin José Rivera Bautista")
print("Carné: 1121224")
print("")
n= int(input("Ingrese un numero mayor a 0: "))

if (n <= 0):
    print("Error, debe ser mayor a 0")

#Definicion de variables
a = 0
b = 1
c = 0
i = 2
resultado = ""

if(n > 0):
    resultado = str(a)

    if(n>1):
        resultado += ","+ str(b)

    print(resultado)

    while(i<n):
        c = a + b
        resultado += "," +str(c) 
        a = b 
        b = c
        i = i + 1
    print(resultado)
else:
    print(resultado)


print("Semana No. 11: Ejercicio 2")

n2 = int(input("Ingrese un numero mayor a 0: "))

if(n2 <= 0):
    print("Error, debe ser mayor a 0")

#Ejercicio A
resultadoA = 0
for x in range(1, n2 + 1):
    resultadoA += 1/x

print("Inciso A:", resultadoA)

#Ejercicio B
resultadoB = 0
for x in range(1, n2 + 1):
    resultadoB += 1/2**x

print("Inciso B:", resultadoB)

#Ejercicio C
x = int(input("Ingrese un numero entero: "))
a = int(input("Ingrese un numero entero: "))
n = int(input("Ingrese un numero entero: "))

ResultadoC = 0
for k in range(1, n2 + 1):
    ResultadoC += x*k*a*(n2-k)

print("Inciso C:", ResultadoC)