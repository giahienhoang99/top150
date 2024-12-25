public class MaxConsecutiveOnes {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int right = 0;

        // if valid:   increment window size 
        // if invalid: shift current window
        // in the end just return right - left => auto track the max length

        for (right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                k--;
            }
            if (k < 0) {
                if (nums[left] == 0) {
                    k++;
                }
                left++;
            }
            //System.out.println(left + " " + right);
        }
        // right - left because right got incremented to nums.length after the last loop
        return right - left;
    }
}
