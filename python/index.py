import re

futbol = "Se suspende los partidos de futbol por 10 dias, en vez de futbol haremos gimnasia funcional en casa"
letra = "e"
palabras = futbol.split(" ")


def principal(): 
    cantidadLetras = len(futbol)
    print (cantidadLetras)

principal()



def cantidadLetraE() :
    contador = 0
    for elemento in futbol:
        if elemento == letra:
            contador = contador + 1
    return contador

contador = cantidadLetraE()

print("la letra", letra, "se repite", contador, "veces")



frecuenciaPalabras = [palabras.count(futbol) for futbol in palabras]
print("repite palabras: ", frecuenciaPalabras)
print(str(list(zip(palabras, frecuenciaPalabras))))


patron = "futbol"

resultado = re.sub(patron, "voley", futbol)
print(resultado)



