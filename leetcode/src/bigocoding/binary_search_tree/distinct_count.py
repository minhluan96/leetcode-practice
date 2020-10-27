if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, X = map(int, input().split())

        nums = list(map(int, input().split()))

        num_set = set(nums)
        if len(num_set) > X:
            print('Average')
        elif len(num_set) < X:
            print('Bad')
        else:
            print('Good')