def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

#더 발전된 방향
#for x, y in zip(a, b):
#   answer += x * y