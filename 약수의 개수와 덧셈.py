def a(i):
    list = []
    for check in range(1, i + 1):
        if i % check == 0:
            list.append(check)
    return len(list)


def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        if a(i) % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer

#회고
#약수 구하는 def 설정