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