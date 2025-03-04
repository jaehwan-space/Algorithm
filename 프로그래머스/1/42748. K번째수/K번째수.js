function solution(array, commands) {
    return commands.map(e => {
        let sparr = array.slice(e[0] - 1, e[1]).sort((a, b) => a - b);
        return sparr[e[2] - 1];
    })
}