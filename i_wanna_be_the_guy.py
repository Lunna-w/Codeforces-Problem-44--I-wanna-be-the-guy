m = int(input())

y = list(map(int, input().split()))
x = list(map(int, input().split()))

yarr = y[1:]
xarr = x[1:]

ly = len(yarr)
xy = len(xarr)

joined_arr = yarr + xarr

xxy = len(joined_arr)

if all(i in joined_arr for i in range(1, m + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")