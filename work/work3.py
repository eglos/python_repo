# 5장
# 
# 텍스트 문자열
# 작은따옴표(') 나 큰 따옴표(")로 사용 가능

# f 또는 F로 시작하는 문자열은 f-문자열 : 포매팅에 사용
# r 또는 R로 시작하는 문자열은 r-문자열 : 이스케이프 시퀀스를 방지하는데 사용
# 두 조합인 fr-문자열 : 원시 f-문자열
# u-문자열 : 유니코드 문자열
# b-문자열 : 바이트 타입

# 여러줄 문자열 표시
str = ''' there was a Young Lady of Norway,
Who casually sat in a doorway;'''
print(str)

# 문자열 타입으로 변환 (cmd로 확인)

# 이스케이프 문자 : \
# 여러 형태를 통해 문자열을 표현할 수 있다.

palindrome = 'A mans,\nA plan,\nA canal:\nPanama.' # \n : 줄바꿈
print(palindrome) 

print('\tabc') # \t : tab
print('a\tbc')
print('ab\tc')

# 특수기호 앞에 \을 쓰면 해당 특수기호를 표현할 수 있다. 예) \" -> "
print ("\" I did morning!\" and I did.")

# r문자열(원시문자열) : 이스케이프 문자 무효화
print(r'Type a \n to get a new line in a normal string')

# 결합 : 문자열끼리 결합할 수 있다
print('I' + 'am')
print ('I' 'AM') #리터럴 문자열(문자열 변수 x)을 왼쪽과 같이 결합할 수 있다.

str = ('a' "t" '''c''' """d""")
print(str)

# 복제 : * 를 통해 복제 가능
str = 'Na'*4 + 't'
print(str)

# 문자 추출 : [] 사용, 오프셋 추출
letters='abcdefg'
print(letters[0])
print(letters[2])
print(letters[4])

name = 'Henny'
name.replace('H','P')
print('P'+name[1:])


# 슬라이스 : 문자열 추출
# [:] : 처음부터 끝까지 전체 시퀀스 추출
# [start:] : start 오프셋부터 끝까지 추출
# [:end] : 처음부터 end-1 오프셋까지 추출 
# [start:end] start부터 end-1 까지 추출
# [start:end:step] : step만큼 문자를 건너뛰면서 start 부터 end-1까지 추출

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[20:])
print(letters[12:15])
print(letters[-3:])
print(letters[-6:-2])
print(letters[::7])

# 문자열 길이 : len()

# 문자열 나누기 : split() , 기준을 정하지 않으면 공백(' ')으로 default

tasks = 'get gloves, get mask, give cat vitamins, call ambulance'
task = tasks.split(',')
print(task)

# 문자열 결합 : join() 
crypto_list = ['Yeti','Bigfoot','Loch Ness Moster']
crypto_string = ','.join(crypto_list)
print('Found and signing book deals:', crypto_string)


# 문자열 대체 : replace()
setup = "a duck goes in to a bar ..."
setups = setup.replace('duck','marmoset')
print(setups)

# 문자열 스트립 : strip() 
# 문자열 맨 앞(왼쪽) 또는 맨 뒤(오른쪽)에서 '패딩'문자 (여백 또는 공백 문자) 제거
# 메서드에 인수가 없다면 공백 문자(' ', '\t', '\n')를 양쪽 끝에서 제거
world = " earth "
tworld = world.strip()
print(tworld)
tworld = world.strip(' ')
print(tworld)
lworld = world.lstrip()
print(lworld)
rworld = world.rstrip()
print(rworld)
blurt = "What the...!!?"
blurts = blurt.strip('.?!')
print(blurts)

# str.startwith('문자열')
# ~~ 로 시작하는가? return : True, False
# str.endwith('문자열')

# 오프셋을 찾기위한 메서드 (find(), index())

poem = ''' All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

word = 'the'
print(poem.find(word))

print(poem.index(word))

print(poem.rfind(word))

print(poem.count(word)) # 해당 단어 포함 갯수


# str.isalnum() : 모두 숫자로 이루어져 있는가?

# 대소문자
setup = 'a duck goes into a bar...'

setup_r = setup.strip('.')
print(setup_r)

setup_s = setup_r.capitalize() # 문자열의 첫 글자 대문자
print(setup_s)

setup_q = setup_r.title() # 문자열의 첫 단어들을 대문자로 표시
print(setup_q)

setup_w = setup_r.upper() # 문자열 모두 대문자
print(setup_w)


# 정렬
setup = 'a duck goes into a bar...'
setup_c = setup.center(30)
print(setup_c)
setup_l = setup.ljust(30)
print(setup_l)
setup_r = setup.rjust(30)
print(setup_r)


#formatting (포매팅)
#옛 스타일 : %
# format_string % data
# %s : 문자열
# %d : 10진수
# %x : 16진수
# %o : 8진수
# %f : 10진 부동소수점
# %e : 지수로 나타낸 부동소수점
# %g : 10진 부동소수점 혹은 지수로 나타낸 부동소수점

#새 스타일 : {}, format()
# {:10s}
# {:<10s} : 왼쪽 정렬 (<)
# {:>10s} : 오른쪽 정렬 (>)
# {:^10s} : 가운데 정렬 (^)

#최신 스타일 : f-문자열
# 문자열 앞에 f나 F를 붙여서 사용
# 중괄호({}) 안에 표현식 사용 가능

#%%
thing = 'wereduck'
place = 'werepond'

f'The {thing} is in the {place}'

f'The {thing.capitalize()} is in the {place.rjust(20)}'

f'The {thing.capitalize()} is in the {place:.^20}'