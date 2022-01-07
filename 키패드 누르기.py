def solution(numbers, hand):
    answer = ''

    position = {1: [1, 1], 2: [1, 2], 3: [1, 3],
                4: [2, 1], 5: [2, 2], 6: [2, 3],
                7: [3, 1], 8: [3, 2], 9:[3, 3],
               '*':[4, 1], 0: [4, 2], '#': [4, 3]}

    l_po = [1, 4, 7]
    r_po = [3, 6, 9]
    l = [4, 1]
    r = [4, 3]

    for num in numbers:
        if num in l_po:
            answer += 'L'
            l = position[num]

        elif num in r_po:
            answer += 'R'
            r = position[num]

        else:
            cen = position[num]
            l_distance = abs(l[0] - cen[0]) + abs(l[1] - cen[1])
            r_distance = abs(r[0] - cen[0]) + abs(r[1] - cen[1])

            if l_distance > r_distance:
                answer += 'R'
                r = position[num]
            elif r_distance > l_distance:
                answer += 'L'
                l = position[num]
            else:
                if hand == "right":
                    answer += 'R'
                    r = position[num]
                else:
                    answer += 'L'
                    l = position[num]

    return answer

#회고
#왼손, 오른손 시작위치를 설정하지 않아 에러발생
#거리 계산 시 abs
#dictionary를 이용한 행렬 설정