# Variables
menor_50 = 0
entre_50_y_70 = 0
entre_70_y_80 = 0
mayor_a_80 = 0

# Solicitacion de datos
for i in range(1, 11):
    calificacion = int(input(f"Ingrese la calificación del estudiante {i}: "))
    
    # Proceso 
    if calificacion < 50:
        menor_50 += 1
    elif calificacion >= 50 and calificacion < 70:
        entre_50_y_70 += 1
    elif calificacion >= 70 and calificacion < 80:
        entre_70_y_80 += 1
    else:
        mayor_a_80 += 1

# los resultados
print("Estudiantes que obtuvieron calificaciones menores a 50:", menor_50)
print("Estudiantes que obtuvieron calificaciones entre 50 y 70:", entre_50_y_70)
print("Estudiantes que obtuvieron calificaciones entre 70 y 80:", entre_70_y_80)
print("Estudiantes que obtuvieron calificaciones mayores a 80:", mayor_a_80)
