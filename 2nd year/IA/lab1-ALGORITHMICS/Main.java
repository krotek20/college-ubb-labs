package ro.ubbcluj.cs;

import java.util.*;

public class Main {
    static class Tuple<E> {
        private final E x, y;

        Tuple(E x, E y) {
            this.x = x;
            this.y = y;
        }

        public E left() {
            return x;
        }

        public E right() {
            return y;
        }
    }

    // ================================================================= //

    /**
     * 1.
     * We are going to iterate through each word in str
     * separated by single spaces. Once we find a word
     * lexicographically "bigger" than the {@code ans},
     * we store it in {@code ans}.
     * Time - O(n) - where n is the number of words in str.
     * Space - O(1)
     *
     * @param str given sentence with words separated only by single spaces.
     * @return the lexicographically biggest word.
     */
    public static String lastWord(String str) {
        String ans = "";
        for (String word : str.split(" ")) {
            if (word.compareTo(ans) > 0) {
                ans = word;
            }
        }
        return ans;
    }

    /**
     * 2.
     * Using plain formula (BC^2 = AB^2 + AC^2)
     * Time - O(1)
     * Space - O(1)
     * x - horizontal axis; y - vertical axis
     *
     * @param x1 first point's x.
     * @param y1 first point's y.
     * @param x2 second point's x.
     * @param y2 second point's y.
     * @return euclidean distance between (x1, y1) and (x2, y2).
     */
    public static double euclideanDistance(double x1, double y1, double x2, double y2) {
        return Math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1));
    }

    /**
     * 3. V1
     * We know the vectors need to have the same size.
     * So, we iterate until we reach the middle, adding
     * the product of the same indexed values from the start,
     * meanwhile we do the same from the end.
     * Time - O(n) - where n is the size of a vector.
     * Space - O(1)
     *
     * @param firstArray  first vector
     * @param secondArray second vector
     * @return scalar product of {@code firstArray} and {@code secondArray}.
     */
    public static int scalarProduct1(int[] firstArray, int[] secondArray) {
        int ans = 0, len = firstArray.length;
        for (int i = 0; i < len / 2; i++) {
            ans += ((firstArray[i] * secondArray[i]) + (firstArray[len - i - 1] * secondArray[len - i - 1]));
        }
        return len % 2 == 1 ? ans + (firstArray[len / 2] * secondArray[len / 2]) : ans;
    }

    /**
     * 3. V2
     * We want to store all non-zero values from the first array into a map
     * so we can access them easily for computing the final sum.
     * Time - O(n) - where n is the size of a vector.
     * Space - O(1)
     *
     * @param firstArray  first vector
     * @param secondArray second vector
     * @return scalar product of {@code firstArray} and {@code secondArray}.
     */
    public static int scalarProduct2(int[] firstArray, int[] secondArray) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < firstArray.length; i++) {
            if (firstArray[i] != 0) {
                map.put(i, firstArray[i]);
            }
        }
        for (int i = 0; i < secondArray.length; i++) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) * secondArray[i]);
            }
        }
        return map.values().stream().reduce(0, Integer::sum);
    }

    /**
     * 4.
     * We are using two sets:
     * - once -> store words that appear only once in str.
     * - more -> store words with multiple occurrences in str.
     * If we find a word that already exists in {@code once} we move it to {@code more}.
     * Otherwise, if the word can't be found in {@code more} we add it in {@code once}.
     * Time - O(n)
     * Space - O(n)
     * where n is the number of words in the given sentence.
     *
     * @param str given sentence with single spaced words.
     * @return words from str with only once occurrence.
     */
    public static List<String> occurredOnce(String str) {
        if (str.length() == 0) return null;
        Set<String> once = new HashSet<>();
        Set<String> more = new HashSet<>();
        for (String word : str.split(" ")) {
            if (once.contains(word)) {
                once.remove(word);
                more.add(word);
            } else if (!more.contains(word)) {
                once.add(word);
            }
        }
        return new ArrayList<>(once);
    }

    /**
     * 5. V1
     * Computing the sum of arr, then we subtract the sum from 1 to n - 1.
     * Time - O(n) - where n is the length of the given array.
     * Space - O(1)
     *
     * @param arr given array.
     * @return repeated element.
     */
    public static int repeatedValue1(int[] arr) {
        int sum = 0;
        for (Integer num : arr) {
            sum += num;
        }
        return sum - (arr.length - 1) * arr.length / 2;
    }

    /**
     * 5. V2
     * Another nice solution extends the problem statement to:
     * "A single value is repeating MORE THAN ONCE" (not only twice, as the original problem says).
     * We are using cycle detection Floyd's theorem (wikipedia: cycle detection).
     * Time - O(n) - where n is the length of the given array.
     * Space - O(1)
     *
     * @param arr given array.
     * @return repeated element.
     */
    public static int repeatedValue2(int[] arr) {
        int slow = arr[0];
        int fast = arr[0];
        do {
            slow = arr[slow];
            fast = arr[arr[fast]];
        } while (slow != fast);

        slow = arr[0];
        while (slow != fast) {
            slow = arr[slow];
            fast = arr[fast];
        }
        return slow;
    }

    /**
     * 6.
     * We want to count instances of majority element as +1 and any occurrence
     * of other elements as -1. Adding them together will make it obvious what's the majority element.
     * As for this, whenever the counting flag will get to 0 we will replace the major with the current element.
     * (I know there were a theorem based on this, but I forgot its name).
     * Time - O(n) - where n is the number of elements in arr
     * Space - O(1)
     *
     * @param arr array of elements.
     * @return the majority element.
     */
    public static int majorityElement(int[] arr) {
        int flag = 0;
        int major = arr[0];
        for (int el : arr) {
            if (flag == 0) {
                major = el;
                flag++;
            } else if (el == major) {
                flag++;
            } else {
                flag--;
            }
        }
        return major;
    }

    /**
     * 7.
     * Using a max-heap and once we remove the root, k is decremented.
     * When k is finally 1, the current root is the kth biggest element of arr.
     * Time - O(n*log(n)) - n is the length of arr
     * Space - O(n)
     *
     * @param arr array of elements.
     * @param k   we want the kth biggest element.
     * @return kth biggest element of the arr.
     */
    public static int findKthBiggest(Integer[] arr, int k) {
        if (k >= arr.length) return -1;

        Queue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        pq.addAll(Arrays.asList(arr));
        while (k-- != 1) {
            pq.poll();
        }
        return pq.peek();
    }

    /**
     * Computing a dp matrix as dp[i][j] = sum(dp[m][n]),
     * where m <= i, n <= j and m can't be equal to i meanwhile n is equal to j.
     *
     * @param matrix given matrix we wanna compute dp for.
     * @return dp matrix.
     */
    private static int[][] computeDp(int[][] matrix) {
        int[][] dp = new int[matrix.length][matrix[0].length];

        // first line initialization
        for (int i = 0; i < matrix[0].length; i++) {
            dp[0][i] = matrix[0][i];
        }
        // compute sum on columns
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                dp[i][j] = dp[i - 1][j] + matrix[i][j];
            }
        }
        // compute sum on rows
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                dp[i][j] += dp[i][j - 1];
            }
        }

        return dp;
    }

    /**
     * 9.
     * We will use dynamic programming to solve this problem.
     * Firstly, we compute the dp matrix.
     * Having this new matrix of sums we can compute the sum of the given submatrix in O(1).
     * Time - O(N * M) - N rows, M columns (length of given matrix)
     * Space - O(N * M)
     *
     * @param matrix given matrix of NxM
     * @param coords list of tuples representing top left and bottom right corners of a given submatrix.
     * @return list of sums for each given submatrix
     */
    public static List<Integer> subMatrixSum(int[][] matrix, List<Tuple<Tuple<Integer>>> coords) {
        int[][] dp = computeDp(matrix);
        List<Integer> ans = new ArrayList<>();
        for (Tuple<Tuple<Integer>> elem : coords) {
            int current_ans = dp[elem.right().left()][elem.right().right()];

            // A B
            // C D
            // D is submatrix we want to find the sum of.
            // so we can subtract A B submatrix,
            // then A
            //      C submatrix, finally we add A submatrix again (because we subtracted it twice)

            // subtract elements that are not included in the submatrix.
            if (elem.left().left() > 0) {
                current_ans -= dp[elem.left().left() - 1][elem.right().right()];
            }
            if (elem.left().right() > 0) {
                current_ans -= dp[elem.right().left()][elem.left().right() - 1];
            }
            // Add again the submatrix that has been subtracted twice.
            if (elem.left().left() > 0 && elem.left().right() > 0) {
                current_ans += dp[elem.left().left() - 1][elem.left().right() - 1];
            }

            ans.add(current_ans);
        }
        return ans;
    }

    /**
     * 10.
     * We start from the right top corner.
     * If the current element is 0, we are moving to the next row.
     * Otherwise, we found the new row with most ones so we update the ans
     * and we are moving to the left with one position.
     * Using this technique, whenever we move down the rows
     * and find a 1 we know that row is the current ans.
     * Time - O(N + M) (matrix traversal) - N rows, M columns
     * Space - O(1)
     *
     * @param matrix given binary matrix of NxM.
     * @return the row with the most ones.
     */
    public static int findRowWithMostOnes(int[][] matrix) {
        int i = 0, j = matrix[0].length - 1, ans = -1;
        while (i != matrix.length && j != -1) {
            if (matrix[i][j] == 0) {
                i++;
            } else {
                j--;
                ans = i;
            }
        }
        return ans;
    }

    /**
     * Whenever a 0 is found on border we will visit all its 0 neighbors
     * and set all of them a temporary value (-1).
     * We are moving on 4 directions (up, left, down, right)
     * using fill algorithm based on dfs.
     *
     * @param matrix     given binary matrix
     * @param row        of 0 wanted cell
     * @param col        of 0 wanted cell
     * @param directions tuples of all 4 directions.
     */
    private static void floodFill(int[][] matrix, int row, int col, Tuple<Integer>[] directions) {
        matrix[row][col] = -1;
        for (Tuple<Integer> dir : directions) {
            int nextRow = row + dir.left(), nextCol = col + dir.right();
            if (nextRow >= 0 && nextRow <= matrix.length - 1
                    && nextCol >= 0 && nextCol <= matrix[0].length - 1
                    && matrix[nextRow][nextCol] == 0) {
                floodFill(matrix, nextRow, nextCol, directions);
            }
        }
    }

    /**
     * We want to replace all 0's which don't locate at borders
     * or connect to 0 at borders to 1.
     * To achieve that, we will mark all 0's (with -1) at borders and apply fill on 4 directions
     * for each of them so we can mark any 0 connected with the found 0's on borders.
     * Once we marked all needed 0's (with -1), the untouched 0's will be replaced with 1.
     * Time - O(N * M) - N rows, M columns.
     * Space - O(1)
     *
     * @param matrix given binary matrix
     * @return the matrix updated.
     */
    public static int[][] surroundedIslands(int[][] matrix) {
        Tuple<Integer>[] directions = new Tuple[]{
                new Tuple<>(0, 1),
                new Tuple<>(0, -1),
                new Tuple<>(1, 0),
                new Tuple<>(-1, 0)
        };
        // top and bottom rows
        for (int i = 0; i < matrix[0].length; i++) {
            if (matrix[0][i] == 0) {
                floodFill(matrix, 0, i, directions);
            }
            if (matrix[matrix.length - 1][i] == 0) {
                floodFill(matrix, matrix.length - 1, i, directions);
            }
        }
        // left and right columns
        for (int i = 1; i < matrix.length - 1; i++) {
            if (matrix[i][0] == 0) {
                floodFill(matrix, i, 0, directions);
            }
            if (matrix[i][matrix[0].length - 1] == 0) {
                floodFill(matrix, i, matrix[0].length - 1, directions);
            }
        }
        // replacing zeros
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][j] = 1;
                } else if (matrix[i][j] == -1) {
                    matrix[i][j] = 0;
                }
            }
        }
        return matrix;
    }

    public static void main(String[] args) {
        // TESTING
        // 1.
        assert lastWord("Ana are mere rosii si galbene").equals("si");
        assert lastWord("").equals("");
        assert lastWord("si siret singur").equals("siret");
        // 2.
        assert euclideanDistance(1, 5, 4, 1) == 5.0;
        assert euclideanDistance(0, 0, 0, 0) == 0.0;
        assert euclideanDistance(0, 0, 3, 4) == 5.0;
        // 3.
        assert scalarProduct1(new int[]{1, 0, 2, 0, 3}, new int[]{1, 2, 0, 3, 1}) == 4;
        assert scalarProduct2(new int[]{1, 0, 2, 0, 3}, new int[]{1, 2, 0, 3, 1}) == 4;
        assert scalarProduct1(new int[]{1, 0, 0, 0, 0, 0, 0, 0, 0, 2}, new int[]{0, 1, 0, 0, 0, 0, 0, 0, 2, 0}) == 0;
        assert scalarProduct2(new int[]{1, 0, 0, 0, 0, 0, 0, 0, 0, 2}, new int[]{0, 1, 0, 0, 0, 0, 0, 0, 2, 0}) == 0;
        assert scalarProduct1(new int[]{1, 0, 0, 3, 0, 0, 4, 0, 0, 2}, new int[]{0, 0, 0, 0, 5, 0, 4, 0, 0, 2}) == 20;
        assert scalarProduct2(new int[]{1, 0, 0, 3, 0, 0, 4, 0, 0, 2}, new int[]{0, 0, 0, 0, 5, 0, 4, 0, 0, 2}) == 20;
        assert scalarProduct1(new int[]{}, new int[]{}) == 0;
        assert scalarProduct2(new int[]{}, new int[]{}) == 0;
        // 4.
        assert occurredOnce("ana are ana are mere rosii ana").get(0).equals("mere");
        assert occurredOnce("ana are ana are mere rosii ana").get(1).equals("rosii");
        try {
            String catching = occurredOnce("ana are ana are mere rosii ana").get(2);
            assert false;
        } catch (IndexOutOfBoundsException ex) {
            assert true;
        }
        assert occurredOnce("") == null;
        assert occurredOnce("MaRe mare mic mic").size() == 2;
        // 5.
        assert repeatedValue1(new int[]{1, 2, 3, 4, 2}) == 2;
        assert repeatedValue2(new int[]{1, 2, 3, 4, 2}) == 2;
        assert repeatedValue2(new int[]{1, 1}) == 1;
        assert repeatedValue2(new int[]{1, 1}) == 1;
        assert repeatedValue2(new int[]{1, 2, 3, 4, 5, 6, 7, 5, 8, 9}) == 5;
        assert repeatedValue2(new int[]{1, 2, 3, 4, 5, 6, 7, 5, 8, 9}) == 5;
        // 6.
        assert majorityElement(new int[]{2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2}) == 2;
        assert majorityElement(new int[]{1, 1, 2, 2, 1, 1}) == 1;
        assert majorityElement(new int[]{1, 1, 2, 2, 2, 1, 1}) == 1;
        assert majorityElement(new int[]{1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 3, 3}) == 2;
        // 7.
        assert findKthBiggest(new Integer[]{7, 4, 6, 3, 9, 1}, 2) == 7;
        assert findKthBiggest(new Integer[]{7, 4, 6, 3, 9, 1}, 10) == -1;
        assert findKthBiggest(new Integer[]{7, 4, 6, 3, 9, 9}, 2) == 9;
        assert findKthBiggest(new Integer[]{7, 4, 7, 3, 9, 9}, 5) == 4;
        // 9.
        int[][] matrix = {{0, 2, 5, 4, 1},
                {4, 8, 2, 3, 7},
                {6, 3, 4, 6, 2},
                {7, 3, 1, 8, 3},
                {1, 5, 7, 9, 4}};
        List<Tuple<Tuple<Integer>>> coords = new ArrayList<>();
        Tuple<Integer> firstUpLeft = new Tuple<>(1, 1);
        Tuple<Integer> firstDownRight = new Tuple<>(3, 3);
        Tuple<Integer> secondUpLeft = new Tuple<>(2, 2);
        Tuple<Integer> secondDownRight = new Tuple<>(4, 4);
        coords.add(new Tuple<>(firstUpLeft, firstDownRight));
        coords.add(new Tuple<>(secondUpLeft, secondDownRight));
        assert subMatrixSum(matrix, coords).get(0) == 38;
        assert subMatrixSum(matrix, coords).get(1) == 44;

        Tuple<Integer> thirdUpLeft = new Tuple<>(0, 0);
        Tuple<Integer> thirdDownRight = new Tuple<>(0, 0);
        coords.add(new Tuple<>(thirdUpLeft, thirdDownRight));
        assert subMatrixSum(matrix, coords).get(2) == 0;

        Tuple<Integer> forthUpLeft = new Tuple<>(0, 0);
        Tuple<Integer> forthDownRight = new Tuple<>(2, 1);
        coords.add(new Tuple<>(forthUpLeft, forthDownRight));
        assert subMatrixSum(matrix, coords).get(3) == 23;
        // 10.
        int[][] matrix21 = {{0, 0, 0, 1, 1},
                {0, 1, 1, 1, 1},
                {0, 0, 1, 1, 1}};
        assert findRowWithMostOnes(matrix21) == 1;
        int[][] matrix22 = {{0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0}};
        assert findRowWithMostOnes(matrix22) == -1;
        // 11.
        int[][] matrix3 = {{1, 1, 1, 1, 0, 0, 1, 1, 0, 1},
                {1, 0, 0, 1, 1, 0, 1, 1, 1, 1},
                {1, 0, 0, 1, 1, 1, 1, 1, 1, 1},
                {1, 1, 1, 1, 0, 0, 1, 1, 0, 1},
                {1, 0, 0, 1, 1, 0, 1, 1, 0, 0},
                {1, 1, 0, 1, 1, 0, 0, 1, 0, 1},
                {1, 1, 1, 0, 1, 0, 1, 0, 0, 1},
                {1, 1, 1, 0, 1, 1, 1, 1, 1, 1}};
        int[][] expected_result = {{1, 1, 1, 1, 0, 0, 1, 1, 0, 1},
                {1, 1, 1, 1, 1, 0, 1, 1, 1, 1},
                {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                {1, 1, 1, 1, 1, 1, 1, 1, 0, 1},
                {1, 1, 1, 1, 1, 1, 1, 1, 0, 0},
                {1, 1, 1, 1, 1, 1, 1, 1, 0, 1},
                {1, 1, 1, 0, 1, 1, 1, 0, 0, 1},
                {1, 1, 1, 0, 1, 1, 1, 1, 1, 1}};
        int[][] result = surroundedIslands(matrix3);
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[0].length; j++) {
                assert result[i][j] == expected_result[i][j];
            }
        }
        // END OF TESTING
    }
}
