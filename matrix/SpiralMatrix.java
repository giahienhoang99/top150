package matrix;

import java.util.ArrayList;
import java.util.List;

public class SpiralMatrix {
   public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length; 
        int n = matrix[0].length;

        List<Integer> result = new ArrayList<>();

        // 4 sides limits
        int left = 0, right = n - 1;
        int top = 0, bot = m - 1;

        while (top <= bot && left <= right) {
            
            
            
        }

        return result;
    } 
}
