# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # simple hashtable lookups, You can store an entire node in a set O(1) and it refernces object memory
        # However it does not keep the objects pointer or links to other nodes
        seen = set()

        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False


        
        
        