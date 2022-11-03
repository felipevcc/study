"""
https://es.acervolima.com/programa-de-python-para-convertir-numeros-enteros-a-romanos/

Se resuelve haciendo el proceso simulando una division 

div = numero que se va colocando en el cociente 
number = al resto que va generando cada cociente

"""

# Function to convert integer to Roman values
def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
  
# Driver code
if __name__ == "__main__":
    number = 3549
    print("Roman value is:", end = " ")
    printRoman(number)
