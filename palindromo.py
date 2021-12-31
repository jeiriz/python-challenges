# retornar true si el string es palindromo
# def palindrome(string):
    # while len(string) > 1:
    #     head = string[0]
    #     tail = string[-1]
    #     string = string[1:-1]
    #     if head != tail:
    #         return False
    # return True

# recursive solution: equivalent to the above.
# def palindrome(string):
#     if len(string) < 2:
#         return True
#     return string[0] == string[-1] and palindrome(string[1:-1])

# # smarter solution:
# # check if reversing the string gives the same string.
def palindrome(string):
    return string == string[::-1] #esto devuelve el string dado vuelta
    # stringReverse = ""
    # for letra in reversed(s):
    #     stringReverse+=letra
    # return stringReverse == s 

print(palindrome("ahsaoasha"))