class Solution {
    public int solution(int[][] sizes) {
        int maxWidth = 0;  // 지갑의 가로 길이
        int maxHeight = 0; // 지갑의 세로 길이

        for (int[] size : sizes) {
            // 명함을 회전하여 큰 값은 가로, 작은 값은 세로로 정렬
            int width = Math.max(size[0], size[1]);
            int height = Math.min(size[0], size[1]);

            // 가로와 세로의 최대값 업데이트
            maxWidth = Math.max(maxWidth, width);
            maxHeight = Math.max(maxHeight, height);
        }

        // 지갑의 크기 = 가로 최대값 * 세로 최대값
        return maxWidth * maxHeight;
    }
}
