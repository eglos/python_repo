'''
자주 봐줘야 할 챕터
많이 헷갈림
'''


'''
데이터 형식
    - text (텍스트) -> 문자열을 사용
    - binary (2진수)

'''
'''
텍스트 문자열 : 유니코드
파이썬의 unicodedata 모듈은 유니코드 식별자와 이름으로 검색할 수 있는 함수를 제공
    - lookup() : 인수로 대소문자를 구분하지 않는 이름을 취하고, 유니코드 문자를 반환
    - name() : 인수로 유니코드 문자를 취하고, 대문자 이름을 반환

'''
def unicode_test(value) :
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))
    
    
unicode_test('$')

'''
    UTF-8은 파이썬, 리눅스, HTML의 표준 텍스트 인코딩이다. 빠르고 완전하며 잘 동작한다.  
'''
''' 
정규표현식
    - 정규표현식으로 복잡한 문자열 패턴 매칭이 가능.
    - 정규 표현식은 임포트할 수 있는 표준 모듈  re로 제공된다.
'''
import re
result = re.match('You','Young Frankenstein')
# You는 패턴, 뒤의 문자열은 확인하고자 하는 소스

'''
    match() :  소스 처음부터 시작하는 패턴만 매칭
    search() : 소스 어디에서나 패턴을 찾아 매칭 (첫번째 일치하는 항목을 반환)
    findall() : 중첩에 상관없이 패턴에 일치하는 모든 문자열 리스트를 반환
    split() : 패턴에 맞게 소스를 쪼갠 후 문자열 조각의 리스트를 반환
    sub() : 대체 인수를 하나 더 받아서, 패턴에 일치하는 모든 소스 부분을 대체 인수로 변경
    
'''
import re
source = 'Young Frankenstein'
m = re.match('You', source) #match는 소스의 시작부터 패턴이 일치하는 지 확인
if m :
    print(m.group())


import re
source = 'Young Frankenstein'
m = re.search('Frank', source) #match는 소스의 시작부터 패턴이 일치하는 지 확인
if m :
    print(m.group())

import re
source = 'Young Frankenstein'
m = re.sub('n', '?', source) #match는 소스의 시작부터 패턴이 일치하는 지 확인
if m :
    print(m)
    
'''
2진 데이터
    - 이진 데이터를 다루기 위해서는 엔디언(endian)과 정수에 대한 사인 비트(sign bit)같은 개념을 알아야 한다.
    
    * 바이트(byte)는 바이트의 튜플처럼 불변
    * 바이트 배열(bytearray)은 바이트의 리스트처럼 가변
'''

# 이진 데이터 변환하기 : struct
'''
    - 파이썬 표준 라이브러리는 C와 C++의 구조체와 유사한, 데이터를 처리하는 struct 모듈이 있다.
    - struct를 사용하면 이진 데이터를 파이썬 데이터 구조로 바꾸거나 파이썬 데이터 구조를 이진 데이터로 바꿀 수 있다.
'''
