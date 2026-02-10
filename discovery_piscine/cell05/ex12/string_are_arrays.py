import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]
    result = ""

    for c in text:
        if c == 'z':
            result += 'z'

    if result == "":
        print("none")
    else:
        print(result)
