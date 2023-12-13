"""<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는
 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
 <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를
 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input()))
home_cnt = []


def dfs(x: int, y: int, cnt: int):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return 0
    if maps[x][y] == '1':
        maps[x][y] = '0'
        cnt += 1
        cnt += dfs(x - 1, y, 0)
        cnt += dfs(x, y - 1, 0)
        cnt += dfs(x + 1, y, 0)
        cnt += dfs(x, y + 1, 0)
        return cnt
    return 0


result = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == '1':
            home_cnt.append(dfs(i, j, 0))
            result += 1
print(result)
home_cnt = sorted(home_cnt)
for i in home_cnt:
    print(i)
