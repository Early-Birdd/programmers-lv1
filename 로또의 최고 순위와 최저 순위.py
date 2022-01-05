def solution(lottos, win_nums):
    answer = []
    max_count = 0
    min_count = 0

    for i in lottos:
        if i == 0:
            max_count += 1
        for j in win_nums:
            if i == j:
                max_count += 1
                min_count += 1

    max_rank = 7 - max_count
    min_rank = 7 - min_count

    if max_rank >= 6:
        max_rank = 6

    if min_rank >= 6:
        min_rank = 6

    answer.append(max_rank)
    answer.append(min_rank)

    return answer

#회고
#append를 적용하지 않고 마음대로 인덱스 할당을 해버렸다.
#answer[0] = max_rank
#answer[1] = min_rank

#더 발전된 방향
#count = lottos.count(0)
#if i in win_nums: