import bisect

class Solution:

    def bs(self, left, right, query):
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] == query:
                return mid
            if nums[mid] > query:
                return self.bs(left, mid - 1, query)
            return self.bs(mid + 1, right, query)
        return -1


if __name__ == '__main__':
    case = 1
    while True:
        N, Q = map(int, input().split())
        if N == 0 and Q == 0:
            break

        print('CASE# {}:'.format(case))
        case += 1
        nums = []

        for i in range(N):
            nums.append(int(input()))

        solution = Solution()
        nums.sort()

        for _ in range(Q):
            query = int(input())
            ans = solution.bs(0, len(nums) - 1, query)
            if ans != -1:
                pos = bisect.bisect_left(nums, query, 0, len(nums))
                print('{} found at {}'.format(query, pos + 1))
            else:
                print('{} not found'.format(query))