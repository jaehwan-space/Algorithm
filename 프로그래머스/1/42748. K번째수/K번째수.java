import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int index = 0; index < commands.length; index++) {
            int i = commands[index][0]; // 시작 인덱스
            int j = commands[index][1]; // 끝 인덱스
            int k = commands[index][2]; // k번째 값

            // 1. i번째부터 j번째까지 자름 (배열은 0-based, i와 j는 1-based라 인덱스 조정 필요)
            int[] slicedArray = Arrays.copyOfRange(array, i - 1, j);

            // 2. 정렬
            Arrays.sort(slicedArray);

            // 3. k번째 수를 결과 배열에 추가 (k는 1-based라 인덱스 조정 필요)
            answer[index] = slicedArray[k - 1];
        }

        return answer;
    }
}