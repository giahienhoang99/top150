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
}
