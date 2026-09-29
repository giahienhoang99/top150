public class RangeSumQueries {
    class NumArray {
        private int[] prefSum;
    
        public NumArray(int[] nums) {
            prefSum = new int[nums.length];
            prefSum[0] = nums[0];
    
            for (int i = 1; i < nums.length; i++) {
                prefSum[i] = prefSum[i-1] + nums[i];
            }
        }
        
        public int sumRange(int left, int right) {
            return left == 0 ? prefSum[right] : prefSum[right] - prefSum[left-1];
        }
    }
}
