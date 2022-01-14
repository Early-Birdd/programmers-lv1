def solution(n):
    answer = 0
    result_r = ''

    while True:
        if n < 3:
            result_r += str(n)
            break
        result_r += str(n % 3)
        n //= 3

    check = result_r[::-1]
    for i in range(len(check)):
        answer += int(check[i]) * (3 ** i)

    return answer

#2
# def solution(n):
#     answer = 0
#     result = ''
#     x = 0
#
#     while n // 3 > 0:
#         re = n % 3
#         n //= 3
#         result = str(re) + result
#     result = str(n) + result
#
#     for i in result:
#         answer += int(i) * (3 ** x)
#         x += 1
#
#     return answer

#회고
#[::-1] => 역순 출력, 일반배열이면 .reverse() 도 가능
#while문에서 9,10줄을 if문 보다 먼저 처리하여 에러가 났다.
#9,10을 먼저 하게되면 3보다 작을경우 02, 01 이런식으로 되어 마지막 for문 지수 계산에서 에러가 발생한다.


#result = str(re) + result => 진법 계산결과 출력하는 아이디어
#진수를 따로 0으로 설정해두고 +1 씩 준다. - for문으로 진법결과를 처음부터 돌면서 함께 곱하면 원하는 결과