import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MergeIntervals {
    public int[][] merge(int[][] intervals) {
       if (intervals.length == 1)
           return intervals;
       int m = intervals.length;


       // idea:
       // sort the intervals by their start then end val
       // make the first interval as big as possible
       // if cannot make bigger then move to next interval and repeat


       // cai nay em dung chatgpt vi e chi biet dung Arrays.sort() binh thuong thoi
       // Sort by first value, then by second value if first values are the same
       Arrays.sort(intervals, (a, b) -> {
           if (a[0] != b[0]) {
               return Integer.compare(a[0], b[0]); // Compare first values
           }
           return Integer.compare(a[1], b[1]); // Compare second values if first are equal
       });


       System.out.print("[");
       for (int i = 0; i < m; i++) {
           int start = intervals[i][0];
           int end = intervals[i][1];
           System.out.print("[" + start + "," + end + "],");
       }
       System.out.print("]");


       // dont know length of merged so have to use list instead of arr
       List<int[]> res = new ArrayList<>();


       int nextIndex = 1;
       // start and end of first interval
       int curStart = intervals[0][0];
       int curEnd = intervals[0][1];


       while (nextIndex < m) {
           // start and end of next interval
           int nextStart = intervals[nextIndex][0];
           int nextEnd = intervals[nextIndex][1];


           // 2 cases (after sorting):
           // nextStart = curStart
           //      => update curEnd = nextEnd
           // nextStart > curStart
           //      => check if nextStart <= curEnd
           //      if nextStart <= curEnd:
           //          then update curEnd = max(curEnd, nextEnd)
           //      if nextStart > curEnd
           //          then not mergeable


           // overlap => merge
           if (nextStart == curStart) {
               curEnd = nextEnd;
               nextIndex++;
               continue;
           } else {
               if (nextStart <= curEnd) {
                   curEnd = Math.max(curEnd,nextEnd);
                   nextIndex++;
                   continue;
               } else {
                   // not overlap
                   // => add merged interval to res
                   // => update curStart, curEnd
                   int[] toAdd = new int[] { curStart, curEnd };
                   res.add(toAdd);


                   curStart = nextStart;
                   curEnd = nextEnd;
                   nextIndex++;
               }
           }
       }
       // final add
       res.add(new int[] {curStart, curEnd});
       // turn res into 2d arr
       int[][] result = new int[res.size()][2];
       for (int i = 0; i < res.size(); i++) {
           result[i] = res.get(i);
       }


       return result;
   }
}
