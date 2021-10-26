import json
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}


def getSubjectInfo(session):
    subjectUrl = 'http://10.100.0.121:8020/UI/wxInterface/syjx.asmx/getRuleItem'
    data = {'page': '1', 'limit': '20', 'jxrwid': '423'}

    result = json.loads(session.post(url=subjectUrl, headers=headers, json=data).json()['d'])['data']
    with open("./Data/SubjectInfo.json", 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def getSubjectInfoTime(session, chooseNum):
    subjectUrl = 'http://10.100.0.121:8020/UI/wxInterface/syjx.asmx/getItemTime'
    data = {'page': '1', 'limit': '30', 'jxrwid': '423', 'xmid': chooseNum}
    while True:
        if judgeOnline(session).text.find('"ReturnFlag": "1"'):
            print('正在攻克ing！！！')
        result = session.post(url=subjectUrl, headers=headers, json=data)
        if result.text.find(r'\"ZC\":\"9\",') != -1:
            return json.loads(result.json()['d'])['data']
        else:
            time.sleep(5)
            continue


def judgeOnline(session):
    isLoginUrl = 'http://10.100.0.121:8020/UI/wxInterface/syjx.asmx/IsLogin'

    return session.post(url=isLoginUrl, headers=headers)
