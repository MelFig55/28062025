
listaproductos = {}

def agregar_producto():
    while True:
        try:
            codigo = int(input("Introduce el codigo del producto"))
            if codigo > 999:
                break
            else:
                print("El codigo debe ser mayor a 999")
        except ValueError:
            print("Por favor introduce un numero valido")
    if codigo not in listaproductos:
        while True:
            nombre = input("Introduce el nombre del producto: ")
            if not nombre:
                print("El nombre no puede estar vacio")
                continue
            break
        while True:
            try:
                tipo = input("Introduce el tipo de producto: [Medicamento/suplemento/higiene]").lower()
                if tipo in ["medicamento", "suplemento", "higiene"]:
                    break
                else:
                    print("Ingresa un tipo de producto valido: [Medicamento/suplemento/higiene]")
            except:
                print("Hubo un error, intentalo denuevo.")
        while True:
            try:
                i_stock = int(input("Introduce el stock inicial del producto : "))
                if i_stock >= 0:
                    break
                else:
                    print("El stock inicial no puede ser un numero negativo!")
            except ValueError:
                print("Introduce un digito valido.")
        while True:
            try:
                precio = int(input("Introduce el precio unitario del producto :"))
                if precio >= 0:
                    break
                else:
                    print("El precio unitario no puede ser un numero negativo!")
            except ValueError:
                print("Introduce un digito valido.")

        listaproductos[codigo] = {"nombre": nombre, "tipo": tipo, "stock_inicial": i_stock, "precio": precio}
        print(f"Producto agregado: {listaproductos[codigo].get("nombre")}")
    else:
        print("Ese codigo ya esta en uso.")

def actualizar_stock():
    while True:
        try:     
            codigo = int(input("Introduce  el codigo a buscar:"))
            if codigo > 999:
                break
            else:
                print("Introduce un codigo valido de 4 digitos.")
        except ValueError:
            print("Introduce un digito valido.")
    if codigo in listaproductos:
        print(f"El stock actual es de: {listaproductos[codigo].get("stock_inicial")}. Deseas modificarlo?")
        while True:
            try:
                ask = input("[Y/N]  ").lower()
                if ask in ["y", "n"]:
                    break
                else:
                    print("Introduce una opcion valida.")
            except:
                print("Hubo un error.")

        if ask == "y":
            while True:
                try:
                    stock = int(input("Introduce el stock actualizado: "))
                    if stock >= 0:
                        break
                    else:
                        print("No puede ser un numero negativo")
                except ValueError:
                    print("Introduce un digito valido.")
            listaproductos[codigo]["stock_inicial"] = stock
            print(f"Producto: {listaproductos[codigo].get("nombre")} actualizado!\nStock actual: {listaproductos[codigo].get("stock_inicial")}")
    else:
        print("Ese codigo no esta en la lista de productos.")

def clasificar_productos():
    med = []
    tmed = 0
    suple = []
    tsuple = 0
    higie = []
    thigie = 0
    for productos in listaproductos:
        if listaproductos[productos]["tipo"] == "medicamento":
            med.append((listaproductos[productos]["nombre"], listaproductos[productos]["stock_inicial"], listaproductos[productos]["precio"]))
            tmed += 1
        elif listaproductos[productos]["tipo"] == "suplemento":
            suple.append((listaproductos[productos]["nombre"], listaproductos[productos]["stock_inicial"], listaproductos[productos]["precio"]))
            tsuple += 1
        elif listaproductos[productos]["tipo"] == "higiene":
            higie.append((listaproductos[productos]["nombre"], listaproductos[productos]["stock_inicial"], listaproductos[productos]["precio"]))
            thigie += 1
    
    print(f"TOTAL MEDICAMENTOS: {tmed}")
    for i in med:
        print(f"Nombre: {i[0]} | stock: {i[1]} | precio: ${i[2]}")
    print(f"TOTAL PRODUCTOS HIGIENE {thigie}")
    for i in higie:
        print(f"Nombre: {i[0]} | stock: {i[1]} | precio: ${i[2]}")
    print(f"TOTAL DE SUPLEMENTOS: {tsuple}")
    for i in suple:
        print(f"Nombre: {i[0]} | stock: {i[1]} | precio: ${i[2]}")

def generar_reporte():
    print("LISTA DE PRODUCTOS POR DEBAJO DE 10u DE STOCK")
    for productos in listaproductos:
        if listaproductos[productos]["stock_inicial"] < 10:
            print(f"producto: {listaproductos[productos]["nombre"]} | stock: {listaproductos[productos]["stock_inicial"]}")


def calcular_inv():
    total = 0
    totalprod= 0
    for producto in listaproductos:
        total += (listaproductos[producto]["stock_inicial"]) * (listaproductos[producto]["precio"])
        totalprod += listaproductos[producto]["stock_inicial"]
    print(f"El total del valor de todo el inventario sumado es de: ${total} | productos en total: {totalprod}")

def salir():
    print("\nNombre: Melissa Figueroa\nCarrera: Ingenieria en informatica\nRut: ########")

def menu():
    opcion = 0
    while opcion != 6:
        print("\nMenu de gestion de inventario de Farmacia\n1.Agregar Producto al Inventario\n2.Actualizar stock\n3.Clasificar productos por tipo\n4.Generar Reporte de Stock Crítico\n5.Calcular valor total del inventario\n6.Salir del programa.")
        while True:
            try:
                opcion = int(input(""))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("Introduce una opcion valida [1-6]")
            except ValueError:
                print("Introduce un digito valido [1-6]")
        
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            if not listaproductos:
                print("Debes agregar un producto primero.")
            else:
                actualizar_stock()
        elif opcion == 3:
            if not listaproductos:
                print("Debes agregar un producto primero.")
            else:
                clasificar_productos()
        elif opcion == 4:
            if not listaproductos:
                print("Debes agregar un producto primero.")
            else:
                generar_reporte()
        elif opcion == 5:
            if not listaproductos:
                print("Debes agregar un producto primero.")
            else:
                calcular_inv()
        elif opcion == 6:
            salir()

menu()


### en el ejercicio en github no incluire mi rut 