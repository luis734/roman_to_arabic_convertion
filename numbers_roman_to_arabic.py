# Dictionary of Roman numbers and its Arabic value
ROMAN = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToArabic(number):
    
    # Split the string into single items
    letter = list(number)

    # Variable to save the digit on the right
    before = 0

    # Cumulative sum of each number
    sum = 0

    # Doing the iteration on the letters backwards to avoid special cases
    for i in reversed(letter):
        # If the number on the right is greater than or equal, add it
        if(before <= ROMAN[i]):
            sum += ROMAN[i]
        # If the number on the right is less, subtract it
        else:
            sum -= ROMAN[i]
        before = ROMAN[i]

    print("%s = %i" %(number,sum))

### EXAMPLES ###
roman = ["XV","LDI","DCCCLXVII","CDXXXIV","DCCVLIII","DCCCLVII","DXL","CIL","III","LVIII","MCMXCIV","CLIX"]

# Sending the examples to the function
for num in roman:
    romanToArabic(num)