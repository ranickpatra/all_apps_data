N = int(str(input()).strip())


def fact(x):
    if x <= 0:
        return 1
    
    return x * fact(x-1)

def permutation(x, r):
    return fact(x) / fact(x - r)


def combination(x, r):
    return permutation(x, r) / fact(r)

xx = int(combination(N-1, N-2))

xx *= xx

print( xx )

