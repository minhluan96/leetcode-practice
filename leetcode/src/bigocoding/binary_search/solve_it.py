import math


def f(x):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * pow(x, 2) + u


if __name__ == '__main__':
    eps = pow(10, -9)

    while True:
        try:
            p, q, r, s, t, u = map(float, input().split())

            left = 0
            right = 1
            ans = 0

            if f(0) * f(1) > eps:
                print('No solution')
                continue

            while abs(left - right) > eps:
                mid = (left + right) / 2

                if f(left) * f(mid) <= 0:
                    right = mid
                else:
                    left = mid

            print('{0:.4f}'.format(left))
        except EOFError:
            break
