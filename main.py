from gestion_productos import GestionProductos


def main():
    gestion = GestionProductos("productos.txt")
    while True:
        print("\n===== KIOSCO =====")
        print("1.-Realizar pedido\n2.-Ver productos\n3.-Registrar producto")
        print("4.-Buscar producto\n5.-Editar producto\n6.-Eliminar producto\n0.-Salir")
        match gestion.leer_entero("Elija una opcion: "):
            case 1: gestion.realizar_pedido()
            case 2: gestion.mostrar_lista()
            case 3: gestion.registrar_producto()
            case 4: gestion.buscar_producto()
            case 5: gestion.editar_producto()
            case 6: gestion.eliminar_producto()
            case 0:
                print("Hasta luego")
                break
            case _: print("Opcion invalida")


if __name__ == "__main__":
    main()
