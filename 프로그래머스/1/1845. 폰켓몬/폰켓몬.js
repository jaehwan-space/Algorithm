function solution(nums) {
    const max = nums.length / 2;
    const arr = new Set(nums).size;
    
    return max > arr ? arr : max;
}