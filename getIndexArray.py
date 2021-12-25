# Devuelve una lista con los indices que contienen letras capitales (mayusculas)
def capital_indexes(string):
    # la primera I significa que es el resultado, es el output, es lo que se quiere obtener siempre y cuando l sea upper
    # el I del principio es igual a indexArrat.append(indice)
    # se crea un nuevo array 
    return [i for i,l in enumerate(string) if l.isupper()]
    
    # La comprensión de listas ofrece una sintaxis más corta cuando se desea crear una nueva lista basada en los valores de una lista existente.
    #    for indice,letra in enumerate(string):
#        if letra.isupper():
#            indexArray.append(indice)


# should return [0, 1,3]
print(capital_indexes ("TEsT"))
