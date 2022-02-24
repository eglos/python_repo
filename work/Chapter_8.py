# 딕셔너리 
# 리스트와 비슷 
# 오프셋으로 항목을 선택할 수 없다.
# 값에 상응하는 고유한 키를 지정
# Note : 다른 언어에서는 딕셔너리를 연관 배열, 해시, 해시맵이라고 부른다.


# 생성하기 : {}
empty_dict= {}
print(empty_dict)

bierce = {
    "day" : "A period of twenty-four hours, mostly misspent",
    "positive" : "Mistaken at the top of one's voice",
    "misfortune" : "The kind of fortune that never misses",
}

print(bierce)


# 생성하기 : dict()
# 일반적인 방법
acme_customer = {'first':'Wile' , 'middle':'E' , 'last':'Coyote'}
print(acme_customer)

# dict() 함수 사용법
# 제약 사항 : 인수 이름이 (공백과 예약어가 없는) 유효한 변수 이름이어야 한다.
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

# 변환하기 : dict()
# 두 항목의 리스트로 구성된 리스트 -> 딕셔너리로 변환
lol = [['a','b'],['c','d'],['e','f']]
lol_dicts = dict(lol)
print(lol_dicts)
# 두 항목의 리스트로 구성된 튜플 -> 딕셔너리로 변환
tol = (['a','b'],['c','d'],['e','f'])
tol_dicts = dict(tol)
print(tol_dicts)

# 두 문자열로 구성된 리스트 -> 딕셔너리로 변환
los = ['ab','cd','ef']
los_dicts = dict(los)
print(los_dicts)

# 두 문자열로 구성된 튜블 -> 딕셔너리로 변환
tos = ('ab','cd','ef')
tos_dicts = dict(tos)
print(tos_dicts)

# 항목 추가 / 변경 : [key]
pythons ={
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Idle' : 'Eric' , 
    'Jones' : 'Terry' , 
    'Palin' : 'Michael',
}

print(pythons)

pythons['Gilliam'] = 'Gerry'

print(pythons)

# 딕셔너리의 키들은 반드시 고유해야한다. 같은 키를 두번 이상 사용하면 마지막 값으로 저장됨.

some_pythons = {
    'Graham' : 'Chapman' ,
    'John' : 'Cleese' , 
    'Eric' : 'Idle' , 
    'Terry' : 'Gilliam' , 
    'Michael' : 'Palin' , 
    'Terry' : 'Jones',
}
print(some_pythons)

# 항목 얻기 : [key]와 get()
text = some_pythons['John']
print(text)

print('Groucho' in some_pythons)

t1 = some_pythons.get('John')
print(t1)

# 키가 존재하지 않으면, 옵션값을 지정해서 이를 출력할 수 있음
t2 = some_pythons.get('Groucho','Not a Python')
print(t2)

# 옵션값을 지정하지 않으면 None을 반환
t3 = some_pythons.get('Groucho')
print(t3)

# 모든 키 얻기 : keys()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
set1 = list(signals.keys())
print(set1)

# 모든 값 얻기 : values()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
set1 = list(signals.values())
print(set1)

# 모든 키-값 얻기 : items()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
set1 = list(signals.items())
print(set1)

# 길이 얻기 : len()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
lens = len(signals)
print(lens)

# 결합하기 : {**a, **b}
# 파이썬 3.5 부터는 **를 사용하여 딕셔너리를 결합할 수 있다.

first = {'a':'agony', 'b':'bliss' }
second = {'b':'bagels', 'c':'candy'}
conc = {**first, **second}
print(conc)

# 딕셔너리를 두 개 이상 결합할 수 있다.
third = {'d':'donuts'}
conc = {**first, **third, **second}
print(conc)


# 결합하기 : update()
pythons ={
    'Chapman' : 'Graham',
    'Cleese' : 'John',
    'Giiliam' : 'Terry',
    'Idle' : 'Eric' , 
    'Jones' : 'Terry' , 
    'Palin' : 'Michael'
}

print(pythons)

others = {'Marx' : 'Groucho', 'Howard':'Moe'}

pythons.update(others)

print(pythons)

# 결합할 때, 두 딕셔너리에서 같은 키 값을 가지는 항목은 두번째 값으로 value가 변경이 된다.

first = {'a':1 , 'b':2}
second = {'b':'platypus'}

first.update(second)
print(first)

# 키와 del로 항목 삭제하기
del pythons['Marx']
print(pythons)

del pythons['Howard']
print(pythons)


# 키로 항목 가져온 뒤 삭제하기 : pop()
lens = len(pythons)
print(lens)

text = pythons.pop('Palin')
print(text)

lens = len(pythons)
print(lens)

# 모든 항목 삭제하기 : clear()
pythons.clear()
print(pythons)

# 키 멤버십 테스트 : in
# 딕셔너리에 키가 존재하는지 알고 싶다면 in을 사용.
pythons = {'Chapman':'Graham','Cleese':'John','Jones':'Terry','Palin':'Michael','Idle':'Eric'}

print ('Chapman' in pythons)

print ('Palin' in pythons)

# 할당하기 : =
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
print(signals)
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
# 얕은 복사 : copy()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
original_signals = signals.copy()

signals['blue'] = 'confuse everyone'
print(signals)

print(original_signals)

# 깊은 복사 : deepcopy()
signals = {'green':'go','yellow':'go faster','red':['stop','smile']}
signals_copy = signals.copy()
print(signals)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy) #얕은 복사가 발생

# 깊은 복사 진행
import copy
signals = {'green':'go','yellow':'go faster','red':['stop','smile']}
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

#딕셔너리 비교
a = {1:1,2:2,3:3}
b = {3:3,1:1,2:2}
print(a == b)

# dict에는 비교연산자(<=, >=) 는 사용할 수 없다.

# 파이썬은 원래 생성된 키/값의 순서에 상관없이 딕셔너리의 키/값을 하나씩 비교
a = {1:[1,2], 2:[1], 3:[1]}
b = {1:[1,1], 2:[1], 3:[1]}
print(a == b)


# 순회하기 : for 와 in
accusation = {'room':'ballroom','weapon':'lead pipe','person':'Col.Mustard'}
for card in accusation : # or, for card in accusation.keys() : 
    print(card) # key 값들을 가져온다.
    
for value in accusation.values() :
    print(value)
    
for item in accusation.items() :
    print(item)
    
for card, contents in accusation.items() :
    print('Card', card , 'has the contents',contents)
    
# 딕셔너리 컴프리헨션
# {키_표현식 : 값_표현식 for 표현식 in 순회 가능한 객체}
word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}
print(letter_counts)


t = set(word)
print(t)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter : word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)

word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)} ### ??
print(letter_counts)


# set : 값은 버리고 키만 남은 딕셔너리와 같다.
#       딕셔너리와 마찬가지로 각 키는 유일해야 한다.

empty_set = set()
print(empty_set)

even_numbers = {0,2,4,6,8}
print(even_numbers)
odd_numbers = {1,3,5,7,9}
print(odd_numbers)

# 변환하기 : set()
print(set('letters')) # 문자가 두개씩 있어도 중복 제거하고 나타낸다.

# 리스트를 셋으로 만들기
tt1 = set(['Dasher','Dancer','Prancer','Mason-Dixon'])
print(tt1)

# 튜플을 셋으로 만들기 
tt2 = set(('Ummagumma','Echoes','Atom Heart Mother'))
print(tt2)

# 딕셔너리에 set()을 사용하면 키만 사용
tt3 = set({'apple':'red','orange':'orange','cherry':'red'})
print(tt3)

# 길이 얻기 : len()
reindeer = set (['Dasher','Dancer','Prancer','Mason-Dixon'])
print(len(reindeer))

# 항목 추가하기 : add()
s = set((1,2,3))
print(s)
s.add(4)
print(s)

# 항목 삭제하기 : remove()
s = set((1,2,3))
s.remove(3)
print(s)

# 순회하기 : for 와 in
furniture = set(('sofa','ottoman','table'))
for piece in furniture : 
    print(piece)
    
    
# 멤버십 테스트 : in
drinks = {
    'martini' : {'vodka','vermouth'},
    'black russian' : {'vodka','kahlua'},
    'white russian' : {'cream','kahlua','vodka'},
    'manhattan' : {'rye','vermouth','bitters'},
    'screwdriver' : {'orange juice','vodka'}
}

for name, contents in drinks.items() :
    if 'vodka' in contents :
        print(name)
        
for name, contents in drinks.items() :
    if 'vodka' in contents and not contents &{'vermouth','cream'} :
        print(name)
        
bruss = drinks['black russian']
wruss = drinks['white russian'] 

a = {1,2}
b = {2,3}

print(a&b)

print(a.intersection(b)) #교집합

print(bruss & wruss)

print(a | b)
print(a.union(b)) #합집합

print (bruss | wruss )

print ( a -  b) #차집합
print(a.difference(b))

print(bruss - wruss)

print(wruss - bruss)

print(a ^ b) # 대칭 차집합(여집합)
print(a.symmetric_difference(b))

print(bruss^wruss)

print(a <= b) #부분집합
print(a.issubset(b))

print(bruss <= wruss) 