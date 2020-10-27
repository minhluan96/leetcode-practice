if __name__ == '__main__':
    n = int(input())

    penguinMap = {}
    for _ in range(n):
        name = input()
        if name not in penguinMap:
            penguinMap[name] = 0
        penguinMap[name] += 1

    maxValue = 0
    namePenguin = ''
    for k, v in penguinMap.items():
        if v > maxValue:
            maxValue = v
            namePenguin = k

    print(namePenguin)