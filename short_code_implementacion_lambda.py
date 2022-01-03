# snake_case
#map builtins se usa para aplicar una funcion (como SUM o una anonima) a cada elemento de una lista, esta es como que tiene un FOR adentro por lo que no hace falta hacer list comprehension
# las builtins se usan con parseadores tipo lista y tupla
def convert(lista):
    return list(map(str,lista))
    # return list(map(lambda numero: str(numero), lista))
    # return [str(numero) for numero in lista]

print(convert([1,2,3]))


# Se realiza la misma funcion pero lambda
lista = lambda param: list(map(str,param))
print(lista([1,2,3]))