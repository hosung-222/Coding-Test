def solution(cacheSize, cities):
    cache = []
    runTimeCnt = 0
    if cacheSize == 0:
        return len(cities)*5
    
    for i in cities:
        i = i.lower()
        if i in cache:
            cache.remove(i)
            cache.append(i)
            runTimeCnt += 1
        elif len(cache) < cacheSize:
            cache.append(i)
            runTimeCnt += 5
        else:
            cache.pop(0)
            cache.append(i)
            runTimeCnt += 5
            
    return runTimeCnt
            