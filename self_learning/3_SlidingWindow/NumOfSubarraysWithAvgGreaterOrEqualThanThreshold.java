public class NumOfSubarraysWithAvgGreaterOrEqualThanThreshold {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int left = 0;
        int right = 0;
        int count = 0;
        int sum = 0;

        for (right = 0; right < k; right++) {
            sum += arr[right];
        }

        if (sum / k >= threshold) {
            count++;
        }
        if (k == arr.length) {
            return count;
        }

        sum -= arr[left];
        left++;

        while (right < arr.length) {
            sum += arr[right];

            if (sum / k >= threshold) {
                count++;
            }

            right++;
            sum -= arr[left];
            left++;
        }

        return count;
    }
    public int numOfSubarrays2(int[] arr, int k, int threshold) {
        int n = arr.length;
        int sum = 0;
        int count = 0;
        
        for (int i = 0; i < k; i++) {
            sum += arr[i];
        }
        
        if (sum / k >= threshold) {
            count++;
        }

        for (int i = k; i < n; i++) {
            int last = arr[i];
            int first = arr[i - k];
            sum += last;
            sum -= first;

            if (sum / k >= threshold) {
                count++;
            }
        }

        return count;
    }
}