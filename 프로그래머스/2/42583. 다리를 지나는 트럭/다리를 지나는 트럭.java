import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        int time = 0;              // 경과 시간
        int totalWeight = 0;       // 현재 다리 위 트럭들의 총 무게
        int index = 0;             // 대기 트럭 인덱스
        
        // 다리 길이를 유지하기 위해 초기 큐를 0으로 채운다.
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }
        
        while (!bridge.isEmpty()) {
            time++; // 시간 증가
            
            // 다리에서 트럭을 내린다
            totalWeight -= bridge.poll();
            
            // 대기 중인 트럭을 다리에 올릴 수 있으면 추가
            if (index < truck_weights.length) {
                if (totalWeight + truck_weights[index] <= weight) {
                    bridge.add(truck_weights[index]);
                    totalWeight += truck_weights[index];
                    index++;
                } else {
                    // 무게 초과 시 트럭 대신 0을 추가 (공간만 차지)
                    bridge.add(0);
                }
            }
        }
        
        return time;
    }
}