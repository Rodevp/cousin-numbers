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



#crea un diccionario con el numero y sus posibles divisores
def  factors_of_numbers( list_of_numbers ) :
    numbers_list = convert_to_integers(list_of_numbers)
    number_and_factors = {}
    for number in numbers_list:
        if number != 0 : 
            list_dividers = all_you_factors(number)
            number_and_factors[ str( number ) ] = list_dividers
            number = number - 1
    
    return number_and_factors


#determina si el numero es primo o no
def is_cousins( numbers_and_dividers = {} ) :
    list_of_counsin = []
    for number, factors in numbers_and_dividers.items() :
        if len(factors) == 2 :
            list_of_counsin.append( int(number) )
    
    return list_of_counsin



##busca si es natural
def is_natural( list_numbers ) : 

    list_numbers_natural = []

    for number in list_numbers :
        if number > 0 :
            list_numbers_natural.append(number)
    
    return list_numbers_natural
