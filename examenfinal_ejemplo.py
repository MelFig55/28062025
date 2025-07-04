# telefonos = {modelo: [marca, tamaño_pantalla, RAM, almacenamiento, procesador, cámara], ...}

telefonos = {
    'A123': ['Samsung', 6.5, '4GB', '64GB', 'Exynos 9611', '48MP'],
    'B234': ['Apple', 6.1, '6GB', '128GB', 'A15 Bionic', '12MP'],
    'C345': ['Xiaomi', 6.43, '8GB', '256GB', 'Snapdragon 778G', '108MP'],
    'D456': ['Motorola', 6.7, '4GB', '128GB', 'MediaTek Helio G85', '50MP'],
    'E567': ['Samsung', 6.4, '6GB', '128GB', 'Exynos 850', '64MP'],
    'F678': ['Apple', 5.4, '4GB', '64GB', 'A14 Bionic', '12MP'],
    'G789': ['Xiaomi', 6.67, '12GB', '512GB', 'Snapdragon 8 Gen 1', '200MP'],
}

# stock = {modelo: [precio, stock], ...}

stock = {
    'A123': [199990, 5],
    'B234': [849990, 2],
    'C345': [349990, 8],
    'D456': [179990, 0],
    'E567': [229990, 10],
    'F678': [399990, 1],
    'G789': [699990, 3],
}

def stock_marca(marca):
    count = 0
    for clave, valor in telefonos.items():
        if valor[0] == marca:
            for key, value in stock.items():
                if key == clave:
                    count += value[1]
    if count >= 1:
        print(f"La cantidad de la marca {marca} en stock es {count}")



def buscar_por_precio(p_min, p_max):
    count = 0
    if isinstance(p_min, float) or isinstance(p_max, float):
        return print("Debe ingresar valores enteros")
    else:
        for clave, valor in stock.items():
            if p_min <= valor[0] <= p_max:
                for key, value in telefonos.items():
                    if key == clave:
                        print(f"{value[0]} - {clave} - ${valor[0]}")
                        count += 1
    if count == 0:
        print("No hay telefonos en ese rango de precios.")



def actualizar_precio(modelo, nuevo_precio):
    count = 0
    if modelo in stock:
        for clave, valor in stock.items():
            if clave == modelo:
                valor[0] = nuevo_precio
                print("Precio actualizado!")
                count += 1
                while True:
                    ask = input("Deseas actualizar otro precio? [s/n]").lower()
                    if ask not in ["s", "n"]:
                        print("Introduce una opcion valida!")
                        continue
                    break
                if ask == "s":
                    for key, value in telefonos.items():
                        for x, y in stock.items():
                            if x == key:
                                print(f"Modelo: {x} - Marca: {value[0]} - Precio: {y[0]}")
                    while True:
                        pregunta = input("Introduce otro modelo a actualizar el precio!").capitalize()
                        if pregunta not in stock:
                            print("Introduce un modelo valido de la lista!")
                            continue
                        break
                    while True:
                        try:
                            p_new = int(input("Introduce el nuevo precio!"))
                            if isinstance(p_new, int):
                                break
                            else:
                                print("Introduce un precio valido!")
                        except ValueError:
                            print("Introduce un numero entero.")
                    stock[pregunta][0] = p_new
                    print("Precio actualizado!")    
                return True
    else:
        print("El modelo no existe")
        return False



def salir():
    print("Programa finalizado.")

def menu():
    opcion = 0
    while opcion != 4:
        print("*** MENÚ PRINCIPAL ***\n1.Stock por marca\n2.Buscar por rango de precios\n3.Actualizar precio de modelo\n4.Salir")
        while True:
            try:
                opcion = int(input(""))
                if 1 <= opcion <= 4:
                    break
                else:
                    print("Debe seleccionar una opcion valida!!!!")
            except ValueError:
                print("Ingresa un digito entero valido entre [1-4]")

        if opcion == 1:
            mark = input("Introduce una marca").capitalize()
            stock_marca(mark)
        elif opcion == 2:
            while True:
                try:
                    precio1 = int(input("Introduce el precio minimo: "))
                    precio2= int(input("Introduce el precio maximo: "))
                    if isinstance(precio1, int) and isinstance(precio2, int):
                        break
                except ValueError:
                    print("Debe ingresar numeros enteros, intentalo denuevo!")
            buscar_por_precio(precio1, precio2)
        elif opcion == 3:
            model = input("Modelo: ")
            while True:
                try:
                    precion = int(input("Introduce un precio nuevo para ese modelo:"))
                    if isinstance(precion, int):
                        break
                except ValueError:
                    print("Introduce un numero entero!!!")
            actualizar_precio(model, precion)
        elif opcion == 4:
            salir()
menu()