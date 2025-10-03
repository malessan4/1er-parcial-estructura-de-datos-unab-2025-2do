class Propiedad:
    def __init__(self, codigo, direccion, tipo, ambientes, precio, estado, premium):
        self.codigo = codigo
        self.direccion = direccion
        self.tipo = tipo
        self.ambientes = ambientes
        self.precio = precio
        self.estado = estado
        self.premium = premium

class Inmobiliaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = []

    def agregar_propiedad(self, propiedad):
        self.propiedades.append(propiedad)
        print("Propiedad agregada exitosamente.")

    def buscar_por_tipo(self, tipo):
        print(f"Propiedades del tipo: {self.tipo}")
        for p in self.propiedaddes:
            if p.tipo.lower() == tipo.lower():
                print(p)

    def buscar_por_precios(self, precio):
        print(f"Propiedades de precio menor a: {self.precio}")
        for i in self.propiedades:
            if i.precio <= precio:
                print(i)



# Ejemplo de Uso

inmobiliaria = Inmobiliaria("Inmobiliaria Central")