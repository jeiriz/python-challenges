# return true if all list's items are equal
def all_equal(lista):
    # for item in lista:
    #     for item2 in lista: 
    #         if item != item2:
    #             return False
    # return True
    return all([item == item2 for item in lista for item2 in lista]) #all() check if all items al true
    # c=0
    # if len(lista) == 0:
    #     return True
    # for i in range(len(lista)):
    #     if i == 0:
    #         pass
    #     else:
    #         if lista[i] == lista[i-1]:
    #             c+=1
    # return c == len(lista)-1



print(all_equal([1,1]))