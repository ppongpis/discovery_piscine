import sys

#num of para
if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        #(inclusive end)
        arr = list(range(start, end + 1))
        print(arr)
    except:
        print("none")
