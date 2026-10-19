notas = [14, 16, 11, 18, 13]
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota maxima:", max(notas))
print("Nota minima:", min(notas))
print("Cantidad de notas:", len(notas))

from statistics import median, mode

print("Mediana de notas:", median(notas))

print("Moda de notas:", mode(notas))

aprobados = 0
desaprobados = 0

for nota in notas:
    if nota >= 11: 
        aprobados += 1
    else:
        desaprobados += 1

print("Alumnos aprobados:", aprobados)
print("Alumnos desaprobados:", desaprobados)
