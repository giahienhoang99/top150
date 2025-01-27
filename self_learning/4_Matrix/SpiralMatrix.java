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
            
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;
            for (int i = top; i <= bot; i++) {
                result.add(matrix[i][right]);
            }
            right--;
            if (top <= bot) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bot][i]);
                }
                bot--;
            }
            if (left <= right) {
                for (int i = bot; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
            
        }

        return result;
    } 
}
