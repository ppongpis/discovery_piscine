value = input("Give me a number: ")

number = float(value)

if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
