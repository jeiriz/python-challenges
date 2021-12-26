# snake_case
#return true if both numbers are integers
def only_ints(x,y):
    return type(x) == int and type(y) == int
    # return True if type(x) == type(1) and type(y) == type(1) else False


#     if type(x) == type(1) and type(y) == type(1):
#         return True
#     else:
#         return False

print(only_ints(1,"s")) 