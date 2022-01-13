from collections import Counter

def solution(nums):
    return min(len(nums) / 2, len(Counter(nums)))


#회고
#아이디어 필요
#combinations로 접근했으나 실패
#len(Counter()) -> 서로 다른 것의 개수

#set은 중복제거 집합
#인덱스로 찍으려면 list씌우기, 아니면 pop 사용