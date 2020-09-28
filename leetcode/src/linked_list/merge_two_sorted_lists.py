# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
        Brute force, time complexity O(n + m)
        space complexity, O(n)
    '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        combined_l1 = l1    
        combined_l2 = l2    
        arr = []

        while combined_l1:
            arr.append(combined_l1.val)
            if not combined_l1.next:
                break
            combined_l1 = combined_l1.next
        
        while combined_l2:
            arr.append(combined_l2.val)
            if not combined_l2.next:
                break
            combined_l2 = combined_l2.next
        
        if not len(arr): return None

        arr = sorted(arr)
        
        head = ListNode(arr[0])
        current = head

        for i in range(1, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        
        return head


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2: return None

        is_finished = False

        head = None
        current = head
        tmp = []

        node_l1 = l1
        node_l2 = l2

        while not is_finished:

            if not node_l1 and not node_l2:
                is_finished = True
                continue
            elif (node_l1 and not node_l2) or (not node_l1 and node_l2):
                existed = node_l1 if node_l1 else node_l2

                tmp.append(existed.val)
            else:    
                min_val = min(node_l1.val, node_l2.val)
                max_val = max(node_l1.val, node_l2.val)
                tmp.append(min_val)
                tmp.append(max_val)

            node_l1 = node_l1.next if node_l1 else None
            node_l2 = node_l2.next if node_l2 else None

        tmp = sorted(tmp)
        head = ListNode(tmp[0])
        current = head

        for i in range(1, len(tmp)):
            current.next = ListNode(tmp[i])
            current = current.next

        return head


class Solution3:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

a1 = ListNode(1)
b2 = ListNode(3)
c3 = ListNode(4)
a1.next = b2
b2.next = c3


solution = Solution3()
result = solution.mergeTwoLists(a, a1)

while result:
    print(result.val)
    result = result.next

                
        