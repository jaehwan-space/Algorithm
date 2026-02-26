def solution(genres, plays):
    answer = []
    
    album = {}
    genplays = {}
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]
        if not genre in album.keys():
            album[genre] = []
            genplays[genre] = 0
        album[genre].append([play, i])
        genplays[genre] += play
    genplays = sorted(genplays, key=lambda x:genplays[x], reverse=True)
    
    for i in genplays:
        album[i].sort(key=lambda x:(-x[0], x[1]))
        answer.append(album[i][0][1])
        if len(album[i]) >= 2:
            answer.append(album[i][1][1])

    return answer