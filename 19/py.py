# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        curr = head
        count = 0
        
        while curr:
            count+=1
            curr = curr.next
        
        index = count - n
        curr = head
        if n == count:
            head = head.next
            return head
        if count == 1:
            return None
        for i in range(index-1):
            curr = curr.next
        if curr.next == None:
            return head
        else:
            curr.next = curr.next.next
        print(head)
        return head