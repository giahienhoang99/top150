public class GameOfLife {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;
        int[] xdir = { 1, -1, 0, 0, 1, -1, -1, 1 };
        int[] ydir = { 0, 0, 1, -1, -1, 1, -1, 1 };

        int[][] temp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int countLive = 0;
                
                for (int idx = 0; idx < 8; idx++) {
                    if (i + xdir[idx] < 0 || i + xdir[idx] >= m || 
                        j + ydir[idx] < 0 || j + ydir[idx] >= n) {
                        continue;
                    }
                    if (board[i + xdir[idx]][j + ydir[idx]] == 1) {
                        countLive++;
                    }
                }
                
                // if cur = 0
                if (board[i][j] == 0 && countLive == 3) {
                    temp[i][j] = 1;
                    continue;
                } else if (board[i][j] == 0 && countLive != 3) {
                    temp[i][j] = 0;
                    continue;
                }
                // if cur = 1
                if (countLive <= 1) {
                    temp[i][j] = 0;
                } else if (countLive <= 3) {
                    temp[i][j] = 1;
                } else {
                    temp[i][j] = 0;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = temp[i][j];
            }
        }
    }
}
