original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for n in original_array:
    new_array.append(n + 2)

print(original_array)
print({x for x in new_array if x  >=10})

