def solution(players, callings):
    dic = {player : index for index, player in enumerate(players)}
    
    for call in callings:
        i = dic[call]
        players[i], players[i-1] = players[i-1], players[i]
        dic[players[i]] = i
        dic[players[i-1]] = i-1
        
    return players
    