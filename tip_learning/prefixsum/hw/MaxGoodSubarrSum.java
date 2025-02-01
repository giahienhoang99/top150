package tip_learning.prefixsum.hw;

import java.util.HashMap;
import java.util.Map;

public class MaxGoodSubarrSum {
    public long maximumSubarraySum(int[] nums, int k) {
        /**
         * CONDITION
         * find max sum from index i to j such that:
         *    |nums[i] - nums[j]| = k
         * <=> nums[i] - nums[j]  = k or -k
         * 
         * PSEUDOCODE
         * for i in range(0, n)
         *      map: map nums[i] -> min prefix sum where nums[i] occur
         *
         *      update map:
         *      if exists key nums[i] then check whether its val is the min prefsum
         *      if not then map nums[i] -> cur prefsum
         *
         *      check if map contains (cur prefsum - k) or (cur prefsum + k)
         *      -> if yes, update max to
         *         max(max, cur prefsum - map.get(cur prefsum +- k) + (cur prefsum +- k))
         *
         */

        // use type long to handle big ints
        long max = Long.MIN_VALUE;
        long prefsum = 0;
        Map<Long,Long> numToSum = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            prefsum += nums[i];
            long cur = nums[i]; // use Long since my map is Long->Long

            // update map
            if (numToSum.containsKey(cur)) {
                numToSum.put(cur, Math.min(prefsum, numToSum.get(cur)));
            } else {
                numToSum.put(cur, prefsum);
            }

            // check condition
            if (numToSum.containsKey(cur - k)) {
                max = Math.max(max, prefsum - numToSum.get(cur - k) + cur - k);
            }
            if (numToSum.containsKey(cur + k)) {
                max = Math.max(max, prefsum - numToSum.get(cur + k) + cur + k);
            }
        }

        return max == Long.MIN_VALUE ? 0 : max;
    }
}
