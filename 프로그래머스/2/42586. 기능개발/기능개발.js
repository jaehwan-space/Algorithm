// 

function solution(progresses, speeds) {
    const days = progresses.map((p, i) =>
        Math.ceil((100 - p) / speeds[i])
    );

    const result = [];
    let currentMaxDay = days[0];
    let count = 1;

    for (let i = 1; i < days.length; i++) {
        if (days[i] <= currentMaxDay) {
            count++;
        } else {
            result.push(count);
            currentMaxDay = days[i];
            count = 1;
        }
    }

    result.push(count); // 마지막 묶음 추가
    return result;
}