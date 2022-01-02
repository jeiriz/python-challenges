# dado un string con valores binarios, retornar la cantidad maxima de zeros consecutivos
# def consecutive_zeros(string):
#     lista=[]
#     backup=[]
#     for num in string:
#         if num=="0":
#             lista.append(num)
#         else:
#             if len(backup) < len(lista):
#                 backup.clear()
#                 backup.extend(lista)
#             lista.clear()
#     return len(lista) if len(lista) > len(backup) else len(backup)


def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
    # result = 0
    # streak = 0
    # for letter in bin_str:
    #     if letter == "0":
    #         streak += 1
    #     else:
    #         streak = 0
    #     result = max(result, streak)
    # return result

print(consecutive_zeros("111001010000110000010010"))
