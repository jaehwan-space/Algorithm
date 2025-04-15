// 장르 별로 가장 많이 재생된 음악 2개 앨범에 수록
// 장르 내에서 재생 횟수가 같다면 고유번호가 낮은 노래로 수록
// 노래가 먼저 담기는 순서는 장르에서 총 재생된 횟수가 큰 것부터
function solution(genres, plays) {
    const genreMap = new Map();       // 장르별 노래 목록
    const genreTotalPlays = new Map(); // 장르별 총 재생 수

    // 장르별로 데이터 정리
    genres.forEach((genre, i) => {
        const play = plays[i];
        
        // 노래 목록 저장
        if (!genreMap.has(genre)) genreMap.set(genre, []);
        genreMap.get(genre).push({ id: i, play });

        // 총 재생 수 계산
        genreTotalPlays.set(genre, (genreTotalPlays.get(genre) || 0) + play);
    });
    
     // 장르 정렬
    const sortedGenres = [...genreTotalPlays]
        .sort((a, b) => b[1] - a[1])
        .map(entry => entry[0]);
    const result = [];

    // 각 장르에서 상위 2곡씩 추출
    for (const genre of sortedGenres) {
        const songs = genreMap.get(genre);

        // 재생 수 내림차순 → 고유번호 오름차순 정렬
        songs.sort((a, b) => {
            if (b.play !== a.play) return b.play - a.play;
            return a.id - b.id;
        });

        // 상위 2개만 push
        result.push(...songs.slice(0, 2).map(song => song.id));
    }

    return result;
}