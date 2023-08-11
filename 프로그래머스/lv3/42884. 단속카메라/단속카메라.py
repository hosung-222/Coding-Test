def solution(routes):
    routes.sort(key = lambda x : x[1])
    camara = []
    camara.append(routes[0][1])
    
    for i in range(1, len(routes)):
        if routes[i][0] > camara[-1]:
            camara.append(routes[i][1])
    print(camara)
    return len(camara)