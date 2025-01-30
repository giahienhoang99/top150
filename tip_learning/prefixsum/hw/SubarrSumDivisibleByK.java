package tip_learning.prefixsum.hw;

import java.util.HashMap;
import java.util.Map;

public class SubarrSumDivisibleByK {
    public int subarraysDivByK(int[] nums, int k) {
        /**
         * sum - target = k * n
         * use hashmap to map: sum % k -> number of occurrence
         * 
         * Objective: target % k == sum % k
         */

        int count = 0;
        Map<Integer, Integer> mapRemToCount = new HashMap<>();
        mapRemToCount.put(0, 1);    // sum % k = zero has one occurrence already

        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            int rem = sum % k;

            if (rem < 0) {
                rem += k;
            }

            if (mapRemToCount.containsKey(rem)) {
                count += mapRemToCount.get(rem);
            }
            // update map
            mapRemToCount.put(rem, mapRemToCount.getOrDefault(rem, 0) + 1);
        }

        return count;
    }
}
