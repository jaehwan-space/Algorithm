import java.util.*;

class Solution {
    // 순열 생성 함수
    private void generatePermutations(String prefix, String remaining, Set<Integer> numberSet) {
        if (!prefix.isEmpty()) {
            numberSet.add(Integer.parseInt(prefix));
        }
        for (int i = 0; i < remaining.length(); i++) {
            generatePermutations(
                prefix + remaining.charAt(i),
                remaining.substring(0, i) + remaining.substring(i + 1),
                numberSet
            );
        }
    }

    // 소수 판별 함수
    private boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
    
    public int solution(String numbers) {
        // 중복 없이 숫자를 저장할 Set
        Set<Integer> numberSet = new HashSet<>();
        // 모든 가능한 숫자 조합 생성
        generatePermutations("", numbers, numberSet);

        // 소수 개수 카운트
        int count = 0;
        for (int num : numberSet) {
            if (isPrime(num)) {
                count++;
            }
        }

        return count;
    }
}