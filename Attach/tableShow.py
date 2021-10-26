from prettytable import PrettyTable
import json
import time


def tableShowSub():
    d = dict()
    subInfoTable = PrettyTable()

    subInfoTable.field_names = ['Num', '项目编号', '项目名称', '选课状态', '选课详情']

    with open('./Data/SubjectInfo.json', 'r') as f:
        result = json.load(f)
    for i, li in enumerate(result):
        subInfoTable.add_row([i, li['XMBH'], li['XMMC'], li['XKZT'], li['XKXQ']])
        d[i] = li['XMID']
    else:
        time.sleep(2)
        print(subInfoTable)
        return d


def tableShowSubTime(time):
    d = dict()
    subTimeInfoTable = PrettyTable()

    subTimeInfoTable.field_names = ['sub_num', '周次', '星期', '日期', '任课教师', '容量', '上课时间', '房间编号']

    for i, li in enumerate(time):
        subTimeInfoTable.add_row([i, li['ZC'], li['XQ'], li['SKRQ'], li['ZJJSXM'], li['RS'], li['SKSJ'], li['FJBH']])
        d[i] = li['ID']
    else:
        print(subTimeInfoTable)
        return d
