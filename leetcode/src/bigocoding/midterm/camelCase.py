class Solution:
    def camelCase(self):
        counter = 1
        for i in range(1, len(s)):
            c = s[i]
            if c.isupper():
                counter += 1
        return counter

if __name__ == '__main__':
    s = input()

    solution = Solution()
    result = solution.camelCase()
    print(result)


