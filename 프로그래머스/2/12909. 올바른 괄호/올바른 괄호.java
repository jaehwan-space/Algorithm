import java.util.*;

class Solution {
    boolean solution(String s) {
        int count = 0;
        // 문자 배열 생성하기
        String[] stringArray = s.split("");

        for(int i = 0; i < stringArray.length; i++){
            if (stringArray[i].equals("(")) {
                count += 1;
            } else if (stringArray[i].equals(")")) {
                count -= 1;
            }

            if(count < 0){
                return false;
            }
        }
        
        if(count == 0){
            return true;
        }else{
            return false;
        }
    }
}