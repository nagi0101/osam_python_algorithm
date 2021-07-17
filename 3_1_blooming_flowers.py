'''
문제 설명
정사각형 크기 격자 모양 정원에 칸마다 핀 꽃 또는 피지 않은 꽃을 심었습니다. 이 정원의 꽃이 모두 피는 데 며칠이 걸리는지 알고 싶습니다. 핀 꽃은 하루가 지나면 앞, 뒤, 양옆 네 방향에 있는 꽃을 피웁니다.

현재 정원의 상태를 담은 2차원 리스트 garden이 주어졌을 때, 모든 꽃이 피는데 며칠이 걸리는지 return 하도록 solution 함수를 작성해주세요.


매개변수 설명
현재 정원 상태를 담은 2차원 리스트 garden이 solution 함수의 매개변수로 주어집니다.

정원의 한 변의 길이는 2 이상 100 이하입니다.
정원 상태를 담은 2차원 리스트 garden의 원소는 0 또는 1 입니다.
이미 핀 꽃은 1로 아직 피지 않은 꽃은 0으로 표현합니다.
정원에 최소 꽃 한 개는 피어 있습니다.
'''


def sum2DMatrix(matrix):
    sum = 0;
    
    for row in matrix:
        for element in row:
            sum += element
            
    return sum


def sizeOf2DMatrix(matrix):
    return len(matrix) * len(matrix[0])


def checkAllFlowersBloomed(garden):
    '''
    행렬의 각 요소의 합과 행렬의 크기가 같은지를 비교하여
    모든 꽃이 피었는지를 검사한다.
    '''
    return sum2DMatrix(garden) == sizeOf2DMatrix(garden)


def bloom(garden, row, col):
    '''
    garden 행렬의 (row, col) 위치에 있는 꽃의 
    상/하/좌/우에 위치한 꽃을 1로 설정한다.
    '''
    MAX_COL = len(garden) - 1
    MAX_ROW = len(garden[0]) - 1
    
    # up
    garden[max(row - 1, 0)][col] = 1
    # down
    garden[min(row + 1, MAX_ROW)][col] = 1
    # left
    garden[row][max(col - 1, 0)] = 1
    # right
    garden[row][min(col + 1, MAX_COL)] = 1

def solution(garden):
    day = 0;
    
    while(not checkAllFlowersBloomed(garden)):
        # 이번 시도에 피워야 할 꽃들의 정보를 저장한다.
        flowers_have_to_bloom = []
        
        # 이번 시도에 bloom 함수를 실행해야 하는 꽃을 flowers_have_to_bloom에 append한다.
        for i in range(len(garden)):
            for k in range(len(garden[0])):
                if garden[i][k] == 1:
                    flowers_have_to_bloom.append({"row": i, "col": k})
        
        # flowers_have_to_bloom의 모든 꽃에 bloom 함수를 실행한다.
        for flower in flowers_have_to_bloom:
            bloom(garden, flower["row"], flower["col"])
        
        day += 1
        
    return day

'''
테스트 1 〉	통과 (0.57ms, 10.3MB)
테스트 2 〉	통과 (1.94ms, 10.3MB)
테스트 3 〉	통과 (24.83ms, 11.6MB)
테스트 4 〉	통과 (141.02ms, 12.2MB)
테스트 5 〉	통과 (157.37ms, 11.5MB)
'''


def solution2(garden):
    day = 0;
    
    while(not checkAllFlowersBloomed(garden)):
        # 이번 시도에 피워야 할 꽃들의 정보를 저장한다.
        flowers_have_to_bloom = []
        MAX_COL = len(garden) - 1
        MAX_ROW = len(garden[0]) - 1
        
        # 현재 피어있는 모든 꽃을 flowers_have_to_bloom에 append한다.
        for i in range(len(garden)):
            for k in range(len(garden[0])):
                is_up_flower_bloomed = garden[max(i - 1, 0)][k] == 1
                is_down_flower_bloomed = garden[min(i + 1, MAX_ROW)][k] == 1
                is_left_flower_bloomed = garden[i][max(k - 1, 0)] == 1
                is_right_flower_bloomed = garden[i][min(k + 1, MAX_COL)] == 1
                
                
                is_flower_have_to_bloom = (
                    garden[i][k] == 1 and (
                        not is_up_flower_bloomed
                        or not is_down_flower_bloomed
                        or not is_left_flower_bloomed
                        or not is_right_flower_bloomed ))
                if is_flower_have_to_bloom:
                    flowers_have_to_bloom.append({"row": i, "col": k})
        
        # flowers_have_to_bloom의 모든 꽃에 bloom 함수를 실행한다.
        for flower in flowers_have_to_bloom:
            bloom(garden, flower["row"], flower["col"])
        
        day += 1
        
    return day
'''
테스트 1 〉	통과 (0.51ms, 10.4MB)
테스트 2 〉	통과 (2.12ms, 10.3MB)
테스트 3 〉	통과 (25.40ms, 10.8MB)
테스트 4 〉	통과 (161.83ms, 10.2MB)
테스트 5 〉	통과 (162.85ms, 10.4MB)
'''