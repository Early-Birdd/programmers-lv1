def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    answer += participant.pop()

    return answer

#회고
#sort()는 따로 갱신하지 않는다.
#["문자"] or ['문자'] 출력 => ['문자']
#"문자" or '문자' 출력 => 문자

# 더 발전된 방향
#import collections
#answer = collections.Counter(participant) - collections.Counter(completion) -> Counter({'key':개수, ~~}), 카운터 객체는 뺄셈 가능
#return list(answer.keys())[0] -> answer dictionary key값들의 list[0] 반환