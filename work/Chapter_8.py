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
set = list(signals.keys())
print(set)

# 모든 값 얻기 : values()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
set = list(signals.values())
print(set)

# 모든 키-값 얻기 : items()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
set = list(signals.items())
print(set)

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

