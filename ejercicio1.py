lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

def buscar_recursivo(lista_numeros, numero):
  

    # Caso Base 1: La lista está vacía. Si llegamos a esta paso, el número no se encontró.
    if not lista_numeros:
        return False

    # Caso Base 2: El primer elemento de la lista es el número que buscamos.
    if lista_numeros[0] == numero:
        return True

    # Paso Recursivo: Si no es ninguno de los casos base, 
    # llamamos a la función con el resto de la lista (todos los elementos excepto el primero).
    return buscar_recursivo(lista_numeros[1:], numero)

#Ejemplo de uso
print(f"Buscando 25: {buscar_recursivo(lista_numeros, 25)}")