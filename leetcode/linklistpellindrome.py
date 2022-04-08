from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_ptr = head
        slow_ptr = head
        val_list = []
        if not head.next:
            return True

        while fast_ptr and fast_ptr.next:
            val_list.append(slow_ptr.val)
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if fast_ptr:
            slow_ptr = slow_ptr.next

        while slow_ptr:
            if slow_ptr.val != val_list[-1]:
                return False
            slow_ptr = slow_ptr.next
            val_list.pop()

        if val_list:
            return False

        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    s = Solution()
    print(s.isPalindrome(head))
