datos = {"comprador":[]}

##menu
while True:

    print ("*** MENU COMPRA DE ENTRADAS CONEJO SIMPATICO ***")
    print ("\n[1] - Comprar entradas")
    print ("\n[2] - Cobsultar comprador")
    print ("\n[3] - Cancelar compra")
    print ("\n[4] - SALIR ")

    opcion = int(input("Ingrese la opcion que desea realizar: "))

    if opcion == 1:
        print ("Sigue los siguientes pasos  para comprar entradas:")
        nombre_comprador = input("\nIngrese el nombre del comprador: ").lower
        tipo_de_entrada = input ("\nIngrese el tipo de entrada que desea (general (g) o VIP (vip): ): ").lower
        codigo_confirmacion = input("ingrese un codigo de confirmacion: ").strip

        print("Entrada registrada con exito!!")

        datos_comprador = [
                                {
                                "nombre_comprador":nombre_comprador,
                                "tipo_de_entrada":tipo_de_entrada,
                                "codigo_confirmacion":codigo_confirmacion
                                }
                            ]

        datos.append(datos_comprador)

    elif opcion == 2:
        print("Se mostraran los datos del comprador: ")
        busqueda_comprador = input("Ingrese el nombre del comprador: ")
        if busqueda_comprador == nombre_comprador:
            print (f"Nombre: {datos["nombre_comprador"]} - Tipo de entrada - {datos["tipo_de_entrada"]} - Codigo de confirmacion: {datos["codigo_confirmacion"]}")

        elif not datos:
            print ("No hay ningun comprador ingresado")
    
    elif opcion == 3:
        eliminar_entrada = input("Ingrese el nombre del comprador de la entrada que desea eliminar: ")
        if eliminar_entrada == nombre_comprador:
            datos_comprador.remove()
            print("Compra cancelada correctamente!!")
        elif eliminar_entrada != nombre_comprador:
            print ("No se pudo cancelar la entrada")

    elif opcion == 4:
        print ("Programa terminado....")
        break
    else:
        print("Debe ingresar una opcion valida!!")