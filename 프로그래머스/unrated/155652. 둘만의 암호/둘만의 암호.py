def solution(s, skip, index):
    set_skip = set(skip)
    arr = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in set_skip:
        arr = arr.replace(i , "")
        
    for i in s:
        result += arr[(arr.index(i)+index) % len(arr)]
    return result
        
