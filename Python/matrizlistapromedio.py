while True:
    print("Ingrese la cantidad de estudiantes:")
    cantidade = int(input())
    if cantidade > 0:
        break
matriz = []

for f in range(1, cantidade+1):
    fila = []
    for c in range(1,3+1):
        print("Ingrese la nota por favor:")
        nota = int(input())
        if nota >= 0 and nota <= 100:
            fila.append(nota)
    matriz.append(fila)

promedio = []

for lista in matriz:
    prom = sum(lista)/3
    promedio.append(prom)
    
for lista, pr in zip(matriz, promedio):
    print("Lista de notas: ",lista," Promedio: ",pr,"")