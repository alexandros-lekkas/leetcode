[
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

// Removed print statements due to output exceeding

class Solution {
    public ListNode doubleIt(ListNode head) {
        Stack<Integer> values = new Stack<>();
        int val = 0;
        
        while (head != null) {
            values.push(head.val);
            head = head.next;
        }
        
        ListNode newTail = null;
        
        while (!values.isEmpty() || val != 0) {
            newTail = new ListNode(0, newTail);
            // System.out.println("Start: " + newTail.val);
                
            if (!values.isEmpty()) {
                val += values.pop() * 2;
            }
            // System.out.println("Popped * 2: " + val);
            newTail.val = val % 10;
