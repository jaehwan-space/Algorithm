import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        // 결과를 저장할 리스트를 생성합니다.
        List<Integer> list = new ArrayList<>();

        // intervals의 범위에 따라 arr의 값을 추가
        for (int i = 0; i < intervals.length; i++) {
            for (int ii = intervals[i][0]; ii <= intervals[i][1]; ii++) {
                list.add(arr[ii]);
            }
        }

        // 리스트를 배열로 변환
        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }

        return result;
    }
}