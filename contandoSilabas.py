# retornar cantidad de silabas
def count(string):
    return len(string.split('-'))

    # return string.count('-')+1

    # c=1
    # return [c := c + 1 for letra in string if letra == '-'][-1]


    # for letra in string:
    #     if letra == '-':
    #         c+=1
    # return c

print(count('ho-tel'))