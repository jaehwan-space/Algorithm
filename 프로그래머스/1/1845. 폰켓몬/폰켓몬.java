import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        // Set을 사용해 중복 제거
        HashSet<Integer> uniquePokemon = new HashSet<>();
        for (int num : nums) {
            uniquePokemon.add(num);
        }
        
        // 중복 제거된 폰켓몬 종류의 개수와 선택 가능한 최대 개수(N/2) 중 더 작은 값을 반환
        int maxSelectable = nums.length / 2;
        return Math.min(maxSelectable, uniquePokemon.size());
    }
}
