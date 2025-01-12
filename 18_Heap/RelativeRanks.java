import java.util.PriorityQueue;
import java.util.Collections;

public class RelativeRanks {
    // initial solution
    public String[] findRelativeRanks(int[] score) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int s : score) {
            maxHeap.add(s);
        }
        String[] res = new String[score.length];
        // terrible time complexity
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

    public class Pair<K, V> {
        private K key;
        private V value;
    
        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }
    
        public K getKey() {
            return key;
        }
    
        public V getValue() {
            return value;
        }
    }

    // better solution
    public String[] findRelativeRanks2(int[] score) {
        int N = score.length;

        // Create a max heap of pairs (score, index)
        PriorityQueue<Pair<Integer, Integer>> heap = new PriorityQueue<>(
                (a, b) -> b.getKey() - a.getKey());
        for (int i = 0; i < N; i++) {
            heap.add(new Pair<>(score[i], i));
        }

        // Assign ranks to athletes
        String[] rank = new String[N];
        int place = 1;
        while (!heap.isEmpty()) {
            Pair<Integer, Integer> pair = heap.poll();
            int originalIndex = pair.getValue();
            if (place == 1) {
                rank[originalIndex] = "Gold Medal";
            } else if (place == 2) {
                rank[originalIndex] = "Silver Medal";
            } else if (place == 3) {
                rank[originalIndex] = "Bronze Medal";
            } else {
                rank[originalIndex] = String.valueOf(place);
            }
            place++;
        }
        return rank;
    }
}
