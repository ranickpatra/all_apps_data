N = int(str(input("value: ")))

n_5 = N // 5 - 1
n_2 = (N - n_5*5) // 2 - 1
if N % 2 == 0 or N % 5 == 0:
    n_2 += 1
n_1 = (N - n_5*5 - n_2 * 2)

print(n_5 + n_2 + n_1)
print(n_5)
print(n_2)
print(n_1)