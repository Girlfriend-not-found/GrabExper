from Login import FastLogin, GrabPrepare
from Info import GetProjectInfo
from Attach import tableShow


def GrabExper(session):
    subjectUrl = 'http://10.100.0.121:8020/UI/wxInterface/syjx.asmx/Addksxmtu'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'}

    print("""
          █████▒ █    ██  ▄████▄   ██ ▄█▀   ▓█████ ▒██   ██▒ ██▓███  ▓█████  ██▀███  
        ▓██   ▒  ██  ▓██▒▒██▀ ▀█   ██▄█▒    ▓█   ▀ ▒▒ █ █ ▒░▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
        ▒████ ░ ▓██  ▒██░▒▓█    ▄ ▓███▄░    ▒███   ░░  █   ░▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
        ░▓█▒  ░ ▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄    ▒▓█  ▄  ░ █ █ ▒ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
        ░▒█░    ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄   ░▒████▒▒██▒ ▒██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
         ▒ ░    ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░░ ▒░ ░▒▒ ░ ░▓ ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
         ░      ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░    ░ ░  ░░░   ░▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
         ░ ░     ░░░ ░ ░ ░        ░ ░░ ░       ░    ░    ░  ░░          ░     ░░   ░ 
                   ░     ░ ░      ░  ░         ░  ░ ░    ░              ░  ░   ░     
                         ░                                                           
        """)
    print("----------------------------------------------------------------------------------------")

    GetProjectInfo.getSubjectInfo(session)

    XMMC_table = tableShow.tableShowSub()

    chooseNum = eval(input('\033[1;32;40m请选择需要的实验！！！！（输入num即可）：\033[0m'))
    '''for i in range(1, 4):
        print("星期1-7对应数字1-7，实验时间1-3对应10点13点16点")
        chooseNumTime.append(eval(input('第'+ i +'次' + '请选择需要的实验时间！！！！！输入格式如：星期三13：30表示(3,b)')))
    '''
    GrabPrepare.GrabPrepare(session)

    kbid_table = tableShow.tableShowSubTime(GetProjectInfo.getSubjectInfoTime(session, XMMC_table[chooseNum]))
    while True:
        chooseNumTime = eval(input('请选择需要的实验时间！！！'))

        data = {'kbid': kbid_table[chooseNumTime], 'jxrwid': '423', 'xmid': '272'}
        result = session.post(url=subjectUrl, headers=headers, json=data)
        if result.text.find('成功') != -1:
            print(result.text)
            print('恭喜你成功选上了实验')
            exit()
        elif result.text.find('批次人数已满') != -1:
            print('本次实验人数达到上限！！！！')
            if eval(input('是否继续选择这门实验？（继续-1，选择其他-2）')) == 1:
                continue
            else:
                chooseNum = eval(input('请选择需要的实验！！！！（输入num即可）'))
                kbid_table = tableShow.tableShowSubTime(
                    GetProjectInfo.getSubjectInfoTime(session, XMMC_table[chooseNum]))
                continue
        print(result.text)


if __name__ == '__main__':
    GrabExper(FastLogin.login())
