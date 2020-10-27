def oppoCase(c):
    if c.isupper():
        return c.lower()
    return c.upper()


if __name__ == '__main__':
    s = input()
    t = input()

    tMap = {}
    sMap = {}

    for c in t:
        if c not in tMap:
            tMap[c] = 0
        tMap[c] += 1

    for c in s:
        if c not in sMap:
            sMap[c] = 0
        sMap[c] += 1

    whoops = 0
    yay = 0

    for c in s:
        if c in tMap:
            tmp = min(sMap[c], tMap[c])
            yay += tmp
            sMap[c] -= tmp
            tMap[c] -= tmp

    for c in s:
        if oppoCase(c) in tMap:
            tmp = min(sMap[c], tMap[oppoCase(c)])
            whoops += tmp
            sMap[c] -= tmp
            tMap[oppoCase(c)] -= tmp

    print('{} {}'.format(yay, whoops))

