public class FindPivotIndex {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        int leftSum = 0;
        
        for (int num : nums) {
            sum += num;
        }

        for (int i = 0; i < nums.length; i++) {
            leftSum += i == 0 ? 0 : nums[i-1];
            if (leftSum == sum - leftSum - nums[i]) {
                return i;
            }
        }

        return -1;
    }
    public int pivotIndex2(int[] nums) {
        int[] prefsum = new int[nums.length+1];
        
        for (int i = 0; i < nums.length; i++) {
            prefsum[i+1] = prefsum[i] + nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            if (prefsum[i] == prefsum[nums.length] - prefsum[i+1]) {
                return i;
            }
        }

        return -1;
    }
}
