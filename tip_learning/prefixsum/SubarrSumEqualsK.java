package tip_learning.prefixsum;

import java.util.HashMap;
import java.util.Map;

public class SubarrSumEqualsK {
    public int subarraySum(int[] nums, int k) {
        // 1 1 1
        // 1 2 3
        // k = 2
        // 1 1
        // 
        // 2 1
        // target = 2 - 2 = 0
        // ans = 1
        // 3 1
        // target = 3 - 2 = 1
        // ans += 1
        // ans = 2

        // n(n+1)/2 on2
        // 10^6 -> fix to 1m-10m

        // [-1,-1,1]
        // 0 -1 -2 -1

        int ans = 0;
        int sum = 0;

        if (nums.length == 1) {
            return nums[0] == k ? 1 : 0;
        }

        // map prefsum to freq
        Map<Integer, Integer> freqMap = new HashMap<>();
        freqMap.put(0, 1);

        // Objective: Find how many i so that prefixSum[i] == target

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            // bao nhieu thang = target
            int target = sum - k;
            ans += freqMap.getOrDefault(target, 0);

            if (!freqMap.containsKey(sum)) {
                freqMap.put(sum, 1);
            } else {
                freqMap.put(sum, freqMap.get(sum) + 1);
            }
        }

        return ans;
    }
}
