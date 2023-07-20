import numpy as np
ROMANOS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToArabic(roman):
    letras = list(roman)

    before = 0
    sum = 0
    for i in reversed(letras):
        if(before <= ROMANOS[i]):
            sum += ROMANOS[i]
        else:
            sum -= ROMANOS[i]
        before = ROMANOS[i]
    print("%s = %i" %(roman,sum))

### EJEMPLOS ###
romano = ["XV","LDI","DCCCLXVII","CDXXXIV","DCCVLIII","DCCCLVII","DXL","CIL","III","LVIII","MCMXCIV"]

for num in romano:
    romanToArabic(num)