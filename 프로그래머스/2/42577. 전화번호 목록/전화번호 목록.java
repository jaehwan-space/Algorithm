import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        // 전화번호 정렬
        Arrays.sort(phone_book);

        // 인접한 번호들 비교
        for (int i = 0; i < phone_book.length - 1; i++) {
            // 현재 번호가 다음 번호의 접두어인지 확인
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }

        return true;
    }
}