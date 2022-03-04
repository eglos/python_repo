# 함수
# 코드의 재사용을 위해 함수를 사용
# define : 0개 또는 1개 이상의 매개변수를 갖는다.
# call : 0개 또는 1개 이상의 결과를 얻는다.

# 함수 정의하기 : def
# def와 함수이름, 괄호를 입력 . 괄호 안에는 옵션으로 매개변수(parameter)입력. 그리고 마지막으로 콜론(:)을 붙인다.
# 함수 이름의 첫글자는 반드시 영문자나 언더바(_)를 사용해야 한다. 그리고 영문자, 숫자, 언더바만 사용할 수 있다.

def do_nothing() :
    print("pass!")
    pass


# 함수 호출하기 (call function)
do_nothing()

def make_a_sound() :
    print('quack')

make_a_sound()

def agree() :
     return True #True 반환

if agree() :
     print('Splendid!')
else :
      print('That was Unexpected.')




# 인수와 매개변수
# 함수 외부에서는 인수라고 부르지만, 함수 내부에서는 매개변수임   
def echo(anything) :
    return print(anything + ' ' + anything) #매개변수

echo('Rump') #인수


# 인수를 취하는 함수 작성
def commentary(color) :
    if color == 'red' :
        return "It's a tomato."
    elif color == 'green' :
        return "It's a green pepper."
    elif color == 'bee purple' :
        return "I don't know what it is, but only bees can see it."
    else :
        return "I've never heard of the color " + color + '.'

comments = commentary('blue')
print(comments)

print(do_nothing())

# 유용한 None
thing = None
if thing : 
    print("It's some thing")
else :
    print("It's no thing")
    

if thing is None : #빠뜨린 빈 값을 구분하기 위해 None을 사용한다. 
    print("It's some thing")
else :
    print("It's no thing")


# 정수(0) 혹은 부동소수점 숫자(0.0), 빈 문자열(''), 빈 리스트([]), 빈 튜플 ((,)), 빈 딕셔너리({}), 빈 셋(set())은 모두 False지만, None과 같지 않다는 점 유의
def whatis(thing) :
    if thing is None :
        print(thing,'is None')
    elif thing :
        print(thing,'is True')
    else :
        print(thing,'is False')


whatis(None) 

whatis(True) 

whatis(False) 


# 위치 인수
def menu(wine, entree, dessert) :
   return {'wine' : wine, 'entree' : entree, 'dessert' : dessert}
    
t1 = menu('chardonnay','chicken','cake') 
   
   
print(t1)

t2 = menu('beef','bagel','bordeaux') 
print(t2)

# 키워드 인수
# 위치 인수의 혼란을 피하기 위해 매개변수에 상응하는 이름을 인수에 지정할 수 있다.
t3 = menu(entree='beef',dessert='bagel',wine='bordeaux')
print(t3)

# 기본 매개변수 값 지정하기
def menu(wine, entree, dessert = 'pudding') :
     return {'wine' : wine, 'entree' : entree, 'dessert' : dessert}
 
print(menu('chardonnay','chicken'))

print(menu('dunkelfelder','duck','doughnut'))

def buggy(arg, result = []) : 
    result.append(arg)
    print(result)

buggy('a')

buggy('b') # 함수에 기본매개변수로 리스트를 취하면, 인수를 넣었을 때 이전 인수는 리스트에 그대로 남아있음.

# 수정
def works(arg) :
    result = [] #함수 실행할 때마다 빈 리스트 선언
    result.append(arg)
    print(result)
    
works('a')    

works('b')

#첫번째 인수 호출을 가리키기 위해 매개변수에 다른 값을 넣어서 수정할 수 있다. (가끔 파이썬 기술 면접에 등장)   **************************************************
def nonbuggy(arg, result=None) :
    if result is None :
        result = []
    result.append(arg)
    print(result)
    
nonbuggy('a')

nonbuggy('b')


# 위치 인수 분해하기/모으기 : *
# 애프터리스크(*)

def print_args(*args) : # 튜플 반환
    print('Positional tuple :', args)
    
# 함수를 인수 없이 호출하면 *args에는 아무것도 없음
print_args()

# 함수에 인수를 넣어서 args 튜플 출력
print_args(3,2,1,'wait!','uh...')

# 가변 인수를 사용하는 print()와 같은 함수는 매우 유용
# 함수에 위치 인수를 지정할 때 맨 끝에 *args를 써서 나머지 인수 모두 취하게 할 수 있음 
def print_more(required1, required2, *args) :
    print('Need this one:',required1)
    print('Need this one. too:',required2)
    print('All the rest:',args)
    
print_more('cap','gloves','scarf','monocle','mustache wax')

# ''' 또는 """ : 여러줄 주석
''' 
* 요약
1. 위치 인수를 함수에 전달하면, 함수 내 위치 매개변수와 일치
2. 튜플 인수를 함수에 전달하면, 함수 내 튜플 매개변수가 있다
3. 위치 인수를 함수에 전달하고, 매개변수 *args로 수집하여 튜플 인수로 해석할 수 있다.
4. args라는 튜플 인수를 함수에 전달하여, 위치 매개변수 *args로 분해할 수 있다. 이것은 튜플 매개변수 args 안에 다시 수집된다.
'''

print_args(2,5,7,'x')

args = (2,5,7,'x') 
print_args(args) # 튜플을 하나의 항목으로 인식
print_args(*args) # 튜플 안의 항목들을 한개씩 인식


'''
# 키워드 인수 분해하기/모으기 : *
1. 키워드 인수를 딕셔너리로 묶기 위해 두 개의 애스터리스크(**) 사용
2. 인수의 이름은 키고, 값은 이 키에 대응하는 딕셔너리 값.
'''

def print_kwargs(**kwargs) :
    print('Keyword arguments: ',kwargs)
    
print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


'''
함수 내에서 kwargs는 딕셔너리 매개변수. 

* 인수 순서
- 위치 인수
- 위치 인수(*args) - 옵션
- 키워드 인수(**kwargs) - 옵션

* 요약
1. 키워드 인수를 함수에 전달하면, 함수 내 키워드 매개변수와 일치
2. 딕셔너리 인수를 함수에 전달하면, 함수 내 딕셔너리 매개변수가 있음
3. 하나 이상의 키워드 인수(이름=값)를 함수에 전달하고 이름 **kwargs에 수집하여, kwargs 딕셔너리 매개변수로 해석할 수 있다.
4. 함수 외부에서 **kwargs는 딕셔너리 kwargs를 '이름=값' 인수로 분해
5. 함수 내부에서 **kwargs는 '이름=값' 인수를 단일 딕셔너리 매개변수 kwargs에 모은다.
''' 


# 키워드 전용 인수
'''
    파이썬 3에서는 키워드 전용 인수를 지정할 수 있다.
'''
def print_data(data, *, start=0, end=100) :
    for value in (data[start:end]) :
        print(value)
        
data = ['a','b','c','d','e','f','g']
print_data(data)

print("="*100)

print_data(data,start=4)

print("="*100)

print_data(data,end=2)


# 가변/불변 인수
'''
함수에 인수를 전달할 때 주의, 인수가 가변 객체인 경우 해당 매개변수를 통해 함수 내부에서 값을 변경할 수 있음.
'''

outside = ['one','fine','day']
def mangle(arg) :
    arg[1] = 'terrible!'

mangle(outside)    

print(outside)

# 독스트링
'''
함수 바디 시작 부분에 문자열을 포함시켜 함수 정의에 문서를 붙일 수 있음
'''

def echo(anything) :
    'echo returns its input argument'
    return anything


def print_if_ture(thing,check) :
    '''
    Prints the first argument if a second argument is true.
    The operation is :
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    
    if check :
        print(thing)
        
help(echo)


print(echo.__doc__) # __doc__은 docstring의 내부 이름인 함수 내의 변수

# 일등시민 : 함수
'''
    객체는 숫자, 문자열, 튜플, 리스트, 딕셔너리, 함수를 포함
    파이썬에서 함수는 일등시민 : 함수를 변수에 할당하고, 다른 함수에서 이를 인수로 사용하고, 함수에서 이를 반환할 수 있음 
'''

def answer() : 
    print(42)
    
answer()

def run_something(func) :
    func()
    
run_something(answer)

print(type(run_something))

# 함수 arg1+arg2

def add_args(arg1, arg2) :
    print(arg1+arg2)
    
def run_something_with_args(func,arg1,arg2) :
    func(arg1,arg2)

run_something_with_args(add_args, 2, 3)

def sum_args(*args) :
    return sum(args)

def run_with_positional_args(func,*args) :
    return func(*args)

print(run_with_positional_args(sum_args,1,2,3,4))


# 내부 함수
'''
    함수 안에 또 다른 함수를 정의할 수 있다.
'''

def outer(a,b) :
    def inner(c,d) :
        return c+d
    return inner(a,b)

print(outer(4,3))


# 클로저 . 클로저는 다른 함수에 의해 동적으로 생성된다.
def knights2(saying) :
    def inner2() :
        return "We are the knights who say : '%s'" % saying
    return inner2

a = knights2('Duck')
print (a())
b = knights2('Hasenpfeffer')
print (b())



# 익명 함수 : lambda
'''
    파이썬 람다함수는 단일 문장으로 표현되는 익명 함수
'''
def edit_story(words, func) :
    for word in words :
        print(func(word))
    
stairs = ['thud','meow','thud','hiss']

def enliven(word) : # 첫글자를 대문자로 만들고 느낌표 붙이기
    return word.capitalize() + '!'

edit_story(stairs, enliven)


# lambda 사용
edit_story(stairs, lambda word : word.capitalize() + '!')


# 제너레이터  : 시퀀스를 생성하는 객체
'''
    시퀀스를 생성하는 함수를 작성하여 활용할 수 있음
'''
print(sum(range(1,101)))


# 데커레이터 (decorator)
'''
    하나의 함수를 취해서 또 다른 함수를 반환하는 함수.
    이 파이썬 트릭을 사용하기 위해 다음 기술을 사용 
        - *args 와 **kwargs
        - 내부 함수
        - 함수 인수
'''

#예시
def document_it(func) :
    def nuw_function (*args, **kwargs) :
        print('Running function:',func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:',kwargs)
        result = func(*args,**kwargs)
        print('Result:',result)
        return result # 함수 반환
    return nuw_function


## 데커레이터 사용
def add_ints(a,b):
    return a+b

add_ints(3,5) #8

cooler_add_ints = document_it(add_ints) #데커레이터 수동 할당
print(cooler_add_ints(3,5))

# 위와 같이 수동으로 데커레이터를 할당하는 대신, 다음과 같이 데커레이터를 사용하고 싶은 함수에 그냥 @데커레이터_이름을 추가한다.
@document_it
def add_ints(a,b) :
    return a + b

add_ints(3,5)

# 함수는 여러 데커레이터를 가질 수 있다. 
# result를 제곱하는 square_it() 데커레이터 작성
def square_it(func) :
    def new_function(*args, **kwargs) :
        result = func(*args, **kwargs)
        return result * result
    return new_function


print("*"*100)

@document_it
@square_it
def add_ints(a,b) :
    return a + b

print(add_ints(3,5))
'''
Running function: new_function
Positional arguments: (3, 5)
Keyword arguments: {}
Result: 64
'''

print("*"*100)

@square_it
@document_it
def add_ints(a,b) :
    return a + b

print(add_ints(3,5)) #데코레이터 순서를 바꾸면 결과는 같으나, 중관 과정이 달라짐을 유의

# 네임스페이스와 스코프 (** 중요)
'''
파이썬 프로그램에는 다양한 네임스페이스가 있다.
네임스페이스는 특정 이름이 유일하고, 다른 네임스페이스에서의 같은 이름과 관계가 없는 것을 말한다.
'''
'''
# 메인 프로그램은 전역 네임스페이스를 정의
# 메인 프로그램의 네임스페이스에서 선언된 변수는 전역변수이다.
'''

animal = 'fruitbat' #전역변수
def print_global() :
    print('insid print_global:',animal)
    
    
print('insid print_global:',animal)
print_global()

# 함수에서 전역 변수의 값을 얻어서 바꾸려하면 에러 발생
def change_and_print_global():
    print('inside change_and_print_global:',animal)
    animal = 'wombat'
    print('after the change:', animal)


#change_and_print_global() #전역변수를 수정하여 에러 발생

# 함수 내에서 전역 변수와 이름이 같은 변수 animal을 변경할 때, 함수 내 animal 변수를 변경한다.
def change_local() :
    animal = 'wombat'
    print('inside change_local:',animal, id(animal))
    
change_local()

print(id(animal)) #함수 내의 animal 객체의 id와 전역변수 animal의 id는 다름 (다른 객체 같은 이름)

# 함수 내의 지역 변수가 아닌 전역 변수를 접근하기 위해 global 키워드 사용
animal = 'fruitbat'
def change_and_print_global() :
    global animal # global 키워드 사용
    animal = 'wombat'
    print('after the change:', animal)
    
change_and_print_global()

'''
    - 파이썬은 네임스페이스의 내용을 접근하기 위해 두가지 함수 제공
        * locals() 함수는 로컬(지역) 네임스페이스의 내용이 담긴 딕셔너리를 반환
        * globals() 함수는 글로벌(전역) 네임스페이스의 내용이 담긴 딕셔너리를 반환
'''

animal = 'fruitbat' #전역변수 
def change_local() :
    animal = 'wombat' #지역변수
    print('locals:',locals())
    
change_local()

print('globals:',globals())
print(animal)

# 이름에 _ 와  __ 사용하기
'''
    - 언더바 두개(__)로 시작하고 끝나는 이름은 파이썬 내부 사용을 위해 예약되어 있다.
    - 그러므로 변수를 선언할 때 두 언더바를 사용하면 안된다 (************)
'''

def amazing() :
    '''
        This is the amazing function.
        Want to see it again?
    '''
    print('This function is named:',amazing.__name__)
    print('And its docstring is:',amazing.__doc__)
    
