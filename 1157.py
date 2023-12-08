"""
알파벳 대소문자로 된 단어가 주어지면,
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
단, 대문자와 소문자를 구분하지 않는다.
"""
word = str(input().upper())
lst = list(set(word))
cnt = []
for i in lst:
    cnt.append(word.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(lst[cnt.index(max(cnt))])
