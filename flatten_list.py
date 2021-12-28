#aplanar listas

def flatten(listaDeListas):
    return [listita for lista in listaDeListas for listita in lista]

    # listaAplanada=[]
    # for lista in listaDeListas:
    #     for listita in lista:
    #         listaAplanada.append(listita)
    # return listaAplanada

    # listaAplanada=[]
    # for lista in listaDeListas:
    #     listaAplanada.extend(lista)
    # return listaAplanada

print(flatten([[1,2],["as","dsa"]]))
