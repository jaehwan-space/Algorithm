function solution(clothes) {
    let count = new Map();
    let object = [];
    
    for([,type] of clothes){
        count.set(type, count.has(type)?count.get(type)+1:1);
    }
    
    for([,v] of count){
        object.push(v+1);
    }
    
    return object.reduce((t,e)=>t * e, 1) - 1;
}