# Devuelve la suma de los valores del array
def sumar(arrayNumeros):
    sum = 0
    return ([sum := sum + num for num in arrayNumeros][-1])
    # return [i for i in range(len(arrayNumeros)) if arrayNumeros[i].isupper()] -> error

    # for numero in arrayNumeros:
    #     sum+=numero
    # print(sum)
    # return sum

print(sumar([1,2,3,4]))

