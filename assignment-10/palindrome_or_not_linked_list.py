# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stk = []
        curr = head
        while curr  :
            stk.append(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.val != stk.pop():
                return False
            curr = curr.next
        return True