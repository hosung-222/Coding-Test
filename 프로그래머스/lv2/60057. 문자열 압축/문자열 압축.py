def solution(s):
    arr =[]
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp=s[:i]
        # 현재 문자열을 i 만큼 자르면서 압축 문자열 만들기
        for j in range(i, len(s)+i, i):
            #현재 문자열 == 이전 문자열
            if tmp==s[j:i+j]:
                cnt+=1
            #이전 문자열과 다른경우
            else:
                #반복횟수가 1이아닌경우 반복횟수와 문자열 추가
                if cnt!=1:
                    b = b + str(cnt)+tmp
                #반복횟수가 1인 경우 문자열 추가
                else:
                    b = b + tmp
                # 현재 문자열로 초기화
                tmp=s[j:j+i]
                cnt = 1
            
        arr.append(len(b))
                       
    return min(arr)

