# 11. Calificación de alumnos
# Dada una lista de tuplas con el nombre del alumno y su calificación, utiliza map y filter para obtener una lista con los nombres de los alumnos que han aprobado (nota >= 5).

alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]

def aprobado(alumno):
    return alumno[1] >= 5

aprobados = list(filter(aprobado, alumnos)) # aprobado lambada -> lambda x: x[1] >= 5
nombre_aprobados = list(map(lambda x: x[0], aprobados))

print(nombre_aprobados)