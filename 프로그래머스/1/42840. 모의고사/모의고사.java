import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        // 수포자의 정답 패턴 정의
        int[][] people = {
            {1, 2, 3, 4, 5},       // 1번 수포자
            {2, 1, 2, 3, 2, 4, 2, 5}, // 2번 수포자
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5} // 3번 수포자
        };

        // 각 수포자의 점수를 저장할 배열
        int[] scores = new int[3];

        // 정답 비교 및 점수 계산
        for (int i = 0; i < answers.length; i++) {
            for (int p = 0; p < people.length; p++) {
                // 현재 수포자의 패턴과 정답 비교
                if (answers[i] == people[p][i % people[p].length]) {
                    scores[p]++;
                }
            }
        }

        // 최고 점수 계산
        int maxScore = Arrays.stream(scores).max().getAsInt();

        // 최고 점수를 받은 수포자 찾기
        List<Integer> indices = new ArrayList<>();
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] == maxScore) {
                indices.add(i + 1); // 수포자 번호는 1부터 시작
            }
        }

        // 결과를 배열로 변환하여 반환
        return indices.stream().mapToInt(i -> i).toArray();
    }
}
