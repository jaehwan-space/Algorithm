import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int k) {
        // 동적으로 값을 저장하기 위해 ArrayList 사용
        ArrayList<Integer> multiples = new ArrayList<>();
        
        // 1 이상 n 이하의 정수 중 k의 배수 찾기
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                multiples.add(i);
            }
        }
        
        // ArrayList를 배열로 변환
        int[] answer = new int[multiples.size()];
        for (int i = 0; i < multiples.size(); i++) {
            answer[i] = multiples.get(i);
        }
        
        return answer;
    }
}
