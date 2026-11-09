class Producto:

    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def a_linea(self):
        return f"{self.codigo};{self.nombre};{self.categoria};{self.precio:.2f}"

    @staticmethod
    def desde_linea(linea):
        partes = linea.strip().split(";")
        if len(partes) != 4:
            raise ValueError("Línea con formato incorrecto")
        return Producto(int(partes[0]), partes[1].strip(),
                        partes[2].strip(), float(partes[3]))

    def __str__(self):
        return f"║{self.codigo:<4}{self.nombre:<20}S/{self.precio:<12.2f}║"
