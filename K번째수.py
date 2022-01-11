def solution(array, commands):
    answer = []

    first = []

    for command in commands:
        first = array[command[0] - 1:command[1]]
        first.sort()
        answer.append(first[command[2] - 1])

    return answer

#더 발전된 방향
#i, j, k = command

#sorted 활용
#sorted(array[~~])[]

#ex - array = [('a', 1), ('b', 2)]
#sorted(array, key = ??(len or abs 등), reverse = True)
#sorted+reverse => 정렬하고 뒤집기
#.reverse => 바로 뒤집기