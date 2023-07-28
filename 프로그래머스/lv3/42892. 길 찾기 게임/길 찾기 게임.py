import sys
sys.setrecursionlimit(10**6)
def preorder(top, left, fanswer):
    n = top[0] # 루트노드 저장
    index = left.index(n) #중심 노드 지정
    arr_left, arr_right =[] , []

    for i in range(1, len(top)):
        if n[0] > top[i][0]: #X값 비교해서 작으면 왼쪽 
            arr_left.append(top[i])
        else:
            arr_right.append(top[i])
    
    fanswer.append(n[2]) #루트 노드 번호 저장
    if len(arr_left) > 0:
        preorder(arr_left, left[:index], fanswer)
    if len(arr_right) > 0:
        preorder(arr_right, left[index+1:], fanswer)
        
def postorder(top, left, sanswer):
    n = top[0]
    index = left.index(n)
    arr_left, arr_right =[] , []
    
    for i in range(1, len(top)):
        if n[0] > top[i][0]: #X값 비교해서 작으면 왼쪽 
            arr_left.append(top[i])
        else:
            arr_right.append(top[i])
            
    if len(arr_left) > 0:
        postorder(arr_left, left[:index], sanswer)
    if len(arr_right) > 0:
        postorder(arr_right, left[index+1:], sanswer)
    
    sanswer.append(n[2])
    
def solution(nodeinfo):
    fanswer, sanswer = [], []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
        
    top = sorted(nodeinfo, key = lambda x : (-x[1],x[0])) #루트노드부터 정렬
    left = sorted(nodeinfo) #왼쪽부터 정렬
    preorder(top, left, fanswer)
    postorder(top, left, sanswer)
    return [fanswer, sanswer]