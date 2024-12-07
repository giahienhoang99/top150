public class IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        if (s.length() > t.length()) return false;
        int i = 0;
        int j = 0;
        
        while (i < s.length() && j < t.length()) {
            char scur = s.charAt(i);
            char tcur = t.charAt(j);
            if (scur != tcur) {
                j++;
                continue;
            }
            i++;
            j++;
        }

        return i > s.length()-1;
    }    
}
