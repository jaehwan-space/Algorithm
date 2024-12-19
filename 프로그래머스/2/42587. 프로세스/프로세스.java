import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        // 큐에 (우선순위, 인덱스) 형태로 저장
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[] {priorities[i], i});
        }

        int order = 0; // 실행 순서
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            boolean hasHigherPriority = false;

            // 큐에 더 높은 우선순위가 있는지 확인
            for (int[] process : queue) {
                if (process[0] > current[0]) {
                    hasHigherPriority = true;
                    break;
                }
            }

            if (hasHigherPriority) {
                // 현재 프로세스를 다시 큐의 끝으로 이동
                queue.offer(current);
            } else {
                // 현재 프로세스를 실행
                order++;
                if (current[1] == location) {
                    return order; // 목표한 프로세스의 실행 순서 반환
                }
            }
        }
        return -1; // 이론적으로 도달하지 않음
    }
}