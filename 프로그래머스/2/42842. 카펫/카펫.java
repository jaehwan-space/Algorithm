class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow; // 카펫의 총 면적

        // 총 면적의 약수 중 가능한 가로(w), 세로(h) 조합 탐색
        for (int h = 1; h <= Math.sqrt(total); h++) {
            if (total % h == 0) { // h가 total의 약수인 경우
                int w = total / h; // 가로 길이

                // 노란색 영역의 조건 확인
                if ((w - 2) * (h - 2) == yellow) {
                    return new int[] {w, h}; // 가로, 세로 반환
                }
            }
        }

        return new int[0]; // 실행되지 않음 (항상 답이 존재한다고 했으므로)
    }
}