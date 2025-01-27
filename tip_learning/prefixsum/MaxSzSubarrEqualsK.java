package tip_learning.prefixsum;

import java.util.HashMap;
import java.util.Map;

public class MaxSzSubarrEqualsK {
    public int maxSubArrayLen(int[] nums, int k) {
        int ans = 0;
        int sum = 0;
        
        // prefix[j] = prefix[i] - k
        // Objective: j satisfies condition + j smallest

        // hashmap<j,sum>
        // map ps[i] to i
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0,-1);

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            int target = sum - k;

            // neu map co target -> ans = max(ans, i - map.get(target) + 1)
            if (map.containsKey(target)) {
                ans = Math.max(ans, i - map.get(target));
            }

            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }

        return ans;
    }
}
