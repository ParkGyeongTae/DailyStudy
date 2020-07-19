#print("Hello World")
#print("Mary's cosmetics")
#print("C:\\Windows")
#print("안녕하세요.\n만나서\t\t반갑습니다.")
#print("오늘은", "일요일")
#print("naver", "kakao", "sk", "samsung", end = ";")
#print("naver", "kakao", "sk", "samsung", sep = ";")
#print("naver", "kakao", "sk", "samsung", sep = "\")
#print("first", "second")
#print("first");print("second")
#print("first", end = " ");print("second")
#print(5/3)
'''
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
'''
'''
시가총액 = 29800000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
'''
'''
s = "hello"
t = "python"
print(s+"!", t)
'''
'''
8
'''
'''
a = "132"
print(a, type(a))
'''
'''
num_str = "720"
num_int = int(num_str)
print(num_int, type(num_int))
'''
'''
num = 100
result = str(num)
print(result, type(result))
'''
'''
data = "15.79"
data = float(data)
print(data, type(data))
'''
'''
year = "2020"
print(int(year)-1)
print(int(year)-2)
print(int(year)-3)
'''
'''
월 = 48584
총금액 = 월 * 36
print(총금액)
'''
'''
letters = "python"
#          012345
print(letters[0], end = "")
print(letters[2])
'''
'''
license_plate = "24가 2210"
#            0 1 2 3 4 5 6 7 8
print(license_plate[-4:])
'''
'''
string = "홀짝홀짝홀짝"
print(string[0],string[2],string[4], sep = "")
'''
'''
string = "홀짝홀짝홀짝"
print(string[0:6:2])
'''
'''
string = "PYTHON"
print(string[::-1])
'''
'''
phone_number = "010-1111-2222"
a = phone_number.replace("-", " ")
print(a)
'''
'''
phone_number = "010-1111-2222"
a = phone_number.replace("-", " ")
print(phone_number)
print(a)
'''
'''
url = "http://sharebook.kr"
print(url[-2:])
'''
'''
lang = "python"
lang[0] = 'P'
print(lang)
'''
'''
string = "abcdef2a354a32a"
a = string.replace("a", "A")
print(string)
print(a)
'''
'''
string = "abcd"
string = string.replace('b', "B")
print(string)
print(a)
'''
'''
a = "3"
b = "4"
print(a+b)
'''
'''
print("Hi" * 3)
'''
#33
'''
print("-" * 80)
'''
#34
'''
t1 = "python"
t2 = "java"
t = t1 + ' ' + t2 + ' '
print(t * 5)
'''
#35
'''
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2))
'''
#36
'''
name1 = "김철수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : {} 나이 : {}".format(name1,age1))
print("이름 : {} 나이 : {}".format(name2,age2))
'''
#37
'''
name1 = "김철수"
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")
'''
#38
'''
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',', '')
print(int(상장주식수))
'''
#39
'''
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
'''
#40
'''
data = "    삼성전자    "
data = data.strip()

print(data, len(data), type(data))
'''
#41
'''
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)
'''
#42
'''
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)
'''
#43
'''
a = "hello"
a = a.capitalize()
print(a)
'''
#44
'''
file_name = "보고서.xlse"
file_name = file_name.endswith("xlse")
print(file_name)
'''
#45
'''
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx","xls")))
'''
#46
'''
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020_"))
'''
#47
# 문자열을 분리하는 함수
'''
a = "hello world"
print(a.split())
'''
#48
# btc와 krw로 분리하기
# _ 기준으로 분리하기
'''
ticker = "btc_krw"
print(ticker.split("_"))
'''
# 049
'''
data = "2020-05-01"
print(data.split("-"))
'''
# 050
'''
data = "039490    "
print(data.strip())
'''
'''
x = 1
y = 2

print(x)
print(y)

z = "안녕"

print(z)
'''
'''
x = 1
y = 2
z = 1.2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x % y)
'''
'''
x = "hello"
y = 'bye'

z = """
안녕하세요
저는 ... 입니다
"""

print(z)
'''
'''
print("너 혹시 몇 살이니? " + str(4))
'''

# x = 4
# y = "4"

# print(str(x)+y)
# print(x+int(y))

# x = True
# y = False

# print(x)
# print(y)

###

# if not 0 > 0 or 2 > 1:
#     print("hello")

# x = 3
# if x > 5:
#     print("hello")
# elif x == 3:
#     print("bye")
# else:
#     print("hi")

# def chat():
#     print("철수 : 안녕? 너는 몇 살이니?")
#     print("영희 : 나? 나는 20살이야")

# chat()
# chat()
# chat()
# chat()

# def chat(name1, name2, age):
#     print("%s : 안녕? 너는 몇 살이니?" % name1)
#     print("%s : 나? 나는 %d살이야." % (name2,age))

# chat("알렉스","윤하",10)
# chat("철수","영희",30)

# def dsum(a,b):
#     result = a + b
#     return result

# d = dsum(1, 2)
# print(d)

# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕"이라고 말해라
# 나이가 10살에서 20살 사이면 "안녕하세요"라고 말해라
# 그 외에는 안녕하십니까 라고 말해라

# def sayhello(name, age):
#     if age < 10:
#         print("안녕" + name)
#     elif age < 20 and age >= 10:
#         print("안녕하세요" + name)
#     else:
#         print("안녕하십니까?" + name)

# sayhello("경태", 5)
# sayhello("알렉스", 10)
# sayhello("윤하", 40)

# print("철수 : 안녕 영희야 뭐해?")
# print("영희 : 안녕 철수야 그냥 있어")

# for, while

# for i in range(3):
#     print(i)
#     print("철수 : 안녕 영희야 뭐해?")
#     print("영희 : 안녕 철수야 그냥 있어.")

# i = 0
# while i < 3:
#     print(i)
#     print("철수 : 안녕 영희야 뭐해?")
#     print("영희 : 안녕 철수야 그냥 있어.")
#     i = i + 1

# i = 0

# while True:
#     print(i)
#     print("철수 : 안녕 영희야 뭐해?")
#     print("영희 : 안녕 철수야 그냥 있어.")
#     i = i + 1

#     if i > 3:
#         break

# for i in range(3):
#     print(i)
#     print("철수 : 안녕 영희야 뭐해?")
#     print("영희 : 안녕 철수야 나는 그냥 있어.")

#     continue

#     print("워니 : 안녕 철수야 영희야")

# print("Hello world")

# print("강한친구 대한육군")
# print("강한친구 대한육군")

# print("고\\")
# print("양\\")
# print("이\\")

# input_data = input().split(' ')
# a = int(input_data[0])
# b = int(input_data[1])
# print(a + b)

# input_data = input().split(' ')
# a = int(input_data[0])
# b = int(input_data[1])
# print(a / b)

# x = 0

# while x < 10:
#     print(x)
#     print("한자리수")
#     x = x + 1

#     if x > 5:
#         break

# 학생의 점수를 출력하는 프로그램

# try:
#     grade = int(input("Type your grade : "))
# except:
#     print("Error")

# else:
#     if grade > 100 or grade < 0:
#         print("Error")
#     elif grade >= 90:
#         print("A")
#     elif grade >= 80:
#         print("B")
#     elif grade >= 70:
#         print("C")
#     elif grade >= 60:
#         print("D")
#     else:
#         print("F")

# from datetime import *

# now = datetime.now()

# print("now date and time : " + str(now))
# print("now year : " + str(now.year))
# print("now month : " + str(now.month))
# print("now day : " + str(now.day))
# print("now hour : " + str(now.hour))
# print("now min : " + str(now.minute))
# print("now second : " + str(now.second))
# print("now date : {} {} {}".format(now.year,now.month,now.day))

# x = list()
# y = []

# print(x)
# print(y)

# x = [4,2,3,1]
# y = ["hello","there"]

# if "hello" in y:
#     print("hello 가 있어요")

# mutable vs immutable
# list는 가변, tuple은 불변

# x = {
#     0 : "hello",
#     1 : "Hello",
#     "age" : 20,
#     }

# x["school"] = "한빛"

# print(x)

# fruit = ["사과","사과","바나나","바나나","딸기","키위","복숭아","복숭아","복숭아"]

# d = {}

# for f in fruit:
#     if f in d:
#         d[f] = d[f] + 1
#     else:
#         d[f] = 1

# print(d)

# print("나는 %d살 입니다." % 20)
# print("%s %d살 입니다." % ("나는", 20))
# print("Apple 은 %c로 시작해요." % "A")

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# print("나는 {}살입니다." .format(20))
# print("나는 {1}색과 {0}색을 좋아합니다." .format("파란","빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문이 불여일견 백견이 불여일타")

# 화면에 Hello World 문자열을 출력하세요.

# print("Hello World")

# print는 정수, 실수, 문자열 등을 화면에 출력합니다.
# 문자열은 큰따옴표 또는 작은따옴표로 표현이 가능합니다.

# 002 화면에 Mary's cosmetics을 출력하세요.
#     중간에 '가 있음에 주의하세요.

# print("Mary's cosmetics")

# 문자열은 큰따옴표나 작은따옴표로 표현 가능합니다.
# 표현하고 싶은 문자열에 작은따옴표가 있으므로 문자열을
# 큰따옴표로 만들어주시면 됩니다.

# print("Mary's cosmetics")

# 003 print 기초
# 화면에 아래 문장을 출력하세요.
# 중간에 "가 있음에 주의하세요.

# 신씨가 소리질렀다. "도둑이야".

# print('신씨가 소리질렀다. "도둑이야"')

# 표현하고 싶은 문자열에 큰따옴표가 포함되어 있습니다.
# 따라서 작은따옴표로 문자열을 만들어주면 됩니다.

# print('신씨가 소리질렀다. "도둑이야"')

# 004 print 기초
# 화면에 "C:\Windows"를 출력하세요.

# print("C:\\Windows")

# print("C:\Windows")

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.

# print("안녕하세요.\n만나서\t반갑습니다.")
# \n 은 줄바꿈이고, \t는 4칸 들여쓰기 입니다.

# \t는 탭을 의미하고, \n은 줄바꿈을 의미합니다.

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 
# 아래 코드의 출력 결과를 예상해봅시다.

# print("오늘은","일요일")
# print("오늘은"+"일요일")
# print("오늘은일요일")

# print("naver;kakao;sk;samsung")
# print("naver"+"kakao","sk","samsung", sep=";")

# print("naver","kakao","sk","samsung", sep="\\")

# print("first");print("second")

# print("first", end="");print("second")

# print(5/3)

# 삼성전자 = 50000
# 보유주식 = 10
# 총평가금액 = 삼성전자 * 보유주식
# print(총평가금액,type(총평가금액))

# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.79

# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# s = "hello"
# t = "python"

# print(s+"!",t)

# print(2+2*3)

# a = 128
# print(a, type(a))

# a = 132
# print(a, type(a))

# num_str = "720"

# print(num_str,type(num_str))

# num_str = int(num_str)

# print(num_str, type(num_str))

# num = 100
# num = str(num)
# print(num, type(num))

# a = "15.79"
# print(a, type(a))
# a = float(a)
# print(a, type(a))

# year = "2020"
# year = int(year)
# print("3년전 : ", year - 3)
# print("2년전 : ", year - 2)
# print("1년전 : ", year - 1)
# print("0년전 : ", year)

# a = 48584
# b = 36
# c = a * b
# print(c)

# letters = 'python'
# print(letters[0],letters[2])

# license_plate = "24가 2210"

# print(license_plate[-4:])

# string = "홀짝홀짝홀짝"

# print(string[0::2])

# string = "PYTHON"
# print(str(string[::-1]))

# phone_number = "010-1111-2222"
# a = phone_number.replace("-", "")
# print(a)

# url = "http://sharebook.kr"
# url_split = url.split(".")
# print(url_split[1])

# lang = 'phtyon'
# lang(0) = 'P'
# print(lang)

# string = 'abcdfe2a354a32a'
# a = string.replace('a', 'A')
# print(a)

# string = 'abcd'
# string.replace('b', "B")
# print(string)


# letters = 'python'
# print(letters[0], letters[2])

# license_plate = '24가 2210'
# print(license_plate[-4:])

# string = '홀짝홀짝홀짝'
# print(string[0::2])

# string = "PYTHON"
# print(string[::-1])

# phone_number = '010-1111-2222'
# print(phone_number.replace('-', ' '))

# phone_number = '010-1111-2222'
# print(phone_number.replace('-', ''))

# url = "http://sharebook.kr"
# print(url[-2:])

# url = "http://sharebook.kr"
# url.split('.')
# print(url.split('.')[1])

# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 에러가 난다. 문자열은 수정할 수 없다.

# string = 'abcdfe2a354a32a'
# print(string.replace('a', 'A'))

# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# a = "3"
# b = "4"
# print(a + b)

# print("Hi" * 3)

# print('-' * 80)

# t1 = 'python'
# t2 = 'java'
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: %s 나이: %s" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 상장주식수 = "5,969,782,550"
# a = int(상장주식수.replace(",", ""))
# print(a, type(a))

# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# data = "    삼성전자    "
# print(data.replace(" ", ""))

# data = "    삼성전자    "
# data1 = data.strip()
# print(data1)

# ticker = "btc_krw"
# print(ticker.upper())

# ticker = "BTC_KRW"
# print(ticker.lower())

# a = 'hello'
# print(a.capitalize())

# file_name = "보고서.xlsx"
# a = file_name.split(".")

# print(a[1])

# file_name = "보고서.xlsx"
# file_name.endswith("xlsx")

# file_name = "보고서.xlsx"
# a = file_name.endswith("xlsx" and "xls")

# print(a)

# file_name = "2020_보고서.xlsx"
# a = file_name.startswith("2020")
# print(a)

# a = "hello world"
# b = a.split()
# print(b)

# ticker = "btc_krw"
# print(ticker.split("_"))

# data = "2020-05-01"
# a = data.split("-")
# print("연도 : " + a[0], "월 : " + a[1], "일 : " + a[2])

# data = "039490    "
# print(data.replace(" ", ""))
# print(data.split())

# data = "039490    "
# print(data.rstrip())

# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# print(movie_rank)
# print(type(movie_rank))

# movie_rank2 = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank2, type(movie_rank2))

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)
# movie_rank[3] = ["베트맨"]
# print(movie_rank)

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs, type(langs))

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max: ", max(nums))
# print("minL ", min(nums))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두"
# , "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]

# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# a = sum(nums)/len(nums)
# print(a, type(a))

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래애셋대우']
# print("/".join(interest))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# string = "삼성전자/LG전자/Naver"
# a = string.split('/')
# print(a)

# data = [2, 4, 3, 1, 5, 10, 9]
# a = sorted(data)
# print(a)

# ticker = "btc_krw"
# print(ticker.upper())

# ticker = "BTC_KRW"
# print(ticker.lower())

# a = "hello"
# print(a.capitalize())

# file_name = "보고서.xlsx"
# print(file_name.endswith('xlsx'))

# file_name = "보고서.xlsx"
# print(file_name.endswith(("xlsx" or "xls")))

# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))

# a = "hello world"
# print(a.split())

# ticker = "btc_krw"
# print(ticker.split("_"))

# date = "2020-05-01"
# a = date.split("-")
# print(a[0])
# print(a[1])
# print(a[2])

# data = "039490    "
# print(data.split())
# print(data.rstrip())

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("베트맨")
# print(movie_rank)

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"]
# del movie_rank[3]
# print(movie_rank)

# movie_rank = ["닥터 스트레인지", "슈퍼맨", "스플릿", "배트맨"]
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max: ", max(nums))
# print("min: ", min(nums))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두"
# , "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# nums = [1, 2, 3, 4, 5]
# print(sum(nums)/len(nums))

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest))

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# my_variable = ()
# print(type(my_variable))

# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# print(movie_rank)

# movie_rank = (1, )
# print(movie_rank,type(movie_rank))

# t = (1, 2, 3)
# t[0] = 'a'
# print(t)

# t = 1, 2, 3, 4
# print(type(t))

# t = ('a', 'b', 'c')
# t = ('A', 'b', 'c')

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# data = list(interest)
# print(interest, type(interest))
# print(data, type(data))

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)
# print(interest, type(interest))
# print(data, type(data))

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# a = tuple(range(1,100))
# print(a[1::2])

# a, b, *c = (0, 1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)
# print(type(a))
# print(type(b))
# print(type(c))

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *vaild_score, a, b = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# print(vaild_score)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, _, *vaild_score = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# print(vaild_score)

# temp = {}
# print(temp, type(temp))

# a = {"메로나":100,"폴라포":1200,"빵빠래":1800,}
# print(a)

# a = {"메로나":100,"폴라포":1200,"빵빠래":1800,"죠스바":1200,"월드콘":1500,}
# print(a.keys)

# a = True
# print(a, type(a))

# print(3 == 5)

# print(3 < 5)

# x = 4
# print(1 < x < 5)

# print((3 == 3) and (4 != 3))

# print(3 => 4)

# if 4 < 3:
#     print("Hello World")

# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")

# if True:
#     print("1")
#     print("2")
# else:
#     print("3")
# print("4")

# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else:
#     print("4")
# print("5")

# user = input("입력 :")
# print(user * 2)

# a = input("숫자를 입력하세요: ")
# print(int(a) + 10)

# a = input()
# if int(a) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# a = input("입력값: ")
# b = int(a) + 20
# if b > 255:
#     print(255)
# else:
#     print(b)


# a = input("입력값: ")
# b = int(a) - 20
# if b < 0:
#     print(0)
# elif b > 255:
#     print(255)
# else:
#     print(b)

# a = input("현재시간: ")
# if a[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은?")
# if a in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# a = input()
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# if a in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# a = input("좋아하는 계절은?")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# if a in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# a = input("좋아하는과일은? ")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# if a in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# a = "   12:00"
# print(a, type(a))
# b = a.lstrip()
# print(b)

# a = input()
# if a.islower() == True:
#     print(a.upper())
# else:
#     print(a.lower())

# a = int(input("score: "))
# if a > 100:
#     print("다시 입력하세요.")
# elif a > 80:
#     print("A")
# elif a > 60:
#     print("B")
# elif a > 40:
#     print("C")
# elif a > 20:
#     print("D")
# elif a > 0:
#     print("E")
# else:
#     print("다시 입력하세요.")

# a = {"달러":1167,"엔":1.096,"유로":1268,"위안":171}
# user = input("입력: ")
# price, currency = user.split()
# print(float(price)*a[currency], "원")

# num1 = int(input("input number1: "))
# num2 = int(input("input number2: "))
# num3 = int(input("input number3: "))
# max = max(num1, num2, num3)
# print(max)

# user = input("휴대전화 번호 입력: ")
# phone = {"011":"SKT", "016":"KT", "019":"LGU", "010":"알수없음"}
# confirm = user.split("-")
# print("당신은", phone[confirm[0]], "사용자입니다.")

# officeNum = input("우편번호: ")
# if int(officeNum[2]) <= 2 and int(officeNum[2]) >= 0:
#     print("강북구")
# elif int(officeNum[2]) >= 3 and int(officeNum[2]) <= 5:
#     print("도봉구")
# elif int(officeNum[2]) >= 6 and int(officeNum[2]) <= 9:
#     print("노원구")
# else:
#     print("다시 입력하세요.")

# personNum = input("주민등록번호 : ")
# confirm = personNum.split("-")
# if confirm[1][0] == "1" or confirm[1][0] == "3":
#     print("남자")
# else:
#     print("여자")

# personNum = input("주민등록번호 : ")
# confirm = personNum.split("-")
# if int(confirm[1][1:3]) >= 0 and int(confirm[1][1:3]) <= 8:
#     print("서울 입니다.")
# elif int(confirm[1][1:3]) >= 9 and int(confirm[1][1:3]) <= 12:
#     print("부산 입니다.")
# else:
#     print("서울이 아닙니다.")

# personNum = input("주민등록번호 : ")
# personNum = personNum.replace("-", "")
# if (confirm == (personNum[0] * 2 + personNum[1] * 3
#     + personNum[2] * str(4) personNum[3] * str(5)
#     + personNum[4] * str(6) + personNum[5] * str(7)
#     + personNum[6] * str(8) + personNum[7] * str(9)
#     + personNum[8] * str(2) + personNum[9] * str(3)
#     + personNum[10] * str(4) + personNum[11] * str(5) %% 11 == personNum[-2:]):
    
#     print("유효한 주민등록번호 입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")


# a = str(4)
# print(a * 2, type(a))

# person = input("주민등록번호 : ")
# confirm = person.replace("-", "")
# if 11 - ((int(confirm[0]) * 2 + int(confirm[1]) * 3 +
#     int(confirm[2]) * 4 + int(confirm[3]) * 5 +
#     int(confirm[4]) * 6 + int(confirm[5]) * 7 +
#     int(confirm[6]) * 8 + int(confirm[7]) * 9 +
#     int(confirm[8]) * 2 + int(confirm[9]) * 3 +
#     int(confirm[10]) * 4 + int(confirm[11]) * 5) % 11) == int(confirm[-1:]):
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# from requests import *
# btc = requests.get("http://api.bithumb.com/public/ticker/").json()['data']

# print(btc[0])

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print("#####")

# for 변수 in ["A", "B", "C"]:
#     print(변수)

# print("++++")
# for num in [10, 20, 30]:
#     print(num)

# for a in [1,2,3,4]:
#     print("-------")

# list = [100, 200, 300]
# for price in list:
#     print(int(price) + 10)

# list = ["김밥", "라면", "튀김"]
# for a in list:
#     print("오늘의 메뉴 : " + a)

# list = ["SK하이닉스", "삼성전자", "LG전자"]
# for a in list:
#     print(len(a))

# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a, len(a))

# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a[0])

# list = [1, 2, 3]
# for a in list:
#     print("3 x", a)

# list = [1, 2, 3]
# for a in list:
#     print("3 x", a, "=", int(a)*3)

# list = ["가", "나", "다", "라"]
# a = list[1:]
# for b in a:
#     print(b)

# list = ["가", "나", "다", "라"]
# for a in list[::2]:
#     print(a)

# list = ["가", "나", "다", "라"]
# for a in list[::-1]:
#     print(a)

# list = [3, -20, -3, 44]
# for a in list:
#     if a < 0:
#         print(a)

# list = [3, 100, 23, 44]
# for num in list:
#     if num % 3 == 0:
#         print(num)

# list = [13, 21, 12, 14, 30, 18]
# for a in list:
#     if a < 20 and a % 3 ==0:
#         print(a)

# list = ["I", "study", "python", "language", "!"]
# for a in list:
#     if len(a) >= 3:
#         print(a)

# list = ["A", "b", "c", "D"]
# for a in list:
#     if a == a.upper():
#         print(a)

# list = ["A", "b", "c", "D"]
# for a in list:
#     if a.isupper() == True:
#         print(a)

# list = ["A", "b", "c", "D"]
# for a in list:
#     if a.isupper() == False:
#         print(a)

# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a.capitalize())

# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a[0].upper()+a[1:])

# list = ['hello.py', 'ex01.py', 'intro.hwp']
# for a in list:
#     split = a.split(".")
#     print(split[0])

# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for a in list:
#     if a[-1] == "h":
#         print(a)

# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for a in list:
#     split = a.split(".")
#     if split[1] == "h":
#         print(a)

# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for a in list:
#     split = a.split(".")
#     if split[1] == "h" or split[1] == "c":
#         print(a)

# for num in range(99):
#     print(num)

# for x in range(2002, 2051, 4):
#     print(x)

# for a in range(1, 31):
#     if a % 3 == 0:
#         print(a)

# for a in range(100, 0, -1):
#     print(a)

# for a in range(10):
#     print(a / 10)

# for a in range(1,10):
#     print("3x"+ a , "= " , (3 * a))

# for number in range(1, 10):
#     if number % 2 == 1:
#         print(3, '*', number, '=', 3 * number)

# for number in range(1, 11, 1):
#     a += number
# print("합 : ", a)

# a = 0
# for number in range(1, 11, 1):
#     if number % 2 == 1:
#         a = a + number
# print(a)

# a = 1
# for number in range(1, 11, 1):
#     a = a * number
# print(a)

# result = 1
# for i in range(1, 11):
#     result *= i
# print(result)

# price_list = [32100, 32150, 32000, 32500]
# for result in (price_list in range(2)):
#     print(result)

# price_list = [32100, 32150, 32000, 32500]
# for result in range(3):
#     print(price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(result, price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(3-result, price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     if result > 0:
#         print(result * 10 + 100, price_list[result])

# my_list = ["가", "나", "다", "라"]
# for result in range(1, len(my_list)):
#     print(my_list[result-1], my_list[result])

# my_list = ["가", "나", "다", "라", "마"]
# for result in range(2, len(my_list)):
#     print(my_list[result - 2], my_list[result - 1], my_list[result])


# my_list = ["가", "나", "다", "라"]
# for result in range(1, len(my_list)):
#     print(my_list[4-result], my_list[3-result])

# my_list = [100, 200, 400, 800]
# for result in range(len(my_list)-1):
#     print(my_list[result + 1] - my_list[result])

# my_list = [100, 200, 400, 800, 1000, 1300]
# for result in range(1, len(my_list) - 1):
#     print(abs(my_list[result - 1] + my_list[result] + my_list[result+1])/3)

# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(len(low_prices)):
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)

# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
# print(apart)

# stock = [["시가", "종가"], [100, 80], [200, 210], [300, 330]]
# print(stock)

# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
# print(stock)

# stock = {"시가" : "종가", 100 : 80, 200 : 210, 300 : 330}
# print(stock)

# stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}
# print(stock)

# stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}
# print(stock)

# apart = [[101, 102], [201, 202], [301, 302]]
# for a in apart:
#     for b in a:
#         print(b, "호")

# apart = [[101, 102], [201, 202], [301, 302]]
# for a in apart[::-1]:
#     for b in a:
#         print(b)

# apart = [[101, 102], [201, 202], [301, 302]]
# for a in apart[::-1]:
#     for b in a[::-1]:
#         print(b, "호")

# apart = [[101, 102], [201, 202], [301, 302]]
# for a in apart:
#     for b in a:
#         print(b)
#         print("-----")


# apart = [[101, 102], [201, 202], [301, 302]]
# for a in apart:
#     for b in a:
#         print(b)
#     print("-----")    

# apart = [[101, 102], [201, 202], [301, 302]]
# for a in apart:
#     for b in a:
#         print(b)
# print("-----")    

# data = [
#     [2000, 3050, 2050, 1980],
#     [ 7500, 2050, 2050, 1980],
#     [15450, 15050, 15550, 14900]
# ]

# tax = 0.00014

# for a in data:
#     for b in a:
#         print(b + b * tax)



# data = [
#     [2000, 3050, 2050, 1980],
#     [7500, 2050, 2050, 1980],
#     [15450, 15050, 15550, 14900]
# ]

# tax = 0.00014

# for a in data:
#     for b in a:
#         print(b + b * tax)
#     print("-" * 4)


# data = [
#     [2000, 3050, 2050, 1980],
#     [7500, 2050, 2050, 1980],
#     [15450, 15050, 15550, 14900]
# ]

# tax = 0.00014
# c = []

# for a in data:
#     for b in a:
#         # print(b + b * tax)
#         c.append(b + b * tax)
# print(c)

# data = [
#     [2000, 3050, 2050, 1980],
#     [7500, 2050, 2050, 1980],
#     [15450, 15050, 15550, 14900]
# ]

# result = []
# for a in data:
#     sub = []
#     for b in a:
#         sub.append(b + 1.00014)
#     result.append(sub)
# print(result)

# ohlc = [
#     ["open", "high", "low", "close"],
#     [100, 110, 70, 100],
#     [200, 210, 180, 190],
#     [300, 310, 300, 310]
# ]

# for a in ohlc[1:]:
#     print(a[3])


# ohlc = [
#     ["open", "high", "low", "close"],
#     [100, 110, 70, 100],
#     [200, 210, 180, 190],
#     [300, 310, 300, 310]
# ]
# for price in ohlc[1:]:
#     if price[3] > 150:
#         print(price[3])


# ohlc = [
#     ["open", "high", "low", "close"],
#     [100, 110, 70, 100],
#     [200, 210, 180, 190],
#     [300, 310, 300, 310]
# ]
# for price in ohlc[1:]:
#     if price[0] <= price[3]:
#         print(price[3])


# ohlc = [
#     ["open", "high", "low", "close"],
#     [100, 110, 70, 100],
#     [200, 210, 180, 190],
#     [300, 310, 300, 310]
# ]
# volatility = []
# for price in ohlc[1:]:
#     result = (price[1] - price[2])
#     volatility.append(result)
# print(volatility)


# ohlc = [
#     ["open", "high", "low", "close"],
#     [100, 110, 70, 100],
#     [200, 210, 180, 190],
#     [300, 310, 300, 310]
# ]
# for price in ohlc[1:]:
#     if price[3] > price[0]:
#         print(price[1]-price[2])

# ohlc = [
#     ["open", "high", "low", "close"],
#     [100, 110, 70, 100],
#     [200, 210, 180, 190],
#     [300, 310, 300, 310]
# ]
# profit = 0
# for price in ohlc[1:]:
#     profit += (price[3] - price[0])
# print(profit)

# def print_coin():
#     print("비트코인")

# for come in range(5):
#     print_coin()

# def print_coin():
#     print("비트코인")
# def print_coins():
#     for a in range(5):
#         print("비트코인")
# print_coin()

# hello()
# def hello():
#     print("Hi!")

# def message():
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# print("A")
# def message():
#     print("B")
# print("C")
# message()

# print("A")
# def message1():
#     print("B")
# print("C")
# def message2():
#     print("D")
# message1()
# print("E")
# message2()

# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()

# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range(3):
#         message2()
#         print("C")
#     message1()
# message3()

# BCBCBCBCA

# def 함수(문자열):
#     print(문자열)
# 함수("안녕")
# 함수("Hi!")

# def 함수(a, b):
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# def 함수(문자열) :
#     print(문자열)

# 함수("문자")

# def 함수(a, b):
#     print(a + b)
# 함수("안녕", 3)

# def print_with_smile(a):
#     print(a, ":D")
# print_with_smile("안녕하세요~~")

# price = int(input("현재 가격 : "))
# def print_upper_price():
#     print(price * 0.3)
# print_upper_price()

# number1 = int(input("첫번째 숫자 : "))
# number2 = int(input("두번째 숫자 : "))
# def sum():
#     print(number1 + number2)
# sum()

# number1 = int(input("첫번째 숫자 : "))
# number2 = int(input("두번째 숫자 : "))
# def confirm():
#     print("합 : ", number1 + number2)
#     print("차 : ", number1 - number2)
#     print("곱 : ", number1 * number2)
#     print("나누기 : ", number1 / number2)
# confirm()

# number1 = int(input("첫번째 숫자 : "))
# number2 = int(input("두번째 숫자 : "))
# number3 = int(input("세번째 숫자 : "))
# def print_max():
#     print(max(number1, number2, number3))
# print_max()

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print("######")

# for 변수 in ["A", "B", "C"]:
#     print(변수)

# print("A")
# print("B")
# print("C")

# for 변수 in ["A", "B", "C"]:
#     print("출력 : " + 변수)
# print("출력 : A")
# print("출력 : B")
# print("출력 : C")

# def 함수(문자열):
#     print(문자열)
# 함수("안녕")
# 함수("Hi!")

# def 함수(a, b):
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# def 함수(문자열) :
#     print(문자열)

# def 함수(a, b):
#     print(a + b)
# 함수("안녕", 3)

# inputt = input("문자를 입력하세요. : ")
# def print_with_smile():
#     print(inputt, ":D")
# print_with_smile()

# def print_with_smile(string):
#     print(string + ":D")

# def print_reverse(reverse):
#     print(reverse[::-1])
# print_reverse("phython")

# def print_score(score):
#     print(sum(score)/len(score)) 
# print_score([1, 2, 3])

# def print_even(score):
#     for a in score:
#         if a % 2 == 0:
#             print(a)
# print_even([1, 3, 2, 10, 12, 15])

# def print_keys(name):
#     for a in name:
#         print(a)
# print_keys({"이름" : "김말똥", "나이" : 30, "성별" : 0})

# my_dick = {"10/26" : [100, 130, 100, 100],
#         "10/27" : [10, 12, 10, 11]}
# def print_value_by_key (input, key):
#     print(input[key])
# print_value_by_key(my_dick, "10/26")

# def print_5xn(string):
#     print(string[:5])
#     print(string[5:])
        
# print_5xn("아이엠어보이유알어걸")

# def print_5xn(line):
#     chunk_num = int(len(line) / 5)
#     for x in range(chunk_num + 1):
#         print(line[x * 5 : x * 5 + 5])
# print_5xn("아이엠어보이유알어걸")

# def print_mxn(a, b):
#     for c in a:
#         print(c)

# print_mxn("아이엠어보이유알어걸", 3)

# 문자열과 한줄에 출력될 글자 수를 입력을 받아
# 한 줄에 입력된 글자 수만큼 출력하는
# print_mxn(stirng) 함수를 작성하라

# def print_mxn(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num + 1):
#         print(line[x * num : x * num + num])
# print_mxn("아이엠어보이유알어걸", 3)

# a = input()
# if a.islower():
#     print(a.upper())
# else:
#     print(a.lower())

# a = int(input("Score : "))
# if a > 100:
#     print("다시 입력하세요.")
# elif a > 80:
#     print("A")
# elif a > 60:
#     print("B")
# elif a > 40:
#     print("C")
# elif a > 20:
#     print("D")
# elif a > 0:
#     print("F")
# else:
#     print("다시 입력하세요.")

# a = {"달러" : 1667, "엔" : 1.096, "유로" : 1268, "위안" : 171}
# user = input("입력 : ")
# price, currency = user.split()
# print(float(price) * a[currency], "원")

# num1 = int(input("input number1 : "))
# num2 = int(input("input number2 : "))
# num3 = int(input("input number3 : "))
# max = max(num1, num2, num3)
# print(max)

# num1 = int(input("input number1 : "))
# num2 = int(input("input number2 : "))
# num3 = int(input("input number3 : "))
# sum = sum(num1, num2, num3)
# print(sum)

# user = input("휴대전화번호 입력 : ")
# phone = {"011" : "SKT", "016" : "KT", "019" : "LGU", "010" : "알수없음"}
# comfirm = user.split("-")
# print("당신은", phone[comfirm[0]], "사용자입니다.")

# officeNum = input("우편번호 : ")
# if int(officeNum[2]) <= 2 and int(officeNum[2]) >= 0:
#     print("강북구")
# elif int(officeNum[2]) >= 3 and int(officeNum[2]) <= 5:
#     print("도봉구")
# elif int(officeNum[2]) >= 6 and int(officeNum[2]) <= 9:
#     print("노원구")
# else:
#     print("다시 입력하세요.")

# personNum = input("주민등록번호 : ")
# confirm = personNum.split("-")
# if confirm[1][0] == "1" or confirm[1][0] == "3":
#     print("남자 입니다.")
# elif confirm[1][0] == "2" or confirm[1][0] == "4":
#     print("여자 입니다.")

# personNum = input("주민등록번호 : ")
# confirm = personNum.split("-")
# if int(confirm[1][1:3]) >= 0 and int(confirm[1][1:3]) <= 8:
#     print("서울 입니다.")
# elif int(confirm[1][1:3]) >=9 and int(confirm[1][1:3]) <= 12:
#     print("부산 입니다.")
# else:
#     print("다시 입력해주세요.")

# person = input("주민등록번호 : ")
# confirm = person.replace("-", "")
# if 11 - ((int(confirm[0]) * 2 + int(confirm[1]) * 3
#     + int(confirm[2]) * 4 + int(confirm[3]) * 5 + int(confirm[4]) * 6
#     + int(confirm[5]) * 7 + int(confirm[6]) * 8 + int(confirm[7]) * 9
#     + int(confirm[8]) * 2 + int(confirm[9]) * 3 + int(confirm[10]) * 4
#     + int(confirm[11]) * 5) % 11) == int(confirm[-1:]):
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# a = input("현재시간 : ")
# if a[-2:] == "00":
#     print("정각입니다.")
# else:
#     print("정각이 아닙니다.")

# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은? : ")
# if a in fruit:
#     print("정답입니다.")
# else:
#     print("정답이 아닙니다.")

# a = input()
# warn_investment_list = ["Microsoft", "Goolge", "Naver", "Kakao", "Samsung", "LG"]
# if a in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# a = input("좋아하는 계절은? : ")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# if a in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# a = input("좋아하는 계절은? : ")
# fruit = {"봄" : "딸기", "여름" : "토미토", "가을" : "사과"}
# if a in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# a = input("좋아하는 과일은? : ")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# if a in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# price_list = [32100, 32150, 32000, 32500]
# for result in range(3):
#     print(price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(result, price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(3-result, price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     print(len(price_list) - result, price_list[result])

# price_list = [32100, 32150, 32000, 32500]
# for result in range(len(price_list)):
#     if result > 0:
#         print(result * 10 + 100, price_list[result])

# my_list = ["가", "나", "다", "라"]
# for result in range(1, len(my_list)):
#     print(my_list[result-1], my_list[result])

# def print_coin():
#     print("비트코인")
# print_coin()

# def print_coin():
#     print("비트코인")
# print_coin()

# def print_coin():
#     print("비트코인")
# for a in range(5):
#     print_coin()

# hello()
# def hello():
#     print("Hi")

# def message():
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# print("A")
# def message():
#     print("B")
# print("C")
# message()

# print("A")
# def message1():
#     print("B")
# print("C")
# def message2():
#     print("D")
# message1()
# print("E")
# message2()

# A C B E D

# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()

# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range(3):
#         message2()
#         print("C")
#     message1()
# message3()

# def 함수(문자열):
#     print(문자열)
# 함수("안녕")
# 함수("Hi")

# def 함수(a, b):
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# def 함수(문자열):
#     print(문자열)

# input = input("문장을 입력하세요. : ")
# def print_with_smile():
#     print(input + ":D")
# print_with_smile()

# input = int(input("금액을 입력하세요. : "))
# def print_upper_price():
#     print(input * 0.3)
# print_upper_price()

# def print_upper_price(price):
#     print(price * 0.3)
# print_upper_price(price)

# def print_sum(a, b):
#     print(a + b)
# print_sum(a, b)

# num1 = int(input("첫번째 숫자를 입력하세요. : "))
# num2 = int(input("두번째 숫자를 입력하세요. : "))
# def print_sum(num1, num2):
#     print(num1 + num2)
# print_sum(num1, num2)

# num1 = int(input("첫번째 숫자를 입력하세요. : "))
# num2 = int(input("두번째 숫자를 입력하세요. : "))
# def print_arithmetic_operation(num1, num2):
#     print(num1, "+", num2, "=", (num1 + num2))
#     print(num1, "-", num2, "=", (num1 - num2))
#     print(num1, "*", num2, "=", (num1 * num2))
#     print(num1, "/", num2, "=", (num1 / num2))
# print_arithmetic_operation(num1, num2)

# number1 = int(input("첫번째 숫자를 입력하세요. : "))
# number2 = int(input("두번째 숫자를 입력하세요. : "))
# number3 = int(input("세번째 숫자를 입력하세요. : "))
# def print_max(number1, number2, number3):
#     print(max(number1, number2, number3))
# print_max(number1, number2, number3)

# number1 = int(input("첫번째 숫자를 입력하세요. : "))
# number2 = int(input("두번째 숫자를 입력하세요. : "))
# number3 = int(input("세번째 숫자를 입력하세요. : "))
# def print_max(number1, number2, number3):
#     if number1 > number2 and number1 > number3:
#         print(number1)
#     elif number2 > number1 and number2 > number3:
#         print(number2)
#     else:
#         print(number3)
# print_max(number1, number2, number3)

# def print_reverse(reverse):
#     print(reverse[::-1])
# print_reverse("python")

# def print_score(number):
#     print(sum(number) / len(number))
# print_score([1, 2, 3])

# def print_even(list_number):
#     for number in list_number:
#         if number % 2 == 0:
#             print(number)
# print_even([1, 3, 2, 10, 12, 11, 15])

# def print_keys(dictionary):
#     for a in dictionary.keys():
#         print(a)
# print_keys({"이름" : "김말똥", "나이" : 30, "성별" : 0})

# my_dict = {"10/26" : [100, 130, 100, 100],
#         "10/27" : [10, 12, 10, 11]}
# def print_value_my_key(my_dict, key):
#     print(my_dict[key])
# print_value_my_key(my_dict, "10/26")

# def print_5xn(string):
#     if len(string) > 5:
#         print(string[:5])
#         print(string[5:10])
# print_5xn("아이엠어보이유알어걸")    

# def print_mxn(a, b):
#     check_value = int(len(a) / b)
#     for x in range(check_value + 1):
#         print(a[x * b: x * b + b])
# print_mxn("아이엠어걸유알어보이", 3)

# annual_salary = int(input("연봉을 입력하세요. : "))
# def calc_monthly_salary(annual_salary):
#     print(annual_salary / 12)
# calc_monthly_salary(annual_salary)

# import datetime

# now = datetime.datetime.now()
# print(now)

# import datetime
# now = datetime.datetime.now()
# print(now, type(now))

# import datetime

# now = datetime.datetime.now()

# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days = day)
#     date = now - delta
#     print(date)

# import datetime

# now = datetime.datetime.now()
# print(now.strftime("%H : %M : %S"))

# import datetime

# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))

# import time
# import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# import os
# ret = os.getcwd()
# print(ret, type(ret))

# import os
# ret = os.getcwd()
# print(ret, type(ret))

# import os
# os.rename("/Users/parkgyeongtae/Documents/무제.rtf", "/Users/parkgyeongtae/Documents/무무제.rtf")

# import numpy
# for i in numpy.arange(0, 5, 0.1):
#     print(i)

# def n_plus_1(n):
#     result = n + 1

# n_plus_1(3)
# print(result)

# def make_url(string):
#     url = "www." + string + ".com"
#     return url
# make_url("naver")

# def make_url(string):
#     return "www." + string + ".com"

# def make_list(string):
#     my_list = []
#     for 변수 in string:
#         my_list.append(변수)
#     return my_list
# make_list("abcd")

# def pickup_even(items):
#     result = []
#     for item in items:
#         if item % 2 == 0:
#             result.append(item)
#         return result
# pickup_even([3, 4, 5, 6, 7, 8])

# print("Hello World")

# print("Mary's cosmetics")

# print('신씨가 소리를 질렀다. "도둑이야".')

# print('"C:/Windows"')

# print("안녕하세요. \n 만나서 \t\t 반갑습니다.")

# print("오늘은", "일요일")

# print("naver;kakao;sk;samsung")

# print("naver/kakao/sk/samsung")

# print("first", end="");print("second")

# print(5/3)

# class human:
#     pass

# class human:
#     pass
# areum = human()

# class human:
#     def __init__(self):
#         print("응애응애")

# areum = human()

# class human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = human("아름", 25, "여자")
# print(areum.sex)

# class human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = human("아름", 25, "여자")
# print(areum.age)

# class human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print("이름 = {} 나이 : {} 성별 : {}".format(self.name, self.age, self.sex))

# areum = human("아름", 25, "여자")
# areum.who()

# class human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def who(self):
#         print("이름 = {} / 나이 = {} / 성별 = {}".format(self.name, self.age, self.sex))
#     def setinfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = human("불명", "미상", "모름")
# areum.who()

# areum.setinfo("아름", 25, "여자")
# areum.who()

# class human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def __del__(self):
#         print("나의 죽음을 적에게 알리지 말라.")
#     def who(self):
#         print("이름 = {} / 나이 = {} / 성별 = {}".format(self.name, self.age, self.sex))
#     def setinfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# areum = human("아름", 25, "여자")
# del(areum)

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# car = 차(2, 1000)
# print(car.바퀴)
# print(car.가격)

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     pass

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 가격
#         self.가격 = 가격
# bicycle = 자전차(2, 100)
# print(bicycle.가격)

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)
# print(bicycle.바퀴)

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
#     def 정보(self):
#         print("바퀴수 : ", self.바퀴)
#         print("가격 : ", self.가격)
# car = 자동차(4, 1000)
# car.정보()

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#     def 정보(self):
#         print("바퀴 : ", self.바퀴)
#         print("가격 : ", self.가격)
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계
# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()

# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#     def 정보(self):
#         print("바퀴수 : ", self.바퀴)
#         print("가격 : ", self.가격)
# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)
# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         self.구동계 = 구동계
#     def 정보(self):
#         super().정보()
#         print("구동계 ", self.구동계)
# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()

# class 부모:
#     def 호출(self):
#         print("부모호출")
# class 자식(부모):
#     def 호출(self):
#         print("자식호출")
# 나 = 자식()
# 나.호출()

# class 부모:
#     def __init__(self):
#         print("부모생성")
# class 자식(부모):
#     def __init__(self):
#         print("자식생성")
# 나 = 자식()

# class 부모:
#     def __init__(self):
#         print("부모생성")
# class 자식(부모):
#     def __init__(self):
#         print("자식생성")
#         super().__init__()
# 나 = 자식()

# sharp = {'C#' : 'c', 'D#' : 'd', 'F#' : 'f', 'G#' : 'g', 'A#' : 'a'}

# def time2mir(time):
#     h, m = time.split(':')
#     return int(h) * 60 + int(m)


# def sharp2lower(m):
#     for s in sharp.keys():
#         m = m.replace(s, sharp[s])
#     return m

# def musicfullstream(mel, dur):
#     mel = sharp2lower(mel)
#     mel = mel * (dur // len(mel) + 1)
#     return mel[:dur]

# def solution(m, musicinfos):
#     m = sharp2lower(m)
#     print(m)
#     play_title = []
#     play_dur=[]
#     play_history=dict()
#     # 재생 시간
#     # 음이 내부에 있는지
#     for music in musicinfos:
#         start, end, title, mel = music.split('.')
#         dur = time2min(end) - time2min(start)

#         mel = musicfullstream(mel, dur)
#         if m in mel:
#             play_history[title] = dur
    
#     print(play_history.values())
#     return None

# a = True
# print(a, type(a))

# print(3 == 5)

# print(3 < 5)

# x = 4
# print(1 < x < 5)

# print((3 == 3) and (4 != 3))

# print(3 >= 4)

# if 4 < 3:
#     print("Hello World")

# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")

# if True:
#     print("1")
#     print("2")
# else:
#     print("3")
# print("4")

# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else:
#     print("4")
# print("5")

# input = input("문자를 입력하세요. : ")
# print(input * 2)

# input = input("숫자를 입력하세요. : ")
# print(int(input) + 10)

# input = input("숫자를 입력하세요. : ")
# if int(input) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# input = int(input("입력값 : "))
# if input + 20 > 255:
#     print("출력값 : 255")
# else:
#     print("출력값 : ", input + 20)

# input = int(input("입력값 : "))
# if input - 20 < 0:
#     print("출력값 : 0")
# else:
#     print("출력값 :", input - 20)

# time = input("현재시간 : ")
# if time[3:5] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

# fruit = ["사과", "포도", "홍시"]
# input = input("좋아하는 과일은? ")
# if input in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# print("Hello World")

# print("Mary's cosmetics")

# print("Mary's cosmetics")

# print('신씨가 소리질렀다. "도둑이야".')

# print('"C:\Windows"')

# print("안녕하세요. \n만나서\t\t반갑습니다.")

# print("오늘은", "일요일")

# print("naver;kakao;sk;samsung")

# print("naver/kakao/sk/samsung")

# print("first",end="");print("second")

# print("first", end=" ");print("second")

# print(5/3)

# 삼성전자 = 50000
# 보유주식 = 10
# 총평가금액 = 삼성전자*보유주식

# print("삼성전자 : ", 삼성전자, type(삼성전자))
# print("보유주식 : ", 보유주식, type(보유주식))
# print("총평가금액 : ", 총평가금액, type(총평가금액))

# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.79

# print("시가총액 :", 시가총액, type(시가총액))
# print("보유주식 :", 현재가, type(현재가))
# print("PER :", PER, type(PER))

# s = "hello"
# t = "python"

# print(s + "!", t)

# print(2+2*3)

# a = "132"
# print(a, type(a))

# num_str = "720"
# num_str = int(num_str)
# print(num_str, type(num_str))

# num = 100
# num = str(num)
# print(num, type(num))

# number = "15.79"
# number = float(number)
# print(number, type(number))

# year = "2020"
# year = int(year)
# print("3년 전 :", year - 3)
# print("2년 전 :", year - 2)
# print("1년 전 :", year - 1)
# print("올해 :", year)

# price = 48584
# month = 36
# sum = price * month
# print("총 가격 :", sum, "원")

# letters = 'python'
# print(letters[0], letters[2])

# license_plate = "24가 2210"
# print(license_plate[4:])

# string = "홀짝홀짝홀짝"
# print(string[0::2])

# string = "PYTHON"
# print(string[::-1])

# phone_number = "010-1111-2222"
# print(phone_number.replace("-", " "))

# phone_number = "010-1111-2222"
# print(phone_number.replace("-", ""))

# url = "http://sharebook.kr"
# print(url[-2:])

# url = "http://sharebook.kr"
# print(url.split(".")[1])

# lang = 'python'
# lang[0] = 'P'
# print(lang)

# string = 'abcdfe2a354a32a'
# print(string.replace("a", "A"))

# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# a = "3"
# b = "4"
# print(a + b)

# print("Hi" * 3)

# print("-" * 8)

# t1 = 'python'
# t2 = 'java'
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 :", name1, "나이 :", age1)
# print("이름 :", name2, "나이 :", age2)

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : %s 나이 : %d" %(name1, age1))
# print("이름 : %s 나이 : %d" %(name2, age2))

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : {} 나이 : {}".format(name1, age1))
# print("이름 : {} 나이 : {}".format(name2, age2))

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름 : {name1} 나이 : {age1}")
# print(f"이름 : {name2} 나이 : {age2}")

# 상장주식수 = "5,969,782,550"
# 상장주식수 = int(상장주식수.replace(",", ""))
# print(상장주식수, type(상장주식수))

# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# data = "   삼성전자   "
# print(data)
# print(data.replace(" ", ""))


# print("안녕하세요")

# ticker = "btc_krw"
# ticker = ticker.upper()
# print(ticker)

# ticker = "BTC_KRW"
# ticker = ticker.lower()
# print(ticker)

# name = "hello"
# name = name.capitalize()
# print(name)

# file_name = "보고서.xlsx"
# a = file_name.endswith("xlsx")
# print(file_name);print(a)

# file_name = "보고서.xlsx"
# a = file_name.endswith(("xlsx", "xls"))
# print(file_name)
# print(a)

# file_name = "2020_보고서.xlsx"
# a = file_name.startswith("2020")
# print(file_name)
# print(a)

# a = "hello world"
# b = a.split()
# print(a)
# print(b)

# ticker = "btc_krw"
# a = ticker.split("_")
# print(a)

# date = "2020-05-01"
# print("연도 :", date.split("-")[0])
# print("월 :", date.split("-")[1])
# print("일 :", date.split("-")[2])

# data = "039490    "
# print(data)
# data = data.split()
# print(data)

# import math

# def abs_sign(a):
#     if a >= 0:
#         return a
#     else:
#         return -a
    
# def square(a):
#     b = a * a
#     return math.sqrt(b)

# print(abs_sign(5))
# print(abs_sign(-3))
# print()
# print(square(5))
# print(square(-3))

# def sum_n(n):
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
#     return s

# print(sum_n(10))
# print(sum_n(100))

# def sum_n(n):
#     return n * ( n + 1 ) // 2

# print(sum_n(10))
# print(sum_n(100))

# def sum_n(n):
#     s = 0
#     for i in range (1, n+1):
#         s = s + ( i * i )
#     return s

# print(sum_n(10))

# def sum_n(n):
#     return (n * (n+1) * (2 * n + 1)) // 6

# print(sum_n(10))

# def find_max(a):
#     n = len(a)
#     max_v = a[0]
#     for i in range (1, n):
#         if a[i] > max_v:
#             max_v = a[i]
#         return max_v

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(find_max(v))

# def find_max_idx(a):
#     n = len(a)
#     max_idx = 0
#     for i in range(1, n):
#         if a[i] > a[max_idx]:
#             max_idx = i
#         return max_idx

# v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(find_max_idx(v))

# def find_same_name(a):
#     n = len(a)
#     result = set()
#     for i in range(0, n - 2):
#         for j in range(i + 1, n):
#             if a[i] == a[j]:
#                 result.add(a[i])
#     return result

# name1 = ["Tom", "Jerry", "Mike", "Tom"]
# print(find_same_name(name1))

# name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
# print(find_same_name(name2))

# def factorial(n):
#     f = 1
#     for i in range(1, n + 1):
#         f = f * i
#     return f

# print(factorial(1))
# print(factorial(5))
# print(factorial(10))

# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n - 1)

# print(fact(1))
# print(fact(5))
# print(fact(10))

# def gcd(a, b):
#     i = min(a, b)
#     if a % i == 0 and b % i == 0:
#         return i
#     i = i - 1
# print(gcd(1, 5))
# print(gcd(3, 6))

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# print(gcd(1, 5))
# print(gcd(60, 24))

# def hanoi(n, from_pos, to_pos, aux_pos):
#     if n == 1:
#         print(from_pos, "->", to_pos)
#         return
    
#     hanoi(n-1, from_pos, aux_pos, to_pos)
#     print(from_pos, "->", to_pos)

#     hanoi(n-1, aux_pos, to_pos, from_pos)

# print("n = 1")
# hanoi(1, 1, 3, 2)
# print("n = 2")
# hanoi(2, 1, 3, 2)
# print("n = 3")
# hanoi(3, 1, 3, 2)

# def search_list(a, x):
#     n = len(a)
#     for i in range (0, n):
#         if x == a[i]:
#             return i
#     return -1

# v = [17, 92, 18, 33, 58, 7, 44, 42]
# print(search_list(v, 18))
# print(search_list(v, 33))
# print(search_list(v, 900))

# def find_min_idx(a):
#     n = len(a)
#     min_idx = 0
#     for i in range (1, n):
#         if a[i] < a[min_idx]:
#             min_idx = i
#     return min_idx

# def sel_sort(a):
#     result = []
#     while a:
#         min_idx = find_min_idx(a)
#         value = a.pop(min_idx)
#         result.append(value)
#     return result
# d = [2, 4, 5, 1, 3]
# print(sel_sort(d))

# def sel_sort(a):
#     n = len(a)
#     for i in range(0, n-1):
#         min_idx = i
#         for j in range(i+1, n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]

# d = [2, 4, 5, 1, 3]
# sel_sort(d)
# print(d)

# def find_ins_idx(r, v):
#     for i in range(0, len(r)):
#         if v < r[i]:
#             return i
#     return len(r)

# def ins_sort(a):
#     result = []
#     while a:
#         value = a.pop(0)
#         ins_idx = find_ins_idx(result, value)
#         result.insert(ins_idx, value)
#     return result

# d = [2, 4, 5, 1, 3]

# print(ins_sort(d))

# def ins_sort(a):
#     n = len(a)
#     for i in range (1, n):
#         key = a[i]
#         j = i - 1
#         while j >= 0 and a[j] > key:
#             a[j + 1] = a[j]
#             j -= 1
#         a[j + 1] = key

# d = [2, 4, 5, 1, 3]
# ins_sort(d)
# print(d)

