import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        // 결과를 저장할 리스트를 생성합니다.
        List<Integer> list = new ArrayList<>();
        
        // 정규 표현식: '0'과 '5'만 포함된 숫자에 매칭
        String regx = "^[^12346789]*$";
        
        for (int i = l; i <= r; i++) {
            // 숫자를 문자열로 변환하고 정규 표현식으로 필터링합니다.
            if (String.valueOf(i).matches(regx)) {
                list.add(i);
            }
        }
        
        // 리스트에 값이 존재하면 결과 배열을 생성하여 반환합니다.
        if (list.size() > 0) {
            int[] result = new int[list.size()];
            for (int i = 0; i < list.size(); i++) {
                result[i] = list.get(i);
            }
            return result;
        }
        
        // 리스트가 비어있다면 [-1]을 반환합니다.
        return new int[]{-1};
    }
}