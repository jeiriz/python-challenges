# hacer funcion que reciba como parametro una letra y un digito
# debe retornar una tupla con el indice correspondiente (fila, columna)
# ejemplo, A3 = (2,0)
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)

    # lista = [listaLD for listaLD in ld ]
    # switch={
    #     "A":0,
    #     "B":1,
    #     "C":2,
    #     "1":0,
    #     "2":1,
    #     "3":2
    #     }
    # return tuple((switch.get(lista[1],"Not valid"),switch.get(lista[0].upper(),"Not valid")))
    
print(get_row_col("B1"))
