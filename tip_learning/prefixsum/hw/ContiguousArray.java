package tip_learning.prefixsum.hw;

import java.util.HashMap;

public class ContiguousArray {
    public int findMaxLength(int[] nums) {
        /**
        Thought process:

        Brute force: O(n^3) => TLE
        int max = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int sumz = 0;
                int sumo = 0;
                for (int left = i; left <= j; left++) {
                    if (nums[left] == 0) sumz++;
                    else sumo++;
                }
                if (sumz == sumo) max = Math.max(max, j-i+1);
            }
        }
        return max;

        2nd Approach
        Notice: the sum is being calculated over and over again
        => Try using prefsum arr for both 0 and 1
        => O(n^2) => Still TLE

        int max = 0;
        
        int n = nums.length + 1;
        int[] ps0 = new int[n];
        int[] ps1 = new int[n];
        ps0[0] = 0;
        ps1[0] = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i-1] == 0) {
                ps0[i] = ps0[i-1] + 1;
                ps1[i] = ps1[i-1];
            } else {
                ps1[i] = ps1[i-1] + 1;
                ps0[i] = ps0[i-1];
            }
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j <= nums.length; j++) {
                if (ps0[j] - ps0[i] == ps1[j] - ps1[i]) {
                    max = Math.max(max, j-i);
                }
            }
        }

        return max;
        
        3rd Approach
        - dont use prefix sum arr?
        - hashmap: count of each num -> index
        - 2 maps?
            map1: count of 0s -> index
            map2: count of 1s -> index

            diff = count0 - count1

        map: diff -> index of first diff
        Objective: max = max(max, cur index - index where the first occurrence of that diff)
        */

        int max = 0;
        // maps to store the first occurrence of counts of 0s and 1s
        HashMap<Integer, Integer> mapDiffToIndex = new HashMap<>();
        // handle cases where the subarray starts at index 0
        mapDiffToIndex.put(0, -1);

        int count0 = 0;
        int count1 = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                count0++;
            } else {
                count1++;
            }

            int diff = count0 - count1;

            // if diff not seen then add
            if (!mapDiffToIndex.containsKey(diff)) {
                mapDiffToIndex.putIfAbsent(diff, i);
            } else {
                // if diff seen then update max
                max = Math.max(max, i - mapDiffToIndex.getOrDefault(diff, i));
            }
        }

        return max;
    }
}
