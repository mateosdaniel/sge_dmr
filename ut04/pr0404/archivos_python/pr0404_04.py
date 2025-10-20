# 4. Diccionario de listas

asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

i = int(input("Selecciona un número del 1 al 3: "))
match i:
    case 1:
        asignatura = input("Introduce una asignatura: ")
        print(asignaturas.get(asignatura))
    case 2:
        asignatura = input("Introduce una asignatura: ")
        alumno = input("Introduce el nuevo alumno: ")
        alumnos_en_asignatura = asignaturas.get(asignatura)
        if alumno not in alumnos_en_asignatura:
            alumnos_en_asignatura.append(alumno)
            print(asignaturas)
        else:
            print("El alumno ya se encuentra matriculado en esta asignatura")
    case 3:
        asignatura = input("Introduce una asignatura: ")
        alumno = input("Introduce el alumno que quieres eliminar: ")
        alumnos_en_asignatura = asignaturas.get(asignatura)
        if alumno in alumnos_en_asignatura:
            alumnos_en_asignatura.remove(alumno)
            print(asignaturas)
        else:
            print("El alumno no se encuentra matriculado en esta asignatura")
    case _:
        print("Eso no es un número del 1 al 3")


