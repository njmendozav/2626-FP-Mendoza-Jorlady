# Registro de estudiantes

estudiantes = []

# Agregar estudiantes
estudiantes.append("Ana")
estudiantes.append("Carlos")
estudiantes.append("María")
estudiantes.append("José")

# Mostrar estudiantes
print("Lista de estudiantes:")

for estudiante in estudiantes:
    print(estudiante)

# Buscar un estudiante
nombre = input("\nIngrese el nombre del estudiante que desea buscar: ")

if nombre in estudiantes:
    print("El estudiante", nombre, "se encuentra en la lista.")
else:
    print("El estudiante", nombre, "no se encuentra en la lista.")

# Eliminar un estudiante
eliminar = input("\nIngrese el nombre del estudiante que desea eliminar: ")

if eliminar in estudiantes:
    estudiantes.remove(eliminar)
    print("El estudiante", eliminar, "fue eliminado.")
else:
    print("El estudiante", eliminar, "no se encuentra en la lista.")

# Mostrar la lista actualizada
print("\nLista actualizada:")

for estudiante in estudiantes:
    print(estudiante)