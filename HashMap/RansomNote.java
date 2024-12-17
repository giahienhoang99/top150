package HashMap;

import java.util.HashMap;
import java.util.Map;

public class RansomNote {
    public boolean canConstructUsingHashMap(String ransomNote, String magazine) {
        Map<Character,Integer> count = new HashMap<>();
        for (int i = 0; i < magazine.length(); i++) {
            char cur = magazine.charAt(i);
            if (!count.containsKey(cur)) {
                count.put(cur, 1);
            } else {
                count.put(cur, count.get(cur) + 1);
            }
        }
        for (char c : ransomNote.toCharArray()) {
            if (count.containsKey(c)) {
                if (count.get(c) == 1) {
                    count.remove(c);
                    continue;
                }
                count.put(c, count.get(c) - 1);
            } else {
                return false;
            }
        }
        return true;
    }


    
}
