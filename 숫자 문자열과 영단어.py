def solution(s):
    answer = 0

    if s.isdigit():
        answer = int(s)
        return answer

    s = s.replace("zero", "0")
    s = s.replace("one", "1")
    s = s.replace("two", "2")
    s = s.replace("three", "3")
    s = s.replace("four", "4")
    s = s.replace("five", "5")
    s = s.replace("six", "6")
    s = s.replace("seven", "7")
    s = s.replace("eight", "8")
    s = s.replace("nine", "9")

    answer += int(s)

    return answer

#회고
# s.replace(~) 사용 후 갱신을 하지 않아 에러가 났다
# s = s.replace(~)

#더 발전된 방향
#dictionary 사용
# dic = {key:value, "zero":"0", ~~ }
# 해당 key의 value 확인 => dic[key] => value
# dictionary 추가 => dic[추가 key] = 추가 value
# dictionary 삭제 => del dic[삭제 key]
# dictionary에 포함된 key 확인 => key in dic
# key만 => dic.keys()
# value만 => dic.values()
# key, value => dic.items()
# dictionary key 존재 여부에 따른 출력 => dic.get(key, "key 없음") => key 존재하면 value 반환, 없으면 "key 없음" 반환
# dictionary 요소 전부 삭제 => dic.clear() => {}
# 특정 키 값 반환 후 삭제 => dic.pop(key) => value

# dictionary for문
# for key, value in dic.items():
#     ~~~