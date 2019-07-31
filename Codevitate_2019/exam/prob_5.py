t = int(input())

monkey = []


def lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


def calculate_pos(mon):
    timing = []
    for i in range(len(mon)):
        desired = i
        current = i
        count = 0
        while True:
            count += 1
            current = mon[current] - 1
            if current == desired:
                timing.append(count)
                break
    filt = []
    for d in timing:
        if not d in filt:
            filt.append(d)
    mlcm = 1
    for i in filt:
        mlcm = lcm(mlcm, i)

    return mlcm



for _ in range(t):
    n = int(input())
    monkey.append(list(map(int, input().split())))


for data in monkey:
    print(calculate_pos(data))

