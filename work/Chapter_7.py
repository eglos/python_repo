# 튜플과 리스트
# 파이썬의 문자열은 문자의 시퀀스
# 튜플 : 불변, 항목을 할당하고나면 변경할 수 없다.
# 리스트 : 가변, 항목을 할당하고 나서 자유롭게 수정 가능

# 튜플 ()
empty_tuple = ()
print(empty_tuple)

# 한 요소 이상의 튜플을 만들기 위해서는 각 요소 뒤에 콤마(,) 붙임.
one_marx = 'Groucho',
print(one_marx)

one_marx = ('Groucho',) #괄호 추가 가능
print(one_marx)


one_marx = ('Groucho') #요소 뒤에 콤마(,) 없으면 문자열이 됨.
print(one_marx)
print(type(one_marx))

marx_tuple = 'Groucho', 'Chico', 'Harpo' #요소가 두개 이상이면 마지막에 콤마를 붙이지 않는다.
print(marx_tuple)

# 쉼표만 사용하여 단일 요소를 가진 튜플을 만들 수 있지만, 함수에 인수로 전달할 수 없음
one_marx = 'Groucho',
print(type(one_marx))       # tuple
print(type('Groucho',))     # str
print(type(('Groucho',)))   # tuple

#튜플로 한 번에 여러 변수를 할당할 수 있음 -> 튜플 언패킹(tuple unpacking)
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
print(a) # marx_tuple(0)
print(b) # marx_tuple(1)
print(c) # marx_tuple(2)


# 튜플 생성
marx_list = ['Groucho', 'Chico', 'Harpo'] #리스트
marx_tuple = tuple(marx_list)
print(marx_tuple)

# 항목 복제 : *
marx_tuple = ('yada',) * 3
print(marx_tuple)

#비교하기 : 리스트 비교와 같음
a = (7,2)
b = (7,2,9)
print(a==b)
print(a<=b)
print(a<b)

# for와 in
words = ('fresh','out','of','ideas')
for word in words :
    print(word)
    
# 수정하기
# 튜플은 문자열처럼 불변 객체이므로 기존 튜플을 변경할 수 없음.
# 문자열과 같이 튜플을 결합하여 새 튜플을 만들 수 있음.

t1 = ('Fee','Fie','Foe')
print(id(t1))
t2 = ('Flop',)
t3 = t1 + t2
print(t3)
t1 += t2
print(id(t1))
print(t1)


# ==============================================================
# 리스트 
# 1. 데이터를 순차적으로 파악하는 데 유용, 변경 가능
# 2. 내용의 순서가 바뀔 수 있음

empty_lsit = []
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
big_birds = ['emu','ostrich','cassowary']
first_names = ['Graham','John','Terry','Terry','Michael'] #값의 고유하지 않아도 됨

# 리스트 생성 및 변환 : list()
another_empty_list = list()
print(another_empty_list) # [] 
# list() 함수는 다른 데이터 타입(튜플, 문자열, 셋, 딕셔너리 등)을 리스트로 변환
t = list('cat')
print(t) #문자열을 한 단어씩 분할

a_tuple = ('ready','fire','aim')
a = list(a_tuple)
print(a) # 튜플을 리스트 형태로 변환

# 문자열 분할로 생성하기 : split()
talk_like_a_pirate_day = '9/19/2019'
t = talk_like_a_pirate_day.split('/')
print(t)

splitme='a/b//c/d///e'
s= splitme.split('/')
print(s)
ss= splitme.split('//')
print(ss)

# offset으로 항목 얻기
marxes=['Goucho','Chico','Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1]) #끝에서부터 거꾸로 값을 추출할 수 있다.
print(marxes[-2])
print(marxes[-3])

#슬라이스로 항목 얻기
marxes=['Goucho','Chico','Harpo']
a = marxes[0:2] # 0부터 (2-1)까지
print(a)