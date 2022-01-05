def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for i in new_id:
        if i.isalnum() or i in ['-', '_', '.']:
            answer += i

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:len(answer) - 1]

    if answer == '':
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[len(answer) - 1]

    return answer

#회고
#함수를 사용하고 갱신하지 않아 에러가 났다.
#전) new_id.lower()              (X)
#후) new_id = new_id.lower()     (O)

#4단계를 아래와 같이 구현하였을 때 입력이=.= 이면 두 번째 조건에서 빈 값이라 에러가 났다.
#if answer[0] == '.':
#     answer = answer[1:]
#if answer[len(answer) - 1] == '.':
#     answer = answer[:len(answer) - 1]

#헷갈리는 배열 사용
# a[:15] : a배열의 인덱스 0부터 14까지, 총 길이는 15
# 마지막 배열 인덱스를 지정할 때 -1을 사용할 것

#함수 이해가 부족했다.
#.lower() : 소문자로 변경
#.islower() : 소문자인지 확인
#.upper() : 대문자로 변경
#.isupper() : 대문자인지 확인
#.isalpha() : 문자열 속 알파벳 유무 여부
#.isdecimal() : 문자열 속 숫자(0~9) 유무 여부
#.isdigit() : 문자열 속 숫자(0~9, 지수 등) 유무 여부
#.isnumeric() : 문자열 속 숫자(숫자로 사용된 모든 문자) 유무 여부
#.isalnum() : 문자열 속 알파벳 및 숫자 유무 여부
#.replace(old, new) : old문자를new문자로 대체
#.startswith('a') : 문자열 시작이a 인가
#.endswith('a') : 문자열 끝이a 인가
#.strip() : 양쪽 공백 제거
#.lstrip() : 왼쪽 공백 제거
#.rstrip() : 오른쪽 공백 제거
#int(~) : ~를 정수형으로 변환
#str(~) : ~를 문자열로 변환

#더 발전된 방향
#적절한 함수 활용