#funcion que agregue puntos en el medio de las letras
def add_dots(string):
    return ".".join(string)

    # out = ""
    # for letter in string:
    #     out+=letter + "."
    # return out[:-1]
    # list=""
    # for i in range(len(string[:-1])):
    #     list+=string[i].__add__(".")
    # return list.__add__(string[-1])

print(add_dots("hola"))

#funcion que saque puntos en el medio de las letras
def remove_dots(string):
    return string.replace(".","")
    
    # out=""
    # for letter in string:
    #     if letter!=".":
    #         out+=letter
    # return out

    # s=""
    # return s.join([i for i in string if i!="."])

    # list=""
    # for i in string:
    #     if i != ".":
    #         list+=i
    # return list

print(remove_dots("h.o.l.a"))