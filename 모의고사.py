def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    answer = []

    for i in range(len(answers)):
        if one[i % len(one)] == answers[i]:
            count[0] += 1
        if two[i % len(two)] == answers[i]:
            count[1] += 1
        if three[i % len(three)] == answers[i]:
            count[2] += 1

    for i in range(3):
        if count[i] == max(count):
            answer.append(i + 1)

    return answer

#회고
#elif를 써서 걸리게 만들어 오류 발생 -> 각각 if로 처리해야한다.
#비교를 할 때 %연산 활용에 유의