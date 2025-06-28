listatemp = [-5, 10, 23, 30, 32, 42, 2, 16]

def registrar_temp():
    while True:
        try:
            temp = float(input("Introduce la temperatura a ingresar:"))
            listatemp.append(temp)
            print("Temperatura registrada :-D")
            break
        except ValueError:
            print("Introduce un digito valido.")

def mostrar_temps():
    promedio = sum(listatemp) / len(listatemp)
    print(f"Temperatura maxima: {max(listatemp)}°C\nTemperatura Minima: {min(listatemp)}°C\nTemperatura promedio: {promedio:.2f}°C")

def contar_30c():
    total = sum(1 for temp in listatemp if temp >= 30)
    print(f"El total de dias con temperatura por encima de 30°C es de: {total}")

def clasificar_dias():
    frio = sum(1 for temp in listatemp if temp <= 15)
    templado = sum(1 for temp in listatemp if 16 <= temp <= 22)
    caluroso = sum(1 for temp in listatemp if temp >= 23)
    print(f"\nCantidad de dias calurosos, frios y templados:\nFrios: {frio}\nCalurosos: {caluroso}\nTemplado: {templado}")

def grafico_textual():
    maxtemp = max(listatemp)
    mintemp = min(listatemp)
    rangotemp = maxtemp - mintemp

    if rangotemp == 0:
        escaladotemp = [25] * len(listatemp)
    else:
        escaladotemp = []
        for i in listatemp:
            valor_escalado = int(((i - mintemp) /rangotemp) * 50)
            escaladotemp.append(valor_escalado)

    print("\nGrafico de temperaturas:")
    for i, x in enumerate(listatemp):
        print(f"Dia: {i+1:2d} ({x}°C): {'*' * escaladotemp[i]}") 

def salir():
    print("Autor: MelFig55\nRepositorio: https://github.com/MelFig55/28062025")

def menu():
    opcion = 0
    while opcion != 6:
        print("Menu de registro y analisis del clima\n1.Registrar temperatura\n2.Mostrar temperatura\n3.Contar dias con temperatura +30°C\n4.Clasificar dias segun temperatura\n5.Mostrar grafico textual en '*'\n6.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("Introduce una opcion valida.")
            except ValueError:
                print("Introduce un digito valido. [1-6]")
    
        if opcion == 1:
            registrar_temp()
        elif opcion == 2:
            if not listatemp:
                print("Debes ingresar una temperatura primero.")
            else:
                mostrar_temps()
        elif opcion == 3:
            if not listatemp:
                print("Debes ingresar una temperatura primero.")
            else:
                contar_30c()
        elif opcion ==  4:
            if not listatemp:
                print("Debes ingresar una temperatura primero.")
            else:
                clasificar_dias()
        elif opcion == 5:
            if not listatemp:
                print("Debes ingresar una temperatura primero.")
            else:
                grafico_textual()
        elif opcion == 6:
            salir()


menu()