'''
A 게임은 4x4 격자 모양의 보드의 가장 왼쪽 위에서 가장 오른쪽 아래로 말을 이동시키면서 각 구역에 있는 코인을 획득하는 게임입니다. 이때, 말은 오른쪽 또는 아래쪽으로만 이동할 수 있습니다.

예를 들어, 보드가 아래와 같다면

https://grepp-programmers.s3.amazonaws.com/files/ybm/66edaada7d/0ac1c4be-5e0c-459a-9b83-b7fccefb70cc.png

아래의 경우가 코인을 최대로 획득할 수 있는 경우이고 이때 획득하는 코인은 38입니다.

https://grepp-programmers.s3.amazonaws.com/files/ybm/1858f83a13/df5c905b-fbd4-40cf-a11b-587f6858932e.png

각 구역에서 획득할 수 있는 코인 양을 담은 2차원 리스트 board가 매개변수로 주어질 때, 최대로 획득할 수 있는 코인의 양을 return 하도록 solution 함수를 작성했습니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 한 줄만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.
'''


def solution(board):
    coins = [[0 for c in range(4)] for r in range(4)]
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                coins[i][j] = board[i][j]
            elif i == 0 and j != 0:
                coins[i][j] = board[i][j] + coins[i][j-1]
            elif i != 0 and j == 0:
                coins[i][j] = board[i][j] + coins[i-1][j]
            else:
                coins[i][j] = board[i][j] + max(coins[i][j], max(coins[i-1][j], coins[i][j-1]))
    answer = coins[3][3]
    return answer
