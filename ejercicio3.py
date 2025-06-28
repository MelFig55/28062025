listalumnos = {
    "pepe": [5.0, 3.7, 4.2],
    "tilin": [4.2, 5.6, 6.3],
    "sech": [3.2, 3.5, 2.6]
}

def ingresar_estudiante():
    while True:
        nombre = input("Nombre estudiante: ")
        if not nombre:
            print("No puede estar vacio el nombre.")
            continue
        break
    if nombre in listalumnos:
        print("No puede ingresar el mismo alumno 2 veces.")
    else:
        while True:
            try:
                nota1= float(input("Introduce la primera nota: "))
                nota2= float(input("Introduce la segunda nota: "))
                nota3= float(input("Introduce la tercera nota: "))
                listalumnos[nombre] = [nota1, nota2, nota3]
                break
            except ValueError:
                print("Introdujiste mal un digito, intentalo denuevo.")
        print(f"Alumno {nombre} agregado con exito!\nNotas: {listalumnos[nombre]}")

def calcular_promedios():
    for alumno in listalumnos:
        promedio = sum(listalumnos[alumno]) / len(listalumnos[alumno])
        print(f"Alumno: {alumno} | promedio: {promedio:.1f}")

def identificar_aprobados():
    count = 0
    print("Lista aprobados: ")
    for alumno in listalumnos:
        promedio = sum(listalumnos[alumno]) / len(listalumnos[alumno])
        if promedio >= 4.0:
            print(f"Alumno: {alumno} | promedio: {promedio:.1f}")
    print("Lista reprobados:")
    for alumno in listalumnos:
        promedio = sum(listalumnos[alumno]) / len(listalumnos[alumno])
        if promedio <= 3.9:
            print(f"Alumno: {alumno} | promedio: {promedio:.1f}")
            count += 1
    if count == 0:
        print("No hubo reprobados!! :3")

def mejorypeor():
    promediomax = 0
    promediomin = 10
    for alumno in listalumnos:
        promedio = sum(listalumnos[alumno]) / len(listalumnos[alumno])
        if promedio > promediomax:
            promediomax = promedio
        if promedio < promediomin:
            promediomin = promedio
    print("Mejor promedio!!! :")
    for alumno in listalumnos:
        promedio = sum(listalumnos[alumno]) / len(listalumnos[alumno])
        if promedio == promediomax:
            print(f"{alumno} tiene el mejor promedio!!! | promedio: {promedio:.1f}")
    print("Peor promedio... :")
    for alumno in listalumnos:
        promedio = sum(listalumnos[alumno]) / len(listalumnos[alumno])
        if promedio == promediomin:
            print(f"{alumno} tiene el peor promedio :c | promedio: {promedio:.1f}")

def listado():
    lista = []

    for alumno, notas in listalumnos.items():
        promedio = sum(notas) / len(notas)
        lista.append((promedio, alumno))
    
    lista.sort(reverse=True)

    for posicion, (promedio, nombre) in enumerate(lista, 1):
        print(f"{posicion}: {nombre} | promedio {promedio:.1f}")

def salir():
    print("Nombre: Melissa Figueroa\nRepositorio: https://github.com/MelFig55/28062025\nPerfil github: https://github.com/MelFig55")

def menu():
    opcion = 0
    while opcion != 6:
        print("Menu de sistema de notas de estudiantes.\n1.Ingresar estudiante y 3 notas\n2.Calcular promedio de cada estudiante\n3.Identificar aprobados y reprobados\n4.Mostrar mayor promedio y menor promedio\n5.Generar listado en orden de promedios\n6.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("Introduce una opcion valida [1-6]")
            except ValueError:
                print("Introduce un digito valido. [1-6]")
        if opcion == 1:
            ingresar_estudiante()
        elif opcion == 2:
            if not listalumnos:
                print("Debes ingresar un estudiante primero.")
            else:
                calcular_promedios()
        elif opcion == 3:
            if not listalumnos:
                print("Debes ingresar un estudiante primero.")
            else:
                identificar_aprobados()
        elif opcion == 4:
            if not listalumnos:
                print("Debes ingresar un estudiante primero.")
            else:
                mejorypeor()
        elif opcion == 5:
            if not listalumnos:
                print("Debes ingresar un estudiante primero.")
            else:
                listado()
        elif opcion == 6:
            salir()

menu()