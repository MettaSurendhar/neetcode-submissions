# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        if not head.next:
            return None

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev

            prev,curr = curr,temp

        head = prev
        dummy = ListNode(0,head)
        prev, curr = dummy, head

        for _ in range(n-1):
            prev,curr = curr,curr.next

        prev.next = prev.next.next

        head = dummy.next
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev

            prev,curr = curr,temp

        return prev
        