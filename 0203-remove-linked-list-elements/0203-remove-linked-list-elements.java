/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return head;
        }
        while (head != null && head.val == val) {
            head = head.next;
            if (head == null) {
                return null;
            }
        }

        ListNode cloneHead = head;
        while (cloneHead.next != null) {
            if (cloneHead.next.val == val) {
                cloneHead.next = cloneHead.next.next;
            } else {
                cloneHead = cloneHead.next;
            }
        }
        return head;
    }
}