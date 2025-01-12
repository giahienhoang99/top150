import java.util.PriorityQueue;
import java.util.Collections;

public class LastStoneWeight {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int stone : stones) {
            maxHeap.add(stone);
        }
        while (maxHeap.size() > 1) {
            int big = maxHeap.poll();
            int small = maxHeap.poll();

            if (big != small) {
                maxHeap.add(big - small);
            }
        }

        return maxHeap.size() == 0 ? 0 : maxHeap.poll();
    }
}
