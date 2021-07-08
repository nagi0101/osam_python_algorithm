'''
스택 두개를 이용해 Queue 자료구조를 만들었을 때, Queue 자료 구조의 pop(또는 dequeue) 함수를 구현하려합니다. Queue란 먼저 삽입한 데이터를 먼저 빼내는 자료구조를 뜻합니다. pop 함수를 만들기 위해 다음과 같이 프로그램 구조를 작성했습니다.

1. 스택2가 비었다면 스택1에 아무것도 남지 않을때까지 스택1에서 pop한 값을 스택2에 push 한다.
2. 스택2에서 pop한 값을 리턴한다.
두 리스트 stack1, stack2가 매개변수로 주어질 때, 두 리스트를 스택으로 이용해 Queue 자료 구조의 pop 함수를 구현하려합니다. 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

※ 리스트 index가 0인 부분을 스택의 bottom으로 생각합니다.
'''


def func_a(stack):
    return stack.pop()


def func_b(stack1, stack2):
    while not func_c(stack1):
        item = func_a(stack1)
        stack2.append(item)


def func_c(stack):
    return (len(stack) == 0)


def solution(stack1, stack2):
    if func_c(stack2):
        func_b(stack1, stack2)

    answer = func_a(stack2)
    return answer
