notas = [14, 16, 11, 18, 13]
nombres = ["Darell", "Fulanito", "Gaga", "Golosito", "Casper"]
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota maxima:", max(notas))
print("Nota minima:", min(notas))
print("Cantidad de notas:", len(notas))

for i in range(len(nombres)):
 print(f"La nota de {nombres[i]} es {notas[i]}, y es el {round(notas[i]*100/max(notas),4)} % de la máxima nota")

from statistics import median

print("Mediana de notas:", median(notas))
