lim = list(map(int, input().split()))

total = sum(lim)

half = 0

if total % 2 == 0:
    half = total // 2
else:
    half = (total + 1) // 2



print(half)

lim.sort()
sums = 0

x = 0
for d in lim:
    sums += d
    if sums > half:
        #sums -= d
        break
    x += 1

print(sums)