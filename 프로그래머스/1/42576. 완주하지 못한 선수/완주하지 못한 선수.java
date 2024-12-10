import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        
        // 참가자의 이름과 등장 횟수를 기록
        for (String person : participant) {
            map.put(person, map.getOrDefault(person, 0) + 1);
        }
        
        // 완주한 사람의 이름을 감소
        for (String person : completion) {
            map.put(person, map.get(person) - 1);
        }
        
        // 완주하지 못한 사람을 찾기
        for (String key : map.keySet()) {
            if (map.get(key) > 0) {
                return key; // 등장 횟수가 1 이상인 이름 반환
            }
        }
        
        return ""; // 논리적으로 이 부분은 도달하지 않음
    }
}