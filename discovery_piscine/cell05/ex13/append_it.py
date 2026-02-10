import sys

args = sys.argv[1:]

# if no parameters
if len(args) == 0:
    print("none")
else:
    for word in args:
        # skip if already ends with "ism"
        if not word.endswith("ism"):
            print(word + "ism")
