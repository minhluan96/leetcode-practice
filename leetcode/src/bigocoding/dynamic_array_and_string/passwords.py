class Solution:

    def calculate_waiting_time(self, effort_index, k):
        penalty = 5
        total_tries = effort_index + 1
        waiting_time = int(effort_index / k) * penalty + total_tries

        return waiting_time

    
    def passwords(self, n, k, possibles, answer):
        possibles.sort(key=len)

        answer_length = len(answer)

        best_index = -1
        worst_index = -1
        

        for i in range(len(possibles)):
            if len(possibles[i]) == answer_length and best_index == -1:
                best_index = i

            if len(possibles[i]) > answer_length and worst_index == -1:
                worst_index = i - 1

        if worst_index == -1:
            worst_index = len(possibles) - 1

        best_effort = self.calculate_waiting_time(best_index, k)
        worst_effort = self.calculate_waiting_time(worst_index, k)

        return (best_effort, worst_effort)




# first_line = list(map(int, input().split()))
# n = first_line[0]
# k = first_line[1]
# possibles = []

# for i in range(n):
#     possible = input()
#     possibles.append(possible)

# answer = input()

possibles = [
    'cba',
    'abc',
    'bb1',
    'abC',
    'ABC',
]

n = 5
k = 2
answer = 'abc'

possibles = [
    '11',
    '22',
    '1',
    '2',
]

n = 4
k = 100
answer = '22'

possibles = [
    'pine',
'kqdhmw',
'ufkszbursb',
'l',
'htalezfiosdepsgmiu',
'v',
'fkzfpno',
'lrscyyhev',
'ffaihnj',
'omvcpnncreznp',
'vnmydarmeqa',
'bzjoonknqchdp',
'qmc',
'wvtnfkggzfwdwubw',
'thhnwjyavvphw',
'bidxkeuhykdbvirebpn',
'rwuggu',
'vjslcqestszouquyfb',
'jrnknmtcjtdm',
'xoixkrdwzzz',
]

#possibles = ['l', 'v', 'qmc', 'pine', 'kqdhmw', 'rwuggu', 'fkzfpno', 'ffaihnj', 'lrscyyhev', 'ufkszbursb', 'vnmydarmeqa', 'xoixkrdwzzz']

n = 20
k = 5
answer = 'xoixkrdwzzz'

solution = Solution()
result = solution.passwords(n, k, possibles, answer)
print(result[0])
print(result[1])