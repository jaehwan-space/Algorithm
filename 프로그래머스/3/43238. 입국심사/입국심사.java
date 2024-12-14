import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long left = 1; // 최소 시간
        long right = (long) Arrays.stream(times).max().getAsInt() * n; // 최대 시간
        long answer = right;

        while (left <= right) {
            long mid = (left + right) / 2; // 중간 시간
            long people = 0;

            // mid 시간 동안 처리 가능한 인원 계산
            for (int time : times) {
                people += mid / time;
            }

            if (people >= n) {
                // 모든 사람을 처리 가능: 시간을 줄임
                answer = mid;
                right = mid - 1;
            } else {
                // 처리 불가할 경우 시간을 늘림
                left = mid + 1;
            }
        }

        return answer;
    }
}