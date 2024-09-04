while True:
    print("Ingrese la cantidad de estudiantes por favor:")
    cantidad = int(input())
    if cantidad > 0:
        break
matriz = []

for f in range(1, cantidad+1):
    fila = []
    for c in range(1,3+1):
        print("Ingrese la nota por favor:")
        nota = int(input())
        if nota >= 0 and nota <= 100:
            fila.append(nota)
    matriz.append(fila)

print("La lista de notas es:")
print(matriz)