import heapq
def solution(book_time):
    book_time = sorted(book_time)
    rooms = []
    for s, e in book_time:
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms)
        x = (e.split(":"))
        x[1] = int(x[1]) + 10
        x[0] = int(x[0])
        
        if x[1] >= 60:
            x[1] -= 60
            x[0] = x[0] + 1
        if x[0] > 24:
            x[0] -= 24
        
        if x[0] < 10:
            x[0] = "0" + str(x[0])
        if x[1] <10:
            x[1] = "0" + str(x[1])
        
        newe = str(x[0])+ ":" + str(x[1])

        heapq.heappush(rooms, newe)
        
    return len(rooms)