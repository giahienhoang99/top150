public class ValidPalindrome {
    public static boolean isPalindrome(String s) {
        String a = s.toLowerCase();
        int last = s.length() - 1;
        int start=0;
        while (start<=last) {
            char cf = a.charAt(start);
            char cl = a.charAt(last);
            if (!Character.isLetterOrDigit(cf)){
                start++;
            } else if (!Character.isLetterOrDigit(cl)){
                last--;
            } else {
                if (cf!=cl) return false;

                start++;
                last--;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String test1 = "A man, a plan, a canal: Panama";
        String test2 = "race a car";
        String test3 = " ";
        String test4 = "v' 5:UxU:5 v'";

        System.out.println("Is this a palindrome?");
        System.out.printf("%-40s: %b%n", test1, isPalindrome(test1));
        System.out.printf("%-40s: %b%n", test2, isPalindrome(test2));
        System.out.printf("%-40s: %b%n", test3, isPalindrome(test3));
        System.out.printf("%-40s: %b%n", test4, isPalindrome(test4));
    }
}