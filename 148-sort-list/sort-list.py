class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Get total length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0)
        dummy.next = head

        size = 1
        while size < length:
            cur = dummy.next
            tail = dummy  # tail of the last merged pair

            while cur:
                left = cur
                right = self.split(left, size)   # split off 'size' nodes as left half
                cur   = self.split(right, size)  # split off 'size' nodes as right half

                # Merge left and right, attach to tail
                merged_head, merged_tail = self.merge(left, right)
                tail.next = merged_head
                tail = merged_tail

            size *= 2

        return dummy.next

    def split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        """Cut off 'size' nodes from head, return the rest."""
        for _ in range(size - 1):
            if not head:
                break
            head = head.next

        if not head:
            return None

        rest = head.next
        head.next = None  # sever the link
        return rest

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        """Merge two sorted lists, return (head, tail)."""
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        # Advance cur to the actual tail
        while cur.next:
            cur = cur.next

        return dummy.next, cur