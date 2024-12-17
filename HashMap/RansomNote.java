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


    public boolean canConstructUsingArray(String ransomNote, String magazine) {
        int[] rsm = getFreq(ransomNote);
        int[] mag = getFreq(magazine);

        for (int i = 0; i < 26; i++) {
            if (rsm[i] > mag[i]) {
                return false;
            }
        }
        
        return true;
    }

    private static int[] getFreq(String s) {
        int[] freq = new int[26];   // all elements init to 0 already
        for (char c : s.toCharArray()) {
            int i = c - 'a';
            freq[i]++;
        }
        return freq;
    }
}
