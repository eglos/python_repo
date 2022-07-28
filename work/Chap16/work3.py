'''
    - 리스트의 리스트가 아닌 딕셔너리의 리스트로 데이터를 만들 수 있다.
    - villains 파일을 다시 한번 읽어보자.
    - 이번에는 DictReader() 함수를 사용하여 열 이름을 지정한다.
'''

import csv
with open('villains','rt') as fin :
    cin = csv.DictReader(fin, fieldnames=['first','last'])
    villains=[row for row in cin]
    
print(villains)

