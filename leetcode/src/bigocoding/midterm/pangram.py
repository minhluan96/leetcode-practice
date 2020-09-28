class Solution:
    def pangram(self, s):

        characterFrequency = {}
        lowerS = s.lower()

        for c in lowerS:
            if 'a' <= c <= 'z':
                if c not in characterFrequency:
                    characterFrequency[c] = 0
                characterFrequency[c] += 1

        return len(characterFrequency) == 26


if __name__ == '__main__':
    n = int(input())
    s = input()
    solution = Solution()
    result = solution.pangram(s)
    if result:
        print('YES')
    else:
        print('NO')