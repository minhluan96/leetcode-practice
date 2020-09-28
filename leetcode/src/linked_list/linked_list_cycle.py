class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
        O(n) time complexity
        O(n) space complexity
    '''

    def hasCycle(self, head: ListNode) -> bool:
        node_arr = []

        while head:
            if head in node_arr:
                return True

            node_arr.append(head)
            head = head.next

        return False 

class Solution2:

    '''
        Time complexity O(n)
        Space complexity O(1)
    '''
    def hasCycle(self, head: ListNode) -> bool:
        
        min_value = float('-inf')
        
        while head:
            if head.val == min_value:
                return True

            head.val = min_value
            head = head.next

        return False

class Solution3:
    '''
        Slow runner & Fast runner
        Time complexity:
            If list has no cycle: O(n)
            If list has cycle: The best case is O(n) and the worst case is O(n + k) = O(n)
        
        Space complexity O(1) since we only used slow and fast pointer
    '''
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = b

solution = Solution3()
result = solution.hasCycle(a)
print(result)         
