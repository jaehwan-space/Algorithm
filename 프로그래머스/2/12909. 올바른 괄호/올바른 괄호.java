import java.util.*;

class Solution {
    boolean solution(String s) {
        int balance = 0;
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                balance++;
            } else {
                balance--;
            }
            
            if (balance < 0) {
                // 닫는 괄호가 많아지는 경우
                return false;
            }
        }
        
        // 모든 괄호를 처리한 후 균형이 맞다면
        return balance == 0;
    }
}