# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node acts as starting point
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # if there are nunmbers left in the lists, or there is a carry to be processed
        while l1 or l2 or carry:
            # Get the value from the node, or 0 if we're at the end of the lists
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Get the current number
            total = val1 + val2 + carry
            carry = total // 10     # Gets the tens digit to the result (i.e. what needs to be carried)
            new_digit = total % 10  # Gets the ones digit of the result
            
            # Build the next node
            current.next =ListNode(new_digit)

            # Shift pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next