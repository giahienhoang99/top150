public class DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        int hottest = 0;
       
        for (int i = n-1; i >= 0; i--) {
            int cur = temperatures[i];
 
 
            // if (temp[i] = hotest one seen => ans[i] = 0
            if (cur >= hottest) {
                ans[i] = 0;
                hottest = cur;
                continue;
            }
 
 
            // if cur < hottest
            /*
            ans[i] = days from t[i] to next bigger val
            => compare temp[i + days] with cur
                                       >  : found next bigger from cur
                                       <= : increment days until temp[i + days] > cur
            set ans[i] = days
            */
            int days = 1;
            while (temperatures[i + days] <= cur) {
                days += ans[i + days];
                // days++ => TLE since it would be same as init sol
                // take advantage of the fact that we have ans[i+1] -> ans[n-1]
                // => jump to nearest warmer day without incrementing by 1 (= what init sol does)
            }
            ans[i] = days;
        }
 
        return ans;
    }
}
