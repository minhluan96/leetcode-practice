import math


if __name__ == '__main__':
    n, s = map(int, input().split())

    cityMap = {}
    population = [0] * n
    MAX_CAPACITY = int(1e6)

    for i in range(n):
        x, y, k = map(int, input().split())
        dis = math.sqrt(pow(x, 2) + pow(y, 2))
        cityMap[i] = dis
        population[i] = k

    sumPopulation = sum(population)
    total = s
    if total + sumPopulation < MAX_CAPACITY:
        print(-1)
    else:
        sortedCityMap = dict(sorted(cityMap.items(), key=lambda x: x[1]))

        minPos = -1
        printed = False

        for k, v in sortedCityMap.items():
            if total >= MAX_CAPACITY:
                print(sortedCityMap[minPos])
                exit()
            else:
                total += population[k]
                minPos = k

        if total >= MAX_CAPACITY:
            print(sortedCityMap[minPos])
        else:
            print(-1)


