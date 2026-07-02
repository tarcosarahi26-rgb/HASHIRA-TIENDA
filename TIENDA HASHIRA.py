def mostrar_factura(saldoapagar):
    print(":::::::::::: FACTURA ::::::::::::::")
    print("TOTAL A PAGAR: $" + str(saldoapagar))
    if saldoapagar >= 1000:
        print("USTED ES GANADOR DE 5 MANGAS DE SU PREFERENCIA")
    elif saldoapagar >= 500:
        print("USTED ES GANADOR DE 75 CUPONES DE DESCUENTO")
    print("Gracias por comprar en HASHIRA")
    print("¡Esperamos verle nuevamente!")


def gestionar_pedido(saldoapagar):
    
    while True:
        print("¿Desea pedir más?")
        print("1 SI")
        print("2 FINALIZAR PEDIDO")
        continuarcompra = int(input("Elija una opción: "))

        if continuarcompra == 1:
            return saldoapagar, False

        elif continuarcompra == 2:
            cancelarpedido = input("¿Desea cancelar su pedido? (si/no): ")

            if cancelarpedido == "si":
                saldoapagar = 0
                print("Lamentamos, si el servicio no fue de su agrado")
                print("Estamos mejorando, por favor vuelva pronto")
                return saldoapagar, True

            else:
                while True:
                    print("Elija una miniopción")
                    print("1 Desea seguir agregando productos")
                    print("2 Pagar mi orden")
                    continuarcompra2 = int(input("Opción: "))

                    if continuarcompra2 == 1:
                        return saldoapagar, False
                    elif continuarcompra2 == 2:
                        mostrar_factura(saldoapagar)
                        return saldoapagar, True
                    else:
                        print("Opción inválida, intente de nuevo")
        else:
            print("Opción inválida, intente de nuevo")


def menu_postres(saldoapagar):
    while True:
        print("************** MENÙ DE POSTRES *****************")
        print("1. TANGHULU .............. $1.50")
        print("2. DORAYAKI .............. $3.50")
        print("3. DANGO ................. $4.00")
        print("4. MOCHI .................. $3.50")
        print("5. BINGSU ................ $10.00")
        print("6. DESEO VOLVER AL MENU OPCIONES")

        segundaopcion = int(input("Por favor elija una opción: "))

        if segundaopcion >= 1 and segundaopcion <= 5:
            agregarcantidad = int(input("Agregue la cantidad de unidades deseadas: "))

            if segundaopcion == 1:
                subtotal = agregarcantidad * 1.50
            elif segundaopcion == 2:
                subtotal = agregarcantidad * 3.50
            elif segundaopcion == 3:
                subtotal = agregarcantidad * 4.00
            elif segundaopcion == 4:
                subtotal = agregarcantidad * 3.50
            elif segundaopcion == 5:
                subtotal = agregarcantidad * 10.00

            saldoapagar = saldoapagar + subtotal

            print("Su producto fue agregado correctamente")
            print("Subtotal agregado: $" + str(subtotal))
            print("Saldo actual: $" + str(saldoapagar))

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar

        elif segundaopcion == 6:
            return saldoapagar
        else:
            print("Opción inválida, intente de nuevo")


def menu_bebidas(saldoapagar):
    while True:
        print("************ MENÙ DE BEBIDAS *****************")
        print("1. TÉ MACHA LATTE ........................ $4.50")
        print("2. TÉ NEGRO CON LECHE CONDENSADA ......... $5.50")
        print("3. TÉ DE CRISANTEMO ...................... $5.00")
        print("4. RAMUNE ................................. $2.50")
        print("5. CALPIS ................................. $13.50")
        print("6. DESEO VOLVER AL MENU OPCIONES")

        terceraopcion = int(input("Por favor elija una opción: "))

        if terceraopcion >= 1 and terceraopcion <= 5:
            agregarcantidad = int(input("Agregue la cantidad de unidades deseadas: "))

            if terceraopcion == 1:
                subtotal = agregarcantidad * 4.50
            elif terceraopcion == 2:
                subtotal = agregarcantidad * 5.50
            elif terceraopcion == 3:
                subtotal = agregarcantidad * 5.00
            elif terceraopcion == 4:
                subtotal = agregarcantidad * 2.50
            elif terceraopcion == 5:
                subtotal = agregarcantidad * 13.50

            saldoapagar = saldoapagar + subtotal

            print("Su bebida fue agregada correctamente")
            print("Subtotal agregado: $" + str(subtotal))
            print("Saldo actual: $" + str(saldoapagar))

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar

        elif terceraopcion == 6:
            return saldoapagar
        else:
            print("Opción inválida, intente de nuevo")


def menu_articulos(saldoapagar):
    while True:
        print("*********** MENÙ DE ARTICULOS **********")
        print("1. PELUCHES PERSONALIZADOS ............... $15.50")
        print("2. PINES PERSONALIZADOS .................. $5.50")
        print("3. LLAVEROS PERSONALIZADOS ................ $3.00")
        print("4. PLUMAS PERSONALIZADOS .................. $2.50")
        print("5. VASOS PERSONALIZADOS ................... $13.50")
        print("6. DESEO VOLVER AL MENU OPCIONES")

        cuartaopcion = int(input("Por favor elija una opción: "))

        if cuartaopcion >= 1 and cuartaopcion <= 5:
            agregarcantidad = int(input("Agregue la cantidad de unidades deseadas: "))

            if cuartaopcion == 1:
                subtotal = agregarcantidad * 15.50
            elif cuartaopcion == 2:
                subtotal = agregarcantidad * 5.50
            elif cuartaopcion == 3:
                subtotal = agregarcantidad * 3.00
            elif cuartaopcion == 4:
                subtotal = agregarcantidad * 2.50
            elif cuartaopcion == 5:
                subtotal = agregarcantidad * 13.50

            saldoapagar = saldoapagar + subtotal

            print("Su artículo fue agregado correctamente")
            print("Subtotal agregado: $" + str(subtotal))
            print("Saldo actual: $" + str(saldoapagar))

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar

        elif cuartaopcion == 6:
            return saldoapagar
        else:
            print("Opción inválida, intente de nuevo")


def menu_combos(saldoapagar):
    while True:
        print("************* MENÙ DE COMBOS ********************")
        print("1. COMBO 1: 2 DORAYAKIS + PASTEL DE LUNA + TE DE MACHA .... $19.00")
        print("2. COMBO 2: TÉ NEGRO CON LECHE CONDENSADA + 3 MOCHIS ....... $15.00")
        print("3. COMBO 3: 2 DANGOS + MOGU ................................ $16.00")
        print("4. COMBO 4: 3 TANGHULUS + CALPIS ........................... $18.00")
        print("5. DESEO VOLVER AL MENU OPCIONES")

        quintaopcion = int(input("Por favor elija una opción: "))

        if quintaopcion >= 1 and quintaopcion <= 4:
            agregarcantidad = int(input("Agregue la cantidad de unidades deseadas: "))

            if quintaopcion == 1:
                subtotal = agregarcantidad * 19.00
            elif quintaopcion == 2:
                subtotal = agregarcantidad * 15.00
            elif quintaopcion == 3:
                subtotal = agregarcantidad * 16.00
            elif quintaopcion == 4:
                subtotal = agregarcantidad * 18.00

            saldoapagar = saldoapagar + subtotal

            print("Su combo fue agregado correctamente")
            print("Subtotal agregado: $" + str(subtotal))
            print("Saldo actual: $" + str(saldoapagar))

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar

        elif quintaopcion == 5:
            return saldoapagar
        else:
            print("Opción inválida, intente de nuevo")


def main():
    saldoapagar = 0
    primeraopcion = 0

    while primeraopcion != 5:
        print("========= MENU DE OPCIONES =========")
        print("1. MENU DE POSTRES")
        print("2. MENU DE BEBIDAS")
        print("3. MENU DE ARTICULOS")
        print("4. MENU DE COMBOS")
        print("5. FACTURAR Y SALIR")

        primeraopcion = int(input("Por favor elija una opción: "))

        if primeraopcion == 1:
            saldoapagar = menu_postres(saldoapagar)
        elif primeraopcion == 2:
            saldoapagar = menu_bebidas(saldoapagar)
        elif primeraopcion == 3:
            saldoapagar = menu_articulos(saldoapagar)
        elif primeraopcion == 4:
            saldoapagar = menu_combos(saldoapagar)
        elif primeraopcion == 5:
            if saldoapagar > 0:
                mostrar_factura(saldoapagar)
                print("Gracias por su compra")
                print("HASHIRA le agradece")
            else:
                print("NO EXISTEN ARTICULOS COMPRADOS")
        else:
            print("Opción inválida, intente de nuevo")

    print("Gracias por su visita")


if __name__ == "__main__":
    main()