roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} 

def converter(rom_num):

    acum = 0
    prev_num = None
    start_resta = False

    for i in range(len(rom_num)-1,-1,-1):

        x = roman[rom_num[i]]

        if prev_num == None:
            acum = x
            prev_num = x
            continue

        if x > prev_num:
            acum += x
            start_resta = False 
        elif x < prev_num:
            acum -= x
            start_resta = True 
        elif x == prev_num and start_resta == True:
            acum -= x 
        elif x == prev_num and start_resta == False:
            acum += x
        
        prev_num = x

    return acum 
        
print(converter("MDCCCLXXXIV"))
#1884

print(converter("MCMXCIV"))
