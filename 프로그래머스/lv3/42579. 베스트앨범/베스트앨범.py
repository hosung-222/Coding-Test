def solution(genres, plays):
    answer = []
    genre = {}
    for i in range(len(genres)):
        if genres[i] in genre:
            genre[genres[i]] += plays[i]
        else:
            genre[genres[i]] = plays[i]

    g = sorted(genre.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(g)):
        temp = {}
        for j in range(len(genres)):
            if genres[j] == g[i][0]:
                temp[j] = plays[j]

        t = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        
        for k, v in t[:2]:
            answer.append(k)
        
        
    return answer