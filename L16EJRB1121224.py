import random
print("Semana No. 16: Ejercicio 1 ")
A=[]
for i in range(10):
    r=random.randint(1,100)
    A.append(r)

promedio=0
for num in A:
    promedio+=num
promedio=promedio/len(A)
print(A)
print("La cantidad de elementos es de",len(A))
print("El promedio es",promedio)

sumapar=0
sumaimpar=0
for i in range(len(A)):
    if i%2==0:
        sumapar+=A[i]
    else:
        sumaimpar+=A[1]
print("La suma par es:",sumapar)
print("La suma impar es:",sumaimpar)

print("\n Semana No. 16: Ejercicio 2")

def NumMayor(arreglo):
    mayor=arreglo[0][0]
    for i in range (len(arreglo)):
        for j in range (len(arreglo[i])):
            if arreglo[i][j]>mayor:
                mayor=arreglo[i][j]
    return mayor

def NumMenor(arreglo):
    menor=arreglo[0][0]
    for i in range (len(arreglo)):
        for j in range (len(arreglo[i])):
            if arreglo[i][j]<menor:
                menor=arreglo[i][j]
    return menor

filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))
B=[]
for i in range(filas):
    temporal=[]
    for j in range(columnas):
        r=random.randint(0,1001)
        temporal.append(r)
    B.append(temporal)
print(B)

par=0
impar=0
for i in range(filas):
    for j in range(columnas):
        if j%2==0:
            par+=1
        else:
            impar+=1

print("El número mayor es: ",NumMayor(B))
print("El número menor es: ",NumMenor(B))
print("La cantidad de números par es: ",par)
print("La cantidad de números par es: ",impar)

    






