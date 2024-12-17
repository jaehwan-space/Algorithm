import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 기능 개발 남은 일수
        int[] days = new int[progresses.length]; 
        
        // 각 작업의 남은 일수 계산
        for (int i = 0; i < progresses.length; i++) {
            days[i] = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
        }
        
        List<Integer> result = new ArrayList<>();
        int count = 1; // 배포되는 기능의 수
        int current = days[0];
        
        // 배열 순회하며 배포 처리
        for (int i = 1; i < progresses.length; i++) {
            if (days[i] <= current) { 
                // 현재 기준 일수 안에 끝나는 경우
                count++;
            } else {
                // 새로운 기준이 등장하면 배포 진행
                result.add(count); // 현재까지의 기능 개수 저장
                current = days[i]; // 기준 업데이트
                count = 1; // 배포 기능 수 초기화
            }
        }
        
        // 마지막 배포 처리
        result.add(count);
        
        // List를 배열로 변환하여 반환
        return result.stream().mapToInt(i -> i).toArray();
    }
}