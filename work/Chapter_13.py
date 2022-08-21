'''
날짜와 시간
'''
'''
책 내용 좀 더 파악 필요
'''
# 윤년
import calendar
print(calendar.isleap(1999))

# datatime 모듈
'''
    date : 년 월 일
    time : 시 분 초 마이크로초
    datetime : 날짜 시간
    timedelta : 날짜 및 시간 간격
'''
from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.day)

from datetime import date
now = date.today()
print(now)

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
