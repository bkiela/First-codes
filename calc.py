import math

type_of_calculation = int(input(""" 
 1. Addition 
 2. Substraction 
 3. Multiplication
 4. Devision
 5. Power
 6. Square Root
 Enter what type of calculation would you like to do: """))

if type_of_calculation == 6:
    num_1 = float(input("Enter the number you would like to get square root of: "))
elif type_of_calculation > 6:
    print("You need to select from numbers between 1 and 6")
else:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

if type_of_calculation == 1:
    print(f"Result of your addidtion is: {num_1+num_2}")
elif type_of_calculation == 2:
    print(f"Result of your substraction is: {num_1-num_2}")
elif type_of_calculation == 3:
    print(f"Result of your multiplication is: {num_1*num_2}")
elif type_of_calculation == 4:
    print(f"Result of your devision is: {num_1/num_2}")
elif type_of_calculation == 5:
    print(f"Result of your power is: {num_1**num_2}")
elif type_of_calculation == 6:
    print(f"Result of your square root is: {math.sqrt(num_1)}")

