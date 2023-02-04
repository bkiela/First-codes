import math

print(""" 
1. Addition 
2. Substraction 
3. Multiplication
4. Devision
5. Power
6. Square Root
Enter what type of calculation would you like to do: """)

type_of_calculation = int(input().strip())
if type_of_calculation not in [1, 2, 3, 4, 5, 6]:
    print("You need to select from numbers between 1 and 6")
    exit()

num_1 = float(input("Enter the first number: "))
if type_of_calculation == 6:
    num_2 = None
else:
    num_2 = float(input("Enter the second number: "))

if type_of_calculation == 1:
    result = num_1 + num_2
elif type_of_calculation == 2:
    result = num_1 - num_2
elif type_of_calculation == 3:
    result = num_1 * num_2
elif type_of_calculation == 4:
    result = num_1 / num_2
elif type_of_calculation == 5:
    result = num_1 ** num_2
else:
    result = math.sqrt(num_1)

calculation_types = ["addition", "subtraction", "multiplication", "division", "power", "square root"]
print(f"Result of your {calculation_types[type_of_calculation-1]} is: {result}")
