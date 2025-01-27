import java.util.HashSet;
import java.util.Set;

public class LongestSubstringWithourRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0 || s.length() == 1) {
            return s.length();
        }
        int left = 0;
        int right = 0;
        Set<Character> seen = new HashSet<>();
        int res = 0;
        int l = s.length();

        while (right < l) {
            char c = s.charAt(right);
            // if not seen => add and continue;
            if (!seen.contains(c)) {
                res = Math.max(res, right - left + 1);
                seen.add(c);
                right++;
                continue;
            }
            
            // if seen => remove leftmost char until unseen
            while (seen.contains(c)) {
                seen.remove(s.charAt(left));
                left++;
            }
            // then add c
            res = Math.max(res, right - left + 1);
            seen.add(c);
            right++;
        }

        return res;
    }    
}
