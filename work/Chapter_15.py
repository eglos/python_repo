'''
    프로세스와 동시성
        - 하나의 프로그램을 실행할 때, 운영체제는 한 프로세스를 생성
'''

# 실행 중인 파이썬 인터프리터에 대한 프로세스 ID와 현재 작업 디렉터리 위치
import os
print(os.getpid())

print(os.getcwd())

#import subprocess #유닉스에서 실행 가능
#ret = subprocess.getoutput('date')


# 프로세스 죽이기 : terminate()


# 시스템 정보 보기 : os
import os
#print(os.uname) #없음

#import psutil
#print(psutil.cpu_times(True))
from invoke import task
@task
def mytime(ctx) :
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local time is", time_str)

import subprocess
ret = subprocess.getoutput('date')
print(ret)