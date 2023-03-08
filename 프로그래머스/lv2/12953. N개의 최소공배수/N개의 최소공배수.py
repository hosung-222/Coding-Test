def solution(arr):
    
    start = arr[-1]
    minmum = start
    i = 1
    while True:
        i+= 1
        division = True
        for k in arr:
            if minmum % k != 0:
                division = False
        if division == True:
            return minmum
        else:
            minmum = start * i
        