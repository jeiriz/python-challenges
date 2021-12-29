# hacer una funcion que determine si el numero es divisible por 3.
#divisiblle por 3 significa que la suma de las cifras del numero, tiene que ser multiple de 3, es decir
# que al dividir el numero por 3, da un tipo de dato entero y no float

def div_3(number):
    return number%3 == 0

print(div_3(540))

