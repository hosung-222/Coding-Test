import math
def solution(fees, records):
    dic = {}
    pay = {}
    answer = []
    for i in records:
        x = i.split(" ")
        if x[2] == "IN":
            dic[x[1]] = x[0]
        else:
            a = x[0].split(":")
            b = dic[x[1]].split(":")
            hour = int(a[0]) - int(b[0])
            minute = int(a[1]) - int(b[1])
            total_time = hour*60 + minute
            if x[1] in pay:
                pay[x[1]] += total_time
            else:
                pay[x[1]] = total_time
    
            del dic[x[1]]
    
    if len(dic):
        for num, time in dic.items():
            t = time.split(":")
            hour = 23 - int(t[0])
            minute =  59- int(t[1])
            total_time = hour*60 + minute
            if num in pay:
                pay[num] += total_time
            else:
                pay[num] = total_time

    pay = sorted(pay.items())
    for num, time in pay:
        total_fees = 0
        if time> fees[0]:
            total_fees += fees[1]
            time -= fees[0]
            total_fees += math.ceil(time/fees[2]) * fees[3]
            answer.append(total_fees)
            
        else:
            answer.append(fees[1])
            
    return answer
    