class Solution {
    public boolean isPalindrome(int x) {
        String num = String.valueOf(x);
        int leftPointer = 0;
        int rightPointer = num.length()-1;

        return check(leftPointer, rightPointer, num); // Perfo
    }

    public boolean check(int leftPointer, int rightPointer, String num) {
        if (num.length() == 1) {
            return true;
        }
        while (leftPointer != rightPointer && leftPointer < num.length() && rightPointer > 0) {
            if (num.charAt(leftPointer) != num.charAt(rightPointer)) {
                return false;
            } else {
                leftPointer++;
                rightPointer--;
            }
        }

        return true;
    }


}