# check if the string have the same two letters in a row
def double_letters(string):    
    return any([a==b for a,b in zip(string,string[1:])])
    
    # list=[]
    # for a,b in zip(string,string[1:]):
    #     list.append(a==b)
    # return any(list)

    # return [True for i,letra in enumerate(string) if letra==string[i-1]]

    # for i,letra in enumerate(string):
    #     if i !=0:
    #         if letra == string[i-1]:
    #             return True
    # return False


    # ulti=""
    # for i in string:
    #     if ulti=="":
    #         ulti=i
    #     else:
    #         if i == ulti:
    #             return True
    #         else:
    #             ulti=i
    # return False


print(double_letters("hola"))    