'''
    DictWriter() 함수를 사용하여 CSV 파일을 다시 써보자. 또한 CSV 파일의 첫 라인에 열 이름을 쓰기 위해 writeheader() 함수를 호출한다.
'''
import csv

villains = [{'first': 'Doctor', 'last': 'No'}, {'first': 'Rosa', 'last': 'Klebb'}, {'first': 'Mister', 'last': 'Big'}, {'first': 'Auric', 'last': 'Goldfinger'}, {'first': 'Ernst', 'last': 'Blofeld'}]

with open('villains.csv','wt') as fout :
    cout = csv.DictWriter(fout,['first','last'])
    cout.writeheader()
    cout.writerows(villains)