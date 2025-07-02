listapedidos = {
    "tilin": {'platos': [{'nombre': 'Pizza con piña', 'precio': 7500}, {'nombre': 'Fideos rojos', 'precio': 6000}], 'total': 13500},
    "pepe": {'platos': [{'nombre': 'Pizza con piña', 'precio': 7500}, {'nombre': 'Fideos al pesto', 'precio': 4000}, {'nombre': 'Fideos rojos', 'precio': 6000}], 'total': 17500},
}
listaplatos = {
    1: {"nombre": "Fideos rojos", "precio": 6000},
    2: {"nombre": "Fideos al pesto", "precio": 4000},
    3: {"nombre": "Pizza con piña", "precio": 7500}
}


def agregar_pedido():
    while True:
        nombre = input("Introduce el nombre del cliente del pedido")
        if not nombre:
            print("El nombre no puede estar vacio.")
            continue
        break
    if nombre not in listapedidos:
            while True:
                try:
                    platos = int(input("Introduce la cantidad de platos a pedir."))
                    if platos >= 1:
                        break
                    else:
                        print("Introduce una cantidad que no sea 0 o menos.")
                except ValueError:
                    print("Introduce un digito valido.")
            for x in listaplatos:
                print(f"{x}) {listaplatos[x]["nombre"]} : {listaplatos[x]["precio"]}")
            pedidoplatos = []
            total = 0
            for x in range(platos):
                while True:
                    try:
                        plato = int(input("Introduce el plato a comprar"))
                        if plato in listaplatos:
                            total += listaplatos[plato]["precio"]
                            pedidoplatos.append((listaplatos[plato]))
                            break
                        else:
                            print("Introduce una opcion de plato valida.")
                    except ValueError:
                        print("Introduce un digito valido de plato [1-3]")
            listapedidos[nombre] = {"platos": pedidoplatos, "total": total}
    else:
        print("No puedes hacer pedidos 2 veces.")

def ver_pedidos():
    print("----------")
    for nombre, pedido in listapedidos.items():
        print(f"{nombre}\nPlatos:")
        for plato in pedido["platos"]:
            print(f" -{plato["nombre"]}: ${plato["precio"]}")
        print(f"Total: ${pedido["total"]}\n----------") 

def calcular_total():
    total = 0
    platos = 0
    pedidos = 0
    for nombre, pedido in listapedidos.items():
        total += pedido["total"]
        pedidos += 1
        for plato in pedido["platos"]:
            platos += 1
    print(f"El total de todos los pedidos juntos es: ${total}\nEsto siendo {platos} platos de parte de {pedidos} pedidos distintos")

def plato_mas_pedido():
    plato1 = 0
    plato2= 0
    plato3= 0
    for nombre, pedido in listapedidos.items():
        for plato in pedido["platos"]:
            if plato == listaplatos[1]:
                plato1 += 1
            elif plato == listaplatos[2]:
                plato2 += 1
            elif plato == listaplatos[3]:
                plato3 += 1
    if plato1 > plato2 and plato1 > plato3:
        print(f"El plato mas pedido es {listaplatos[1]["nombre"]}")
    elif plato2 > plato3 and plato2 > plato1:
        print(f"El plato mas pedido es {listaplatos[2]["nombre"]}")
    elif plato3 > plato2 and plato3 > plato1:
        print(f"El plato mas pedido es {listaplatos[3]["nombre"]}")
    else:
        print("2 o mas platos tienen la misma cantidad de pedidos.")

def estadistica():
    promediot = 0
    total = 0
    for nombre, pedido in listapedidos.items():
        total += 1
        for plato in pedido["platos"]:
            promediot += 1

    promedio = promediot / len(listapedidos)
    print(f"El promedio de platos por pedido es: {promedio:.1f}\nEl total de pedidos es: {total}")

def salir():
    print("Nombre: Melissa Figueroa\nPerfil de Github: https://github.com/MelFig55")

def menu():
    opcion = 0
    while opcion != 6:
        print("Menu de sistema de pedidos en un restaurante.\n1.Registrar pedido\n2.Ver todos los pedidos del dia\n3.Calcular total recaudado\n4.Plato mas pedido\n5.Estadisticas del dia\n6.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("Introduce una opcion valida: [1-6]")
            except ValueError:
                print("Introduce un digito valido.")
        
        if opcion == 1:
            agregar_pedido()
        elif opcion == 2:
            if not listapedidos:
                print("Debes agregar un pedido primero.")
            else:
                ver_pedidos()
        elif opcion == 3:
            if not listapedidos:
                print("Debes agregar un pedido primero.")
            else:
                calcular_total()
        elif opcion == 4:
            if not listapedidos:
                print("Debes agregar un pedido primero.")
            else:
                plato_mas_pedido()
        elif opcion == 5:
            if not listapedidos:
                print("Debes agregar un pedido primero.")
            else:
                estadistica()
        elif opcion == 6:
            salir()

menu()