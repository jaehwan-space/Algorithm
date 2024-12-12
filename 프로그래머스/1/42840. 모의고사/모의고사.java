import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[][] people = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
        int[] count = {0, 0, 0};
        
        for(int i = 0; i < answers.length; i++){
            for(int p = 0; p < people.length; p++){
                if(answers[i] == people[p][i % people[p].length]){
                    count[p] += 1;
                }
            }
        }
        
        // 최대값 초기화
        int max = 0;
        List<Integer> indices = new ArrayList<>();
        
        // 첫 번째 반복으로 최대값 찾기
        for (int num : count) {
            if (num > max) {
                max = num;
            }
        }
        // 두 번째 반복으로 최대값의 인덱스 추가
        for (int i = 0; i < count.length; i++) {
            if (count[i] == max) {
                indices.add(i+1);
            }
        }
        
        // List를 배열로 변환
        return indices.stream().mapToInt(i -> i).toArray();
    }
}