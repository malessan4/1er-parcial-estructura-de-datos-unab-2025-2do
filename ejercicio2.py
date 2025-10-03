class Propiedad:
    def __init__(self, codigo, direccion, tipo, ambientes, precio, estado, premium):
        self.codigo = codigo
        self.direccion = direccion
        self.tipo = tipo
        self.ambientes = ambientes
        self.precio = precio
        self.estado = estado
        self.premium = premium

    def __str__(self):
        premium_str = "Premium" if self.premium else "Standard"
        return f"Código: {self.codigo}, Dirección: {self.direccion}, Tipo: {self.tipo}, Ambientes: {self.ambientes}, Precio: ${self.precio}, Estado: {self.estado}, {premium_str}"

class Inmobiliaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = []

    def agregar_propiedad(self, propiedad):
        self.propiedades.append(propiedad)
        print("Propiedad agregada exitosamente.")

    def buscar_por_tipo(self, tipo):
        print(f"Propiedades del tipo: {tipo}")
        for p in self.propiedades:
            if p.tipo.lower() == tipo.lower():
                print(p)


    def buscar_por_precios(self, precio):
        print(f"Propiedades de precio menor a: {precio}")
        for i in self.propiedades:
            if i.precio <= precio:
                print(i)

    
    def promocion_premium(self):
        print("Propiedades en promocion")
        for j in self.propiedades:
            if j.premium == True :
                print(j)



# Ejemplo de Uso

inmobiliaria = Inmobiliaria("Inmobiliaria Central")
p1 = Propiedad(1, "Calle 123", "Casa", 3, 150000, "Disponible", True)
p2 = Propiedad(2, "Avenida 456", "Departamento", 2, 90000, "Vendido", False)   
p3 = Propiedad(3, "Boulevard 789", "Casa", 4, 200000, "Disponible", False)

inmobiliaria.agregar_propiedad(p1)
inmobiliaria.agregar_propiedad(p2)
inmobiliaria.agregar_propiedad(p3)

inmobiliaria.buscar_por_tipo("Casa")    
inmobiliaria.buscar_por_precios(160000)
inmobiliaria.promocion_premium()
