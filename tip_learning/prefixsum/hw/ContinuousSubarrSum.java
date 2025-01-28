package tip_learning.prefixsum.hw;

import java.util.HashMap;
import java.util.Map;

public class ContinuousSubarrSum {
    public boolean checkSubarraySum(int[] nums, int k) {
        /**
        good sub arr:
        - length >= 2
        - sum of elements % k == 0
        
        nums 23 2  4  6  7
        pref 23 25 29 35 42
                i  j
        
        j - i + 1 >= 0

        Objective: target = sum - k * n
        sum - target = k*n
        sum - target % k == 0

        sum % k = x
        map: x -> i
        if in map exist a key that has the same rem when divided by k as when divide cur sum by k that means the range from that key to sum is divisible by k
        */

        int sum = 0;
        // map (sum % k) to idx
        Map<Integer,Integer> map = new HashMap<>();
        map.put(0, -1);

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            int rem = sum % k;

            if (map.containsKey(rem) && i - map.get(rem) >= 2) {
                return true;
            }

            if (!map.containsKey(rem)) {
                map.put(rem, i);
            }
        }

        return false;
    }
}
