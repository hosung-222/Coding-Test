import re 
def solution(s):
    s = s.title()
    for i in s.split():
        if i[0].isalpha() == False:
            s = re.sub(i,i.lower(),s)
    return s