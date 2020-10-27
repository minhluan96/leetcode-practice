if __name__ == '__main__':
    t = int(input())

    input()

    for _ in range(t):
        treeFrequency = {}
        counter = 0

        while True:
            try:
                name = input()
                if len(name) == 0:
                    break
                if name not in treeFrequency:
                    treeFrequency[name] = 0
                treeFrequency[name] += 1
                counter += 1
            except EOFError:
                break

        sortedTreeFrequency = dict(sorted(treeFrequency.items(), key=lambda x: x[0].lower()))

        for k, v in sortedTreeFrequency.items():
            percentage = v / counter * 100
            print('{} {:.4f}'.format(k, percentage))

        print()


