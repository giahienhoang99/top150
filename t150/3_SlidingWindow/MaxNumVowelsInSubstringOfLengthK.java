public class MaxNumVowelsInSubstringOfLengthK {
    public int maxVowels(String s, int k) {
        int left = 0;
        int right = 0;
        int res = 0;
        int countVowelsInCurrentWindow = 0;

        // construct window
        for (; right < k; right++) {
            char c = s.charAt(right);
            if (isVowel(c)) {
                countVowelsInCurrentWindow++;
            }
        }
        
        res = Math.max(res, countVowelsInCurrentWindow);

        if (k == s.length()) {
            return res;
        }

        // start sliding the window
        while (right < s.length()) {
            if (isVowel(s.charAt(right))) {
                countVowelsInCurrentWindow++;
            }
            if (isVowel(s.charAt(left))) {
                countVowelsInCurrentWindow--;
            }
            res = Math.max(res, countVowelsInCurrentWindow);
            right++;
            left++;
        }

        return res;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }    
}
