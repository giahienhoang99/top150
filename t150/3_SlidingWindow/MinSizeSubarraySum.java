public class MinSizeSubarraySum {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0; // left
        int right = 0; // right
        int sum = 0; // window sum
        int minLen = Integer.MAX_VALUE; // answer: min length

        for (; right < nums.length; right++) {
            sum += nums[right];
            
            while (sum >= target) {
                minLen = Math.min(minLen, right - left + 1);
                sum -= nums[left];
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }    
}
