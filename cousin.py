#Parsea los numeros a enteros
def convert_to_integers( list_of_numbers ) :
    list_numbers_integers = []
    for number in list_of_numbers :
        number = int( number )
        list_numbers_integers.append( number )
    
    return list_numbers_integers


#muestra los posibles divisores entre sus factores
def all_you_factors(number) :
    factor = 1
    list_factors_number = []
    limit = number

    while limit != 1 :
        if limit % factor == 0 :

            list_factors_number.append(factor)
            limit = limit / factor 
            factor = 1
        
        factor += 1
    
    #si no encuentra el factor como si mismo lo agrega
    if not number in list_factors_number : list_factors_number.append(number)

    return list_factors_number


