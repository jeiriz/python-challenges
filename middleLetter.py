# Devuelve la letra del medio, si no hay, devuelve vacio
def mid (string):
    # if len string % 2 == 0, return "", else return string ....
    return "" if len(string) % 2==0 else string[len(string) // 2]

print(mid("aasd"))
        