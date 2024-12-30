import java.util.HashMap;
import java.util.Map;

public class WordPattern {
    public boolean wordPattern(String pattern, String s) {
        String[] arr = s.split(" ");
        Map<Character, String> map = new HashMap<Character, String>();
        Map<String, Character> map2 = new HashMap<String, Character>();

        if (arr.length != pattern.length()) {
            return false;
        }

        for (int i = 0; i < pattern.length(); i++) {
            char cur = pattern.charAt(i);

            // map does not have cur
            if (!map.containsKey(cur)) {
                // map2 does not have arr[i]
                if (!map2.containsKey(arr[i])) {
                    // map both
                    map.put(cur, arr[i]);
                    map2.put(arr[i], cur);
                } else {
                    // if cur not in map but arr[i] in map2 already => false
                    return false;
                }
            } else {// map has cur already
                // but map2 does not have arr[i]
                if (!map2.containsKey(arr[i])) {
                    return false;
                } else {
                    // map2 has arr[i] but assigned to diff char than cur
                    if (!map2.get(arr[i]).equals(cur)) {
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
