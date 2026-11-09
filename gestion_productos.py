from producto import Producto

CATEGORIAS = ["Bocadillos", "Platos a la carta", "Bebidas", "Postres"]

PRODUCTOS_INICIALES = [
    ("Oreo", 0, 1.20), ("Margarita", 0, 1.00), ("Picara", 0, 1.50),
    ("Arroz con pollo", 1, 12.00), ("Broaster", 1, 15.00), ("Causa", 1, 14.00),
    ("Agua", 2, 1.00), ("Gaseosa", 2, 2.00), ("Refresco", 2, 1.50),
    ("Empanada", 3, 6.00), ("Pan con pollo", 3, 5.00), ("Torta", 3, 8.00),
]


class GestionProductos:

    def __init__(self, archivo="productos.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar()
        if not self.productos:         
            self.cargar_por_defecto()
            self.guardar()

    @staticmethod
    def leer_entero(mensaje, minimo=None):
        while True:
            try:
                valor = int(input(mensaje))
                if minimo is not None and valor < minimo:
                    print(f"Introduzca un valor mayor o igual a {minimo}")
                    continue
                return valor
            except ValueError:
                print("Debe ingresar un número entero")

    @staticmethod
    def leer_decimal(mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Debe ingresar un número")

    @staticmethod
    def elegir_categoria():
        for i, cat in enumerate(CATEGORIAS, 1):
            print(f"{i}.-{cat}")
        while True:
            opc = GestionProductos.leer_entero("Selecciona que categoria: ")
            if 1 <= opc <= len(CATEGORIAS):
                return CATEGORIAS[opc - 1]
            print("Opcion invalida")

    def cargar_por_defecto(self):
        for nombre, idx_cat, precio in PRODUCTOS_INICIALES:
            self.registrar(nombre, CATEGORIAS[idx_cat], precio, guardar=False)

    def cargar(self):
        self.productos = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip():
                        self.productos.append(Producto.desde_linea(linea))
        except FileNotFoundError:
            pass
        except ValueError:
            print("Aviso: el archivo tiene datos dañados, se omitió su contenido.")
            self.productos = []

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for p in self.productos:
                f.write(p.a_linea() + "\n")

    def generar_codigo(self):
        return max((p.codigo for p in self.productos), default=0) + 1

    def registrar(self, nombre, categoria, precio, guardar=True):
        nombre = nombre.strip().title()
        if not nombre or precio <= 0 or categoria not in CATEGORIAS:
            return None
        if any(p.nombre.lower() == nombre.lower() for p in self.productos):
            return None                  # ya existe
        producto = Producto(self.generar_codigo(), nombre, categoria, precio)
        self.productos.append(producto)
        if guardar:
            self.guardar()
        return producto

    def buscar_por_codigo(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def buscar_por_nombre(self, texto):
        texto = texto.strip().lower()
        return [p for p in self.productos if texto in p.nombre.lower()]

    def listar_por_categoria(self, categoria):
        return [p for p in self.productos if p.categoria == categoria]

    def editar(self, codigo, nombre=None, precio=None):
        p = self.buscar_por_codigo(codigo)
        if p is None:
            return False
        if nombre:
            p.nombre = nombre.strip().title()
        if precio is not None:
            if precio <= 0:
                return False
            p.precio = precio
        self.guardar()
        return True

    def eliminar(self, codigo):
        p = self.buscar_por_codigo(codigo)
        if p is None:
            return False
        self.productos.remove(p)
        self.guardar()
        return True

    def registrar_producto(self):
        categoria = self.elegir_categoria()
        nombre = input("Nombre del producto: ")
        precio = self.leer_decimal("Precio: S/")
        p = self.registrar(nombre, categoria, precio)
        print(f"Producto registrado con codigo {p.codigo}" if p
            else "No se pudo registrar (datos invalidos o producto repetido)")

    def buscar_producto(self):
        texto = input("Buscar por codigo o nombre: ").strip()
        if texto.isdigit():
            p = self.buscar_por_codigo(int(texto))
            resultados = [p] if p else []
        else:
            resultados = self.buscar_por_nombre(texto)
        self.mostrar_lista(resultados, "RESULTADOS")

    def editar_producto(self):
        codigo = self.leer_entero("Codigo del producto a editar: ")
        p = self.buscar_por_codigo(codigo)
        if p is None:
            print("Producto no encontrado")
            return
        nombre = input(f"Nuevo nombre ({p.nombre}) [Enter = mantener]: ")
        precio_txt = input(f"Nuevo precio ({p.precio:.2f}) [Enter = mantener]: ").strip()
        try:
            precio = float(precio_txt) if precio_txt else None
        except ValueError:
            print("Precio invalido")
            return
        print("Producto actualizado" if self.editar(codigo, nombre, precio)
            else "No se pudo actualizar")

    def eliminar_producto(self):
        codigo = self.leer_entero("Codigo del producto a eliminar: ")
        print("Producto eliminado" if self.eliminar(codigo) else "Producto no encontrado")

    def mostrar_lista(self, lista=None, titulo="LISTA DE PRODUCTOS X COSTO"):
        lista = self.productos if lista is None else lista
        print("╔" + "═" * 38 + "╗")
        print(f"║{titulo:^38}║")
        print("╠" + "═" * 38 + "╣")
        if not lista:
            print(f"║{'(sin productos)':^38}║")
        for p in lista:
            print(p)
        print("╚" + "═" * 38 + "╝")

    def tomar_pedido(self):
        n = self.leer_entero("Cuantos pedidos deseas hacer: ", 1)
        detalle, total = [], 0
        for k in range(n):
            print(f"PEDIDO N°{k + 1}")
            categoria = self.elegir_categoria()
            opciones = self.listar_por_categoria(categoria)
            if not opciones:
                print("No hay productos en esta categoria")
                continue
            for p in opciones:
                print(f"{p.codigo}.-{p.nombre}(S/{p.precio:.2f})")
            while True:
                producto = self.buscar_por_codigo(self.leer_entero("Elige tu producto (codigo): "))
                if producto and producto.categoria == categoria:
                    break
                print("opcion invalida")
            cantidad = self.leer_entero(f"Cuantos(as) {producto.nombre} deseas: ", 1)
            subtotal = cantidad * producto.precio
            total += subtotal
            detalle.append((producto.nombre, cantidad, subtotal))
        return detalle, total

    @staticmethod
    def elegir_pago(total):
        print("Metodo de pago: \n1.-Efectivo \n2.-Tarjeta \n3.-Yape")
        while True:
            opc = GestionProductos.leer_entero("Elija su metodo de pago: ")
            if opc == 1:
                while True:
                    efec = GestionProductos.leer_decimal("Con cuanto efectivo va a pagar: ")
                    if efec >= total:
                        return "Efectivo", efec
                    print("No tiene efectivo suficiente para realizar la compra")
            elif opc == 2:
                return "Tarjeta", 0
            elif opc == 3:
                return "Yape", 0
            print("Metodo de pago no reconocido")

    @staticmethod
    def imprimir_boleta(nombre, detalle, total, metodo, efec):
        linea = lambda texto: print(f"║{texto:<38}║")
        print("╔" + "═" * 38 + "╗")
        print(f"║{'BOLETA DE PAGO':^38}║")
        print("╠" + "═" * 38 + "╣")
        linea(f"Metodo de pago: {metodo}")
        linea(f"Nombre del comprador: {nombre[:16]}")
        linea("Detalles de compra:")
        for nom, cant, sub in detalle:
            print(f"║{nom:<15.15} x{cant:<6} S/{sub:<12.2f}║")
        linea(f"Monto total:            S/{total:.2f}")
        if metodo == "Efectivo" and efec > total:
            linea(f"vuelto de pago:         S/{efec - total:.2f}")
        print("╚" + "═" * 38 + "╝")

    def realizar_pedido(self):
        self.mostrar_lista()
        nombre = input("Cual es tu nombre: ")
        detalle, total = self.tomar_pedido()
        if not detalle:
            print("No se registro ningun producto.")
            return
        metodo, efec = self.elegir_pago(total)
        self.imprimir_boleta(nombre, detalle, total, metodo, efec)
