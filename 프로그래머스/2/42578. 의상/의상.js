// 종류별로 최대 1가지 의상만 착용 가능, 하루에 최소 한 개의 의상 착용
// 종류가 다르면 여러 의상 착용 가능

function solution(clothes) {
    return Object.values(clothes.reduce((obj, t)=> {
        obj[t[1]] = obj[t[1]] ? obj[t[1]] + 1 : 1;
        return obj;
    } , {})).reduce((a,b)=> a*(b+1), 1)-1;    
}