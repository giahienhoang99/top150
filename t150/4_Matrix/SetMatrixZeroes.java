public class SetMatrixZeroes {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[] rowZeroes = new int[m];
        int[] colZeroes = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rowZeroes[i] = 1;
                    colZeroes[j] = 1;
                }
            }
        }

        for (int i = 0; i < rowZeroes.length; i++) {
            if (rowZeroes[i] == 1) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < colZeroes.length; i++) {
            if (colZeroes[i] == 1) {
                for (int j = 0; j < m; j++) {
                    matrix[j][i] = 0;
                }
            }
        }
    }
}
