# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

a = ListNode(1)
b = ListNode(1)
c = ListNode(2)

a.next = b
b.next = c

solution = Solution()
result = solution.deleteDuplicates(a)

while result:
    print(result.val)
    result = result.next