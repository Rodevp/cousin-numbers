#Parsea los numeros a enteros
def convert_to_integers( list_of_numbers ) :
    list_numbers_integers = []
    for number in list_of_numbers :
        number = int( number )
        list_numbers_integers.append( number )
    
    return list_numbers_integers