import sys
input = sys.stdin.read

def check():
    for i in range(1, N+1):
        temp = i
        for j in range(1, H+1):
            if arr[j][temp] == 1:  # 오른쪽으로 이동
                temp += 1
            elif arr[j][temp-1] == 1:  # 왼쪽으로 이동
                temp -= 1
        if temp != i:  # 시작과 끝이 다르면 실패
            return False
    return True

def dfs(depth, start):
    global ans
    if depth >= ans:  # 현재 추가한 사다리 수가 최소값 이상이면 중단
        return
    if check():  # 모든 세로선이 올바르면 최소값 갱신
        ans = depth
        return

    for i in range(start, len(position)):
        x, y = position[i]
        # 사다리 추가 가능한지 확인
        if not arr[x][y] and not arr[x][y-1] and not arr[x][y+1]:
            arr[x][y] = 1  # 사다리 추가
            dfs(depth + 1, i + 1)  # 다음 사다리 추가
            arr[x][y] = 0  # 사다리 제거

# 입력 처리
data = input().split()
N, M, H = map(int, data[:3])  # N: 세로선, M: 가로선, H: 가로선을 놓을 수 있는 높이

# 사다리 배열 초기화
arr = [[0] * (N+1) for _ in range(H+1)]

# 가로선 정보 입력
for i in range(M):
    x, y = map(int, data[3 + 2*i: 3 + 2*i + 2])
    arr[x][y] = 1

# 가능한 사다리 위치 저장
position = []
for i in range(1, H+1):
    for j in range(1, N):  # 가장 오른쪽 세로선 제외
        if arr[i][j] == 0:
            position.append((i, j))

ans = 4
dfs(0, 0)
print(ans if ans < 4 else -1)