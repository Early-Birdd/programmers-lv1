#런타임 에러 - 70점
# def solution(N, stages):
#     answer = []
#     dic = {}
#     person = {}
#     total = len(stages)
#
#     for i in range(1, N + 1):
#         person[i] = stages.count[i]
#
#     for i in range(N):
#         rank_value = stages.count(i + 1) / total
#         total -= person[i + 1]
#         dic[i + 1] = rank_value
#
#     answer = sorted(dic, key=lambda x: dic[x], reverse=True)
#
#     return answer

def solution(N, stages):
    answer = []
    total = len(stages)
    rank = {}

    for i in range(1, N + 1):
        if total == 0:
            rank[i] = 0
        else:
            person = stages.count(i)
            rank[i] = person / total
            total -= person

    answer = sorted(rank, key=lambda x: rank[x], reverse=True)

    return answer

#회고
#dictionary 정렬에서 lambda 사용법 숙지
#적절한 변수 사용