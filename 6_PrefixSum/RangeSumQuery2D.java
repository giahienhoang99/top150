public class RangeSumQuery2D {
    class NumMatrix {

        int[][] sumMatrix;
    
        public NumMatrix(int[][] matrix) {
            int m = matrix.length;
            int n = matrix[0].length;
            sumMatrix = new int[m][n];
    
            sumMatrix[0][0] = matrix[0][0];
    
            // prefix sum for first col
            for (int i = 1; i < m; i++) {
                sumMatrix[i][0] = matrix[i][0] + sumMatrix[i-1][0];
            }
            // prefix sum for first row
            for (int i = 1; i < n; i++) {
                sumMatrix[0][i] = matrix[0][i] + sumMatrix[0][i-1];
            }
            // 2d arr prefix sum or region sum
            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    sumMatrix[i][j] = matrix[i][j] + sumMatrix[i][j-1] + sumMatrix[i-1][j] - sumMatrix[i-1][j-1];
                }
            }
        }
        
        public int sumRegion(int row1, int col1, int row2, int col2) {
            if (row1 == 0 && col1 == 0) {
                return sumMatrix[row2][col2];
            }
            if (row1 == 0) {
                return sumMatrix[row2][col2] - sumMatrix[row2][col1-1];
            }
            if (col1 == 0) {
                return sumMatrix[row2][col2] - sumMatrix[row1-1][col2];
            }
            return sumMatrix[row2][col2] - sumMatrix[row1-1][col2] - sumMatrix[row2][col1-1] + sumMatrix[row1-1][col1-1];
        }
    }
}
