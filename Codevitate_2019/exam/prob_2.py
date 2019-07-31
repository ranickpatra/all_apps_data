T = int(input())
n1, n2 = map(int, input().split())

print(n1, n2)


def calc():
    
    return



if n1 % 2 == 0:
    if n2 % 2 == 0:
        print("2")
    else:
        calc()
else:
    if n2 % 2 == 1:
        print("1")
    else:
        calc()