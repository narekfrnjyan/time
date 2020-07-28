from datetime import datetime
from sys import argv
from pytz import timezone
import pytz
import time
if len(argv) >1 and argv[1]=='1':
    s=datetime.today().strftime('%Y.%m.%d')
    print(s)
if len(argv)>1 and argv[1] == '2':
    d=datetime.today().strftime('%Y.%m.%d %H:%M:%S')
    print(d)
if len(argv) > 1 and argv[1] == '3':
    armenia = timezone('asia/yerevan')
    loc_dt = armenia.localize(datetime.now())
    arm_dt=loc_dt.astimezone(armenia)   
    fmt = '%a %b %Y %H:%M:%S %z'
    print(arm_dt.strftime(fmt))
