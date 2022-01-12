#45점 풀이 - 런타임 에러 등
# def solution(n, lost, reserve):
#     answer = 0
#     count = [1] * (n + 1)
#
#     for i in reserve:
#         count[i] = 2
#
#     for lp in lost:
#         count[lp] = 0
#         if lp - 1 in reserve or lp + 1 in reserve:
#             if count[lp - 1] == 2:
#                 count[lp] = 1
#                 count[lp - 1] -= 1
#
#             elif count[lp + 1] == 2:
#                 count[lp] = 1
#                 count[lp + 1] -= 1
#
#     answer = count.count(1) + count.count(2) - 1
#
#     return answer

def solution(n, lost, reserve):
    answer = 0
    count = [1] * (n + 1)

    for i in reserve:
        count[i] = 2

    for lp in lost:
        if count[lp] == 2:
            count[lp] = 1
        else:
            count[lp] = 0

    for j in range(1, n + 1):
        if count[j] == 2 and count[j - 1] == 0:
            count[j], count[j - 1] = 1, 1
        elif count[j] == 0 and count[j - 1] == 2:
            count[j], count[j - 1] = 1, 1

    answer = count.count(1) + count.count(2) - 1

    return answer

#회고
#인덱스 에러를 방지하기 위해 왼쪽만 보게하는 전략
#여벌을 가진 사람이 도난당하는 경우를 추가하지 않아 에러가 발생하였다...