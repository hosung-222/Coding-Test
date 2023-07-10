def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


# 1(a),4(b)    3(x),3(y)    [a*x(3)+b*u(12), a*y(3)+b*v(12)], 
# 3(c),2(d)  * 3(u),3(v)  = [c*x(9)+d*u(6), c*y(9)+d*v(6)],
# 4(e),1(f)                 [e*x(12)+f*u(3), e*y(12)+f*v(3)]

#for 문 순서 
#1. ace 순회
#2. x,y 순회
#3. a,b 순회
