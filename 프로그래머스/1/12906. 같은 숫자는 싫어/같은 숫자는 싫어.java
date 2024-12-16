import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        // 결과 리스트
        List<Integer> result = new ArrayList<>();
        
        int prev = -1; // 이전 값을 저장
        for (int num : arr) {
            if (num != prev) { // 이전 값과 다른 경우만 추가
                result.add(num);
                prev = num; // 이전 값 저장
            }
        }
        
        // List를 배열로 변환
        return result.stream().mapToInt(i -> i).toArray();
    }
}