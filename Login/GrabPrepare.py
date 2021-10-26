import time
import datetime
from Info import GetProjectInfo
from Login import FastLogin

Time = ['21:00', '21:37']


def GrabPrepare(session):
    while datetime.datetime.now().strftime('%H:%M') not in Time:
        print(datetime.datetime.now().strftime('%H:%M'))
        if GetProjectInfo.judgeOnline(session).text.find('"ReturnFlag": "1"'):
            print('此用户在线')
            time.sleep(5)
        else:
            print('用户断开进行重连')
            session = FastLogin.login()


