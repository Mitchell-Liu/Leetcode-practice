# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, pre.next = ListNode(), head
        ans = pre
        while pre.next and pre.next.next:
            curr = pre.next
            next_node = curr.next
            pre.next,  next_node.next, curr.next = next_node,  curr, next_node.next
            pre = curr
        return ans.next