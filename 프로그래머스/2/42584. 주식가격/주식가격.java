import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        // 배열 순회
        for (int i = 0; i < n; i++) {
            // 스택의 최상단 값과 현재 값을 비교
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int index = stack.pop();
                result[index] = i - index; // 떨어지기까지 걸린 시간
            }
            stack.push(i);
        }
        
        // 남은 인덱스 처리
        while (!stack.isEmpty()) {
            int index = stack.pop();
            result[index] = n - index - 1; // 끝까지 떨어지지 않음
        }
        
        return result;
    }
}