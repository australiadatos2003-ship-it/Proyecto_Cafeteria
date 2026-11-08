print("╔══════════════════════════════════════╗")
print("║      LISTA DE PRODUCTOS X COSTO      ║")
print("╠══════════════════════════════════════╣")
print("║1.Oreo                   S/1.20       ║")
print("║2.Margarita              S/1.00       ║")
print("║3.Picara                 S/1.50       ║")
print("║4.Arroz con pollo        S/12.00      ║")
print("║5.Broaster               S/15.00      ║")
print("║6.Causa                  S/14.00      ║")
print("║7.Agua                   S/1.00       ║")
print("║8.Gaseosa                S/2.00       ║")
print("║9.Refresco               S/1.50       ║")
print("║10.Empanada              S/6.00       ║")
print("║11.Pan con pollo         S/5.00       ║")
print("║12.Torta                 S/8.00       ║")
print("╚══════════════════════════════════════╝")
nombre=input("Cual es tu nombre: ")
while True:
    n=int(input("Cuantos pedidos deseas hacer: "))
    if n > 0:
        break
    else:
        print("Introduzca un valor superior a 0")
coste_u = 0
coste = 0
detalle_pedido= ""
efec = 0
for k in range(n):
    print(f"PEDIDO N°{k+1}")
    print("1.-Bocadillos \n2.-Platos a la carta \n3.-Bebidas \n4.-Postres")
    while True:
        opc_pedido=int(input("Selecciona que categoria: "))
        match opc_pedido:
            case 1:
                print("1.-Oreo(S/1.20) \n2.-Margarita(S/1.00) \n3.-Picaras(S/1.50)")
                p_bocadillo = ""
                while True:
                    p_bocadillo=int(input("Elige tu bocadillo: "))
                    match p_bocadillo:
                        case 1:
                            bocadillo = "Oreo"
                            p_u_b= 1.20
                            break
                        case 2:
                            bocadillo = "Margarita"
                            p_u_b= 1.00
                            break
                        case 3:
                            bocadillo ="Picara"
                            p_u_b= 1.50
                            break
                        case _:
                            print("opcion invalida")
                cantidad=int(input(f"Cuantas {bocadillo}s deseas: "))
                coste +=cantidad*p_u_b
                coste_u = cantidad*p_u_b
                detalle_pedido+=f"\n║{bocadillo:<15} x{cantidad:<6} S/{coste_u:<12.2f}║"
                break
            case 2:
                print("1.-Arroz con pollo(S/12.00) \n2.-Broaster(S/15.00) \n3.-Causa(S/14.00)")
                p_plato = ""
                while True:
                    p_plato=int(input("Elige tu plato: "))
                    match p_plato:
                        case 1:
                            plato = "Arroz con pollo"
                            p_u_pl= 12.00
                            break
                        case 2:
                            plato="Broaster"
                            p_u_pl= 15.00
                            break
                        case 3:
                            plato = "Causa"
                            p_u_pl= 14.00              
                            break        
                        case _:
                            print("opcion invalida")                       
                cantidad=int(input(f"Cuantos {plato} deseas: "))
                coste += cantidad*p_u_pl
                coste_u = cantidad*p_u_pl
                detalle_pedido+=f"\n║{plato:<15} x{cantidad:<6} S/{coste_u:<12.2f}║"
                break
            case 3:
                print("1.-Agua(S/1.00) \n2.-Gaseosa(S/2.00) \n3.-Refresco(S/1.50)")
                p_bebidas = ""
                while True:
                    p_bebidas=int(input("Elige tu bebida: "))
                    match p_bebidas:
                        case 1:
                            bebida= "Agua"
                            p_u_be= 1.00
                            break
                        case 2:
                            bebida= "Gaseosa"
                            p_u_be= 2.00
                            break
                        case 3: 
                            bebida="Refresco"
                            p_u_be= 1.50
                            break
                        case _:
                            print("opcion invalida")
                cantidad=int(input(f"Cuantas {bebida} deseas: "))
                coste += cantidad*p_u_be
                coste_u = cantidad*p_u_be
                detalle_pedido +=f"\n║{bebida:<15} x{cantidad:<6} S/{coste_u:<12.2f}║"
                break
            case 4:
                print("1.-Empanada(S/6.00) \n2.-Pan con pollo(S/5.00) \n3.-Torta(S/8.00)")
                p_postre = ""
                while True:
                    p_postre=int(input("Elige tu postre: "))
                    match p_postre:
                        case 1:
                            postre="Empanada"
                            p_u_pos= 6.00
                            break
                        case 2:
                            postre="Pan con pollo"
                            p_u_pos= 5.00
                            break
                        case 3:
                            postre="Torta"
                            p_u_pos= 8.00
                            break
                        case _:
                            print("opcion invalida")
                cantidad=int(input(f"Cuantas {postre}s deseas: "))
                coste += cantidad*p_u_pos
                coste_u = cantidad*p_u_pos
                detalle_pedido +=f"\n║{postre:<15} x{cantidad:<6} S/{coste_u:<12.2f}║"
                break
            case _:
                print("Opcion invalida")
print("Metodo de pago: \n1.-Efectivo \n2.-Tarjeta \n3.-Yape")
while True:
    metodo=int(input("Elija su metodo de pago: "))
    if metodo == 1:
        metodo = "Efectivo"
        efec=float(input("Con cuanto efectivo va a pagar: "))
        if efec < coste:
            print("No tiene efectivo suficiente para realizar la compra")
            exit()
        break
    elif metodo == 2:
        metodo = "Tarjeta"
        break
    elif metodo == 3:
        metodo = "Yape"
        break
    else:
        print("Metodo de pago no reconocido")
vuelto = efec - coste
print("╔══════════════════════════════════════╗")
print(f"║            BOLETA DE PAGO            ║")
print("╠══════════════════════════════════════╣")
print(f"║Metodo de pago: {metodo:<22}║")
print(f"║Nombre del comprador: {nombre:<16}║")
print(f"║Detalles de compra:                   ║ {detalle_pedido} ")
print(f"║Monto total:            S/{coste:<12.2f}║")
if metodo == "Efectivo":
    if efec > coste:
        print(f"║vuelto de pago:         S/{vuelto:<12.2f}║")
        print("╚══════════════════════════════════════╝")
    elif efec == coste:
        print("╚══════════════════════════════════════╝")
else:
    print("╚══════════════════════════════════════╝")
