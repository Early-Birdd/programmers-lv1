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