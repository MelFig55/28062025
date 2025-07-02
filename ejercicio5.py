listapedidos = {}
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
                    num_platos = int(input("Introduce la cantidad de platos a pedir."))
                    if num_platos >= 1:
                        break
                    else:
                        print("Introduce una cantidad que no sea 0 o menos.")
                except ValueError:
                    print("Introduce un digito valido.")
            print("Platos disponibles:")
            for id, plato in listaplatos.items():
                print(f"{id}:  {plato["nombre"]} - ${plato["precio"]}")
            pedido_platos = []
            total = 0
            for x in range(num_platos):
                while True:
                    try:
                        plato_id = int(input(f"Plato #{x+1}: "))
                        if plato_id not in listaplatos:
                            print("Error: ID de plato invalido")
                            continue
                        pedido_platos.append(plato_id)
                        total += listaplatos[plato_id]["precio"]
                        break
                    except ValueError:
                        print("Introduce un digito valido.")
            listapedidos[nombre] = {
                "platos": pedido_platos,
                "total": total}
            print(f"Pedido a nombre de {nombre} realizado!")
    else:
        print("No puedes hacer pedidos 2 veces.")

def ver_pedidos():
    print("\n--- TODOS LOS PEDIDOS ---")
    for nombre, pedido in listapedidos.items():
        print(f"\nCliente: {nombre}\nPlatos:")
        for plato_id in pedido["platos"]:
            plato = listaplatos[plato_id]
            print(f" -{plato["nombre"]}: ${plato["precio"]}")
        print(f"Total: ${pedido["total"]}")
    print("-----------------") 

def calcular_total():

    total_recaudado = sum(pedido["total"] for pedido in listapedidos.values())
    total_platos = sum(len(pedidos["platos"]) for pedidos in listapedidos.values())

    print(f"El total de todos los pedidos juntos es: ${total_recaudado}\nEsto siendo {total_platos} platos de parte de {len(listapedidos)} pedidos distintos")

def plato_mas_pedido():
    contador = {nombre: 0 for nombre in listaplatos}
    for pedido in listapedidos.values():
        for plato_id in pedido["platos"]:
            contador[plato_id] += 1
    max_id = max(contador, key=contador.get)
    max_nombre = listaplatos[max_id]["nombre"]
    print(f"El plato mas pedido es: {max_nombre}\nVeces pedido {contador[max_id]}")


def estadistica():
    total_pedidos = len(listapedidos)
    total_platos = sum(len(pedidos["platos"]) for pedidos in listapedidos.values())
    promedio = total_platos / total_pedidos

    print(f"El promedio de platos por pedido es: {promedio:.1f}\nEl total de pedidos es: {total_pedidos}")

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