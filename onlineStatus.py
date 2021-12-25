# Funcion que muestra la cantidad de personas online
def online_count (dictionary):
    return len([list for i in dictionary if dictionary[i]=='online'])
    # return len([list for k,status in dictionary.items() if status=='online'])

    # lista=[]
    # for name,status in dictionary.items():
    #     if status=='online':
    #         lista.append(status)
    # return len(lista)
    
    # for name,status in dictionary.items():
    #     if status == "online":
    #         contador+=1
    # return contador

    # return [contador:= contador +1 for i,k in enumerate(dictionary) if dictionary[k]=="online"][-1]
    # for i,k in enumerate(dictionary):
    #     if dictionary[k] == "online":
    #         contador+=1
    # return contador 

    #  for person, status in people.items():


print(online_count({
    "juan":"online",
    "nico":"offline",
    "julian":"online"
    }))
