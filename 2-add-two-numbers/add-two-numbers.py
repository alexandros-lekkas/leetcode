class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = ""
        while l1 is not None:
            l1_num = str(l1.val) + l1_num
            l1 = l1.next
        l1_num = int(l1_num)

        l2_num = ""
        while l2 is not None:
            l2_num = str(l2.val) + l2_num
            l2 = l2.next
        l2_num = int(l2_num)

        l3 = l1_num + l2_num
        l3 = str(l3)

        root = ListNode(int(l3[-1]))
        node = root

        for i in range(len(l3) - 2, -1, -1):
            new_node = ListNode(int(l3[i]))
            node.next = new_node
            node = new_node

        return root
