first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
solution = first*second
print(f"{first} x {second} = {solution}")
if solution == 0:
	print("The result is positive and negative")
elif solution > 0:
	print("The result is positive")
elif solution < 0:
	print("The result is negative")
