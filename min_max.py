# retornar la diferencia entre el numero mas grande y el numero mas chico
# la dif entre build in y data type functions es que las build in no se acceden con punto
#para saber cuales son las builtins, importar y realizar dir(builtins)

def largest_difference(listaDeNumeros):
    return max(listaDeNumeros) - min(listaDeNumeros)

    # listaDeNumeros.sort()
    # max=listaDeNumeros[-1]
    # min=listaDeNumeros[0]
    # return max-min

    # max=0
    # min=999
    # for numero in listaDeNumeros:
    #     if numero > max:
    #         max = numero
    #     if numero < min:
    #         min = numero
    # return max - min

print(largest_difference([1,3,4,9,30, -4]))
