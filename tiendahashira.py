
def mostrar_factura(saldoapagar, **datos_cliente):
    print("::******* FACTURA*******::")

    
    if datos_cliente:
        print("---- DATOS DEL CLIENTE ----")
        for clave, valor in datos_cliente.items():
            print(f"{clave}: {valor}")

    print(f"TOTAL A PAGAR: ${saldoapagar}")
    if saldoapagar >= 1000:
        print("USTED ES GANADOR DE 5 MANGAS DE SU PREFERENCIA")
    elif saldoapagar >= 500:
        print("USTED ES GANADOR DE 75 CUPONES DE DESCUENTO")
    print("Gracias por comprar en HASHIRA")
    print("¡Esperamos verle nuevamente!")


def resumen_compras(*subtotales):
   
    print(":::::::::::: RESUMEN DE COMPRA ::::::::::::::")
    print(f"Cantidad de productos/combos agregados: {len(subtotales)}")
    total = sum(subtotales)
    print(f"Suma verificada de subtotales: ${total}")


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
                        return saldoapagar, True
                    else:
                        print("Opción inválida, intente de nuevo")
        else:
            print("Opción inválida, intente de nuevo")


def menu_postres(saldoapagar):
    subtotal_acumulado_postres = 0
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
            subtotal_acumulado_postres = subtotal_acumulado_postres + subtotal

            print("Su producto fue agregado correctamente")
            print(f"Subtotal agregado: ${subtotal}")
            print(f"Saldo actual: ${saldoapagar}")

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar, subtotal_acumulado_postres

        elif segundaopcion == 6:
            return saldoapagar, subtotal_acumulado_postres
        else:
            print("Opción inválida, intente de nuevo")


def menu_bebidas(saldoapagar):
    subtotal_acumulado_bebidas = 0
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
            subtotal_acumulado_bebidas = subtotal_acumulado_bebidas + subtotal

            print("Su bebida fue agregada correctamente")
            print(f"Subtotal agregado: ${subtotal}")
            print(f"Saldo actual: ${saldoapagar}")

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar, subtotal_acumulado_bebidas

        elif terceraopcion == 6:
            return saldoapagar, subtotal_acumulado_bebidas
        else:
            print("Opción inválida, intente de nuevo")


def menu_articulos(saldoapagar):
    subtotal_acumulado_articulos = 0
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
            subtotal_acumulado_articulos = subtotal_acumulado_articulos + subtotal

            print("Su artículo fue agregado correctamente")
            print(f"Subtotal agregado: ${subtotal}")
            print(f"Saldo actual: ${saldoapagar}")

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar, subtotal_acumulado_articulos

        elif cuartaopcion == 6:
            return saldoapagar, subtotal_acumulado_articulos
        else:
            print("Opción inválida, intente de nuevo")


def menu_combos(saldoapagar):
    subtotal_acumulado_combos = 0
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
            subtotal_acumulado_combos = subtotal_acumulado_combos + subtotal

            print("Su combo fue agregado correctamente")
            print(f"Subtotal agregado: ${subtotal}")
            print(f"Saldo actual: ${saldoapagar}")

            saldoapagar, terminar = gestionar_pedido(saldoapagar)
            if terminar:
                return saldoapagar, subtotal_acumulado_combos

        elif quintaopcion == 5:
            return saldoapagar, subtotal_acumulado_combos
        else:
            print("Opción inválida, intente de nuevo")


def main():
    saldoapagar = 0
    primeraopcion = 0

    total_postres = 0
    total_bebidas = 0
    total_articulos = 0
    total_combos = 0

    while primeraopcion != 5:
        print("========= MENU DE OPCIONES =========")
        print("1. MENU DE POSTRES")
        print("2. MENU DE BEBIDAS")
        print("3. MENU DE ARTICULOS")
        print("4. MENU DE COMBOS")
        print("5. FACTURAR Y SALIR")

        primeraopcion = int(input("Por favor elija una opción: "))

        if primeraopcion == 1:
            saldoapagar, total_postres = menu_postres(saldoapagar)
        elif primeraopcion == 2:
            saldoapagar, total_bebidas = menu_bebidas(saldoapagar)
        elif primeraopcion == 3:
            saldoapagar, total_articulos = menu_articulos(saldoapagar)
        elif primeraopcion == 4:
            saldoapagar, total_combos = menu_combos(saldoapagar)
        elif primeraopcion == 5:
            if saldoapagar > 0:
               
                nombre_cliente = input("Ingrese su nombre (opcional, Enter para omitir): ")

                if nombre_cliente != "":
                    mostrar_factura(saldoapagar, nombre=nombre_cliente)
                else:
                    mostrar_factura(saldoapagar)

                
                resumen_compras(total_postres, total_bebidas, total_articulos, total_combos)

                print("Gracias por su compra")
                print("HASHIRA le agradece")
            else:
                print("NO EXISTEN ARTICULOS COMPRADOS")
        else:
            print("Opción inválida, intente de nuevo")

    print("Gracias por su visita")


main()