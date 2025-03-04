function solution(numbers) {
    let answer = numbers.map(String) // 숫자를 문자열로 변환
                        .sort((a, b) => (b + a) - (a + b)) 
                        .join(""); 
    
    return answer[0] === "0" ? "0" : answer; // "0000" 같은 경우 "0" 반환
}