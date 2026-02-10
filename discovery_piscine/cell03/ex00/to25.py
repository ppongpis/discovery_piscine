user = int(input("Enter a number less than 25\n"))
if user > 25:
	print("Error")
else:
	while user <= 25:
		print(f"Inside the loop, my variable is {user}")
		user += 1
