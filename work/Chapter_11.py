"""
    모듈과 패키지
"""

# 모듈과 import문
# 모듈 import 하기
'''
    Chap_11 폴더의 
    fast.py
    fast2.py
    lunch.py
'''


# 다른 이름으로 모듈 임포트하기
'''
    Chap_11 폴더의 
    fast3.py
'''

# 필요한 모듈만 임포트하기
'''
    Chap_11 폴더의 
    fast4.py
    fast5.py
'''

# 패키지
'''
    - 파이썬 애플리케이션을 좀 더 확장하기 위해 모듈을 패키지(package)라는 파일과 모듈 계층 구조에 구성할 수 있다.
    - 패키지는 .py 파일을 포함한 하위 디렉터리
    - 또한 디렉터리 안에 디렉터리를 여러 깊이로 사용할 수 있다.
    
    Chap_11 폴더의
    questions.py
    
    sources 폴더의
    choice/advice.py
    choice/fast.py
'''


# 모듈 탐색 경로
'''
    - 파이썬 인터프리터가 보는(임포트하는) 모든 위치를 보려면 표준 sys 모듈을 임포트해서 path 리스트를 살펴본다.
'''
import sys
from typing import OrderedDict
for place in sys.path :
    print(place)
    
'''
    - 코드 내에서 탐색 경로를 수정할 수 있다.
    - 파이썬이 다른 것보다 먼저 /my/modules 디렉터리에서 탐색하길 원한다고 가정하면 다음과 같이 코드를 추가
'''
import sys
sys.path.insert(0,"/my/modules")


# 상대/절대 경로 임포트
'''
    - 파이썬은 절대 또는 상대 경로 임포트를 지원한다.
'''

'''
from . import work1 # 현재 경로 import
from .. import xx # 상위 경로 import
'''

# 네임 스페이스 패키지
'''
    헷갈림...
'''


# 파이썬 표준 라이브러리
# 누락된 키 처리하기 : setdefault() 와 defaultdict()
'''
setdefault : 존재하는 키에는 할당 못함
'''
periodic_table = {'Hydrogen':1, 'Helium':2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon',12)
print(periodic_table)

# 항목 세기 : Counter()
from collections import Counter
breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

# 데크 (스택 + 큐)
'''
    데크(deque)는 스택과 큐의 기능을 모두 가진 출입구가 양 끝에 있는 큐
    데크는 시퀀스의 양 끝으로부터 항목을 추가하거나 삭제할 때 유용하게 쓰임
'''
def palindrome(word) :
    from collections import deque
    dq = deque(word)
    while len(dq) > 1 :
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('radar'))

# 깔끔하게 출력하기 : pprint
from pprint import pprint
quotes = OrderedDict([('Moe','A wise guy, Huh?'),
                      ('Larry',';Ow!'),
                      ('Curly','Nyuk nyuk!'),
                      ])

print(quotes)

pprint(quotes)