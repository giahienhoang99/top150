import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupAnagram {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] cur = s.toCharArray();
            Arrays.sort(cur);
            String sorted = new String(cur);

            if (!map.containsKey(sorted)) {
                map.put(sorted, new ArrayList<>(Arrays.asList(s)));
            } else {
                map.get(sorted).add(s);
            }
        }
        return new ArrayList<>(map.values());
    }
}
