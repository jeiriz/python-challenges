# devolver true si los 2 strings son anagramas
def count_letters(string):
    # a cada key (l), le voy a agregar un value que sera lo que ponga luego del 2 puntos
    return {l: string.count(l) for l in string}

    # dict={}
    # for letra in string:
    #     c=0
    #     if letra in dict:
    #         c=dict[letra]
    #         dict[letra]=c+1
    #     c+=1
    #     dict[letra]=c
    # return dict

print(count_letters("hooola"))

def is_anagram(string1,string2):
    return count_letters(string1) == count_letters(string2)
    
    
    # if len(string1) == len(string2):
    #     lista1 = [letra1 for letra1 in string1]
    #     lista2 = [letra2 for letra2 in string2]
    #     lista1.sort()
    #     lista2.sort()  -> esta utiliza una funcion de una lista
    #     return lista1 == lista2
    # return False


    # return sorted(string1) == sorted(string2) #esta utiliza una buildin function, crea una lista con valores ordenados

print(is_anagram("olah","hola"))
            