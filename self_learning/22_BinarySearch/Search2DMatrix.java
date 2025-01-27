public class Search2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int row = 0;
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] == target) {
                return true;
            }
            if (target > matrix[i][0]) {
                row = i;
            }
        }
        int left = 0;
        int right = matrix[row].length - 1;
        while (left <= right) {
            int mid = left + (right - left)/2;
            if (matrix[row][mid] == target) {
                return true;
            }
            if (matrix[row][mid] > target) {
                right = mid - 1;
            }
            if (matrix[row][mid] < target) {
                left = mid + 1;
            }
        }
        return false;
    }
}
