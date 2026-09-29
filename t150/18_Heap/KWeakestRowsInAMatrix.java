import java.util.PriorityQueue;

public class KWeakestRowsInAMatrix {
    public int[] kWeakestRows(int[][] mat, int k) {
        // idea:
        // using max heap to store k smallest elements only by using
        // the cycle of adding and removing the biggest if heap size > k

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            // int[2]: first int = row, second int = soldier count for row
            (a, b) -> {
                if (a[1] == b[1]) {
                    return b[0] - a[0];
                } else {
                    return b[1] - a[1];
                }
            }
        );

        for (int i = 0; i < mat.length; i++) {
            int count = 0;

            for (int j = 0; j < mat[0].length; j++) {
                if (mat[i][j] == 1) count++;
                else break;;
            }

            maxHeap.add(new int[]{i, count});
            
            if (maxHeap.size() > k) {
                maxHeap.remove();
            }
        }

        int[] res = new int[maxHeap.size()];
        int i = 0;
        // getting result int arr
        while (!maxHeap.isEmpty()) {
            int[] cur = maxHeap.poll();
            // reverse order since result is ordered from weak to strong
            res[k - 1 - i] = cur[0];
            i++;
        }

        return res;
    }
}
