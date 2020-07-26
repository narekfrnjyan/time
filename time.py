from datetime import datetime
from sys import argv
if len(argv) >1 and argv[1]=='1':
    s=datetime.today().strftime('%Y.%m.%d')
    print(s)
if len(argv)>1 and argv[1] == '2':
    d=datetime.today().strftime('%Y.%m.%d %H:%M:%S')
    print(d)
if len(argv) > 1 and argv[1] == '3':
    date=datetime.today().isoformat()
    print(date)
if len(argv) > 1 and argv[1] == '4':
    d=datetime.today().strftime('%a %b %Y %H:%M:%S')
