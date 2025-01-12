import java.util.PriorityQueue;
import java.util.Collections;

public class RelativeRanks {
    public String[] findRelativeRanks(int[] score) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : score) {
            maxHeap.add(s);
        }

        String[] res = new String[score.length];

        for (int i = 0; i < score.length; i++) {
            int cur = maxHeap.poll();
            for (int j = 0; j < score.length; j++) {
                if (score[j] == cur) {
                    if (i > 2) {
                        res[j] = String.valueOf(i + 1);
                    } else {
                        if (i == 0) {
                            res[j] = "Gold Medal";
                        }
                        if (i == 1) {
                            res[j] = "Silver Medal";
                        }
                        if (i == 2) {
                            res[j] = "Bronze Medal";
                        }
                    }
                }
            }
        }

        return res;
    }
}
