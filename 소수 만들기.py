from itertools import combinations

def solution(nums):
    answer = 0

    for check in combinations(nums, 3):
        for i in range(2, sum(check)):
            if sum(check) % i == 0:
                result = False
                break
            else:
                result = True
        if result:
            answer += 1

    return answer

#회고
#from itertools import combinations 에서의 combinations 사용법 숙지
#break를 넣지않아 오답이 나왔다.