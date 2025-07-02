listaautos = {
    "999999": {"tipo": "auto", "km": 10000, "mantencion": 20000},
    "ABDCFG": {"tipo": "camion", "km": 12500, "mantencion": 30000},
    "FGHJKL": {"tipo": "bus", "km": 50000, "mantencion": 40000}
}

def agregar_vehiculo():
    while True:
        patente = input("Introduce la patente de 6 caracteres")
        if len(patente) != 6:
            print("Debe tener almenos 6 digitos")
            continue
        break
    if patente not in listaautos:
        while True:
            try:
                tipo = input("Introduce un tipo de vehiculo: [Auto/Camion/Bus]").lower()
                if tipo in ["auto", "camion", "bus"]:
                    break
                else:
                    print("Introduce un tipo de vehiculo valido: [auto/camion/bus]")
            except:
                print("Hubo un error. Intentalo denuevo")
        while True:
            try:
                km = float(input("Introduce el kilometraje actual (en km)"))
                if km >= 0:
                    break
                else:
                    print("Introduce un un kilometraje actual valido superior o igual a 0")
            except ValueError:
                print("Introduce digitos validos.")
        while True:
            try:
                mantencion = float(input("Introduce el kilometraje de la ultima mantencion"))
                if mantencion >= 0:
                    break
                else:
                    print("Introduce un un kilometraje de la ultima mantencion superior o igual a 0")
            except ValueError:
                print("Introduce digitos validos.")
        listaautos[patente] = {"tipo": tipo, "km": km, "mantencion": mantencion}
    else:
        print("No se puede introducir 2 veces la misma patente.")

def actualizar_km():
    while True:
            patente = input("Introduce la patente de 6 caracteres")
            if len(patente) < 6:
                print("Debe tener almenos 6 digitos")
                continue
            break
    if patente not in listaautos:
                print("Esta patente no esta registrada, intentalo denuevo.")
    else:
        while True:
            ask = input(f"Deseas actualizar el Kilometraje de este vehiculo? [{listaautos[patente]["tipo"]}|{patente}|] : km: {listaautos[patente]["km"]} | Y/N").lower()
            if ask not in ["y", "n"]:
                print("Introduce una opcion valida [Y/N]")
                continue
            break
        if ask == "y":
            while True:
                try:
                    km_nuevo = float(input("Introduce el nuevo kilometraje del vehiculo")) 
                    if km_nuevo >= 0:
                        break
                    else:
                        print("Introduce un kilometraje valido")   
                except ValueError:
                    print("Introduce un kilometraje valido")
            listaautos[patente]["km"] = km_nuevo
            print(f"El kilometraje del auto [{listaautos[patente]["tipo"]}|{patente}|] ha sido actualizado a: {km_nuevo}")
        if ask == "n":
            print("No se cambiara nada!")

def revisar_autos():
    print("Lista de autos con mantencion pendiente: ")
    for x in listaautos:
        if listaautos[x]["km"] % 10000 == 0:
            print(f"Patente: {x} | km: {listaautos[x]["km"]}")

def listar_autos():
    print("Lista de autos:")
    for x in listaautos:
        if listaautos[x]["tipo"] == "auto":
            print(f"Patente: {x} | {listaautos[x]["tipo"]} | {listaautos[x]["km"]}KM")
    print("Lista camiones:")
    for x in listaautos:
        if listaautos[x]["tipo"] == "camion":
            print(f"Patente: {x} | {listaautos[x]["tipo"]} | {listaautos[x]["km"]}KM")
    print("Lista buses:")
    for x in listaautos:
        if listaautos[x]["tipo"] == "bus":
            print(f"Patente: {x} | {listaautos[x]["tipo"]} | {listaautos[x]["km"]}KM")

def resumen_flota():
    cantidad = 0
    kms = []
    max_km = 1
    placa = None
    for x in listaautos:
        kms.append(listaautos[x]["km"])
        cantidad += 1
    for placa, auto in listaautos.items():
        if auto["km"] > max_km:
            max_km = auto["km"]
            placa = placa
    promedio = sum(kms) / len(kms)
    print(f"Promedio km de todos los vehiculos: {promedio:.2f}\nCantidad vehiculos: {cantidad}\nVehiculo mas usado: {placa} | {max_km}")

def salir():
    print("Link repositorio: https://github.com/MelFig55/28062025/tree/main\nNombre: Melissa Figueroa\nCarrera: Ing en informatica\nRut: ########")

def menu():
    opcion = 0
    while opcion != 6:
        print("Menu de control de flota de vehiculos\n1.Agregar vehiculo\n2.Actualizar kilometraje\n3.Revisar vehiculos con mantencion pendiente\n4.Listar vehiculos por tipo\n5.Generar resumen de flota\n6.Salir.")
        while True:
            try:
                opcion = int(input(""))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("Introduce una opcion valida [1-6]")
            except ValueError:
                print("Introduce un digito valido.")
        
        if opcion == 1:
            agregar_vehiculo()
        elif opcion == 2:
            if not listaautos:
                print("Introduce un auto a la lista primero.")
            else: 
                actualizar_km()
        elif opcion == 3:
            if not listaautos:
                print("Introduce un auto a la lista primero.")
            else: 
                revisar_autos()
        elif opcion == 4:
            if not listaautos:
                print("Introduce un auto a la lista primero.")
            else: 
                listar_autos()
        elif opcion == 5:
            if not listaautos:
                print("Introduce un auto a la lista primero.")
            else: 
                resumen_flota()
        elif opcion == 6:
            salir()

menu() 

#actualizar_km
#agregar_vehiculo()
#evisar_autos()
#listar_autos()
#resumen_flota()