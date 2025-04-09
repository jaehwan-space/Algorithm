function solution(arr)
{
    let result = [];
    
    arr.forEach((val,idx) => {
        if(arr[idx] !== arr[idx+1]) result.push(val);
    });
    
    return result
}