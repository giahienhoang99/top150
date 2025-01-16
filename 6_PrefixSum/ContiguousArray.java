import java.util.HashMap;
import java.util.Map;

public class ContiguousArray {
    public int findMaxLength(int[] nums) {
        int res = 0;
        int diff = 0;
        Map<Integer,Integer> mapDiffToIdx = new HashMap<>();
        mapDiffToIdx.put(0, -1);

        for (int i = 0; i < nums.length; i++) {
            diff += (nums[i] == 1) ? 1 : -1;
            if (!mapDiffToIdx.containsKey(diff)) {
                mapDiffToIdx.put(diff, i);
            } else {
                res = Math.max(i - mapDiffToIdx.get(diff), res);
            }
        }

        return res;
    }
}
