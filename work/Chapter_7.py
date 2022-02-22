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
b = marxes[::2]
print(b)
c = marxes[::-2]
print(c)

# 리스트 끝에 항목 추가 : append()
marxes=['Goucho','Chico','Harpo']
marxes.append('Zeppo')
print(marxes)

# 리스트 중간에 항목 추가 : 오프셋, insert()
marxes=['Goucho','Chico','Harpo']
marxes.insert(2,'Gummo')
print(marxes)

# 모든 항목 복제하기 : * 
t = ["blah"]*3
print(t)

# 리스트 병합하기 extend()와 +
marxes=['Goucho','Chico','Harpo','Zeppo']
others=['Gummo','Karl']
marxes.extend(others)
print(marxes)

marxes=['Goucho','Chico','Harpo','Zeppo']
others=['Gummo','Karl']
marxes+=others
print(marxes)

# extend를 사용하지 않고 append로 사용하면 항목을 병합하지 않고 others가 하나의 리스트로 추가가 됨
marxes=['Goucho','Chico','Harpo','Zeppo']
others=['Gummo','Karl']
marxes.append(others)
print(marxes)


# 오프셋으로 항목 바꾸기
marxes=['Goucho','Chico','Harpo']
marxes[2] = 'Wanda'
print(marxes)

# 슬라이스로 항목 바꾸기 
numbers = [ 1, 2, 3, 4]
numbers[1:3] = [8,9]
print(numbers)

numbers = [ 1, 2, 3, 4]
numbers[1:3] = [7,8,9] # 항목수가 달라도 insert 됨
print(numbers)


numbers = [ 1, 2, 3, 4]
numbers[1:3] = [] # 제거
print(numbers)

numbers = [ 1, 2, 3, 4]
numbers[1:3] = 'wat?' # 문자열이 한글자씩 한 오프셋으로 자리가 잡힘
print(numbers)

# 오프셋으로 항목 삭제하기
marxes=['Groucho','Chico','Harpo','Zeppo','Gummo','Karl']
del marxes[-1] #del 함수 사용
print(marxes)

del marxes[1] # 중간의 오프셋에 있는 항목을 삭제하면 앞으로 한칸 씩 당겨진다. 길이 감소
print(marxes)

# 값으로 항목 삭제하기 - 리스트에 같은 값으로 항목이 중복된다면, remove()는 첫번째 항목만 삭제시킴.
marxes=['Groucho','Chico','Harpo']
marxes.remove('Groucho')
print(marxes)

#오프셋으로 항목을 얻은 후 삭제하기 : pop()
marxes=['Groucho','Chico','Harpo','Zeppo']
pops = marxes.pop() #pop() 안에 인수가 없으면 기본값은 -1(끝 항목)
print('pops=',pops,'marxes= ',marxes)

pops = marxes.pop(1)
print('pops=',pops,'marxes= ',marxes)


## 참고 ##
# append()로 새로운 항목을 끝에 추가한 뒤 pop()으로 다시 마지막 항목을 제거했다면, 후입선출(LIFO - Last In First Out) 자료구조인 스택(stack)
# append()로 새로운 항목을 끝에 추가한 뒤 pop(0)을 이용했다면, 선입선출(FIFO - First In First Out) 자료구조인 큐(QUEUE)


# 모든 항목 삭제 : clear()
work_quotes = ['Working hard?','Quick question!','Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)

# 값으로 오프셋 찾기 : index()
marxes=['Groucho','Chico','Harpo','Zeppo']
a = marxes.index('Chico')
print(a)

simpsons = ['Lisa','Bart','Marge','Homer','Bart'] # 동일한 항목이 있을 경우 첫번째 오프셋만 반환
a = simpsons.index('Bart')
print(a)

# 존재 여부 확인하기 : in
marxes=['Groucho','Chico','Harpo','Zeppo']
print('Groucho' in marxes)

print('Bob' in marxes)

# 값 세기 : count()
marxes=['Groucho','Chico','Harpo']
print(marxes.count('Harpo'))


# 문자열로 변환하기 : join()
marxes=['Groucho','Chico','Harpo']
text = ','.join(marxes)
print(text) #반환되는 값은 문자열

# 정렬하기 : sort(), sorted()
# sort() : 리스트 자체를 내부적으로 정렬
# sorted() : 리스트의 정렬된 복사본을 반환
# 리스트 항목이 숫자면 오름차순, 문자면 알파벳순
marxes=['Groucho','Chico','Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)

marxes=['Groucho','Chico','Harpo']
marxes.sort() # 함수 실행
print(marxes)

#항목 개수 얻기 : len()
marxes=['Groucho','Chico','Harpo']
print(len(marxes))

# 할당하기
a = [1, 2, 3]
print('a=',a)
b = a
print('b=',b)
a[0] = 'surprise'
print('a=',a)
print('b=',b) # a 리스트의 항목이 바뀌면 b도 바뀐다.

b[0] = 'I have surprises'
print('b=',b)
print('a=',a)

#복사하기 : copy()-메서드, list()-변환 함수, 슬라이스 [:]
a = [1, 2, 3]
b = a.copy()    # 복사본 (새로운 객체) - a에 영향을 주지 않는다.
c = list(a)     # 복사본 (새로운 객체) - a에 영향을 주지 않는다.
d = a[:]        # 복사본 (새로운 객체) - a에 영향을 주지 않는다.

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)


# 깊은 복사 : deepcopy()
a = [1, 2, 3]
b = a.copy()    # 복사본 (새로운 객체) - a에 영향을 주지 않는다.
c = list(a)     # 복사본 (새로운 객체) - a에 영향을 주지 않는다.
d = a[:]        # 복사본 (새로운 객체) - a에 영향을 주지 않는다.

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
