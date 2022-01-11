import pandas as pd
import os


# 路径检测
def path():
    if os.path.exists('source.csv') is False:
        csv = pd.DataFrame(columns=["题目", "答案"])
        csv.to_csv('source.csv', sep=',', index=False, encoding='gb18030')


# 写入
def write():
    number = 1
    key, value = [], []
    print("输入格式为:题目 答案,以/为分隔,停止录入使用回车")
    while number:
        try:
            a_key, b_value = str(input()).split("/")
            key.append("".join(a_key.split()))
            value.append(b_value)
            dict = {'题目': key, '答案': value}
        except:
            number -= 1
    csv = pd.read_csv('source.csv', encoding='gb18030')
    if csv.empty is True:
        data = pd.DataFrame(dict)
        data.to_csv('source.csv', sep=',', index=False, encoding='gb18030')
    else:
        data = pd.DataFrame(dict)
        data_casv = csv.append(data, ignore_index=True)
        data_casv.to_csv('source.csv', sep=',', index=False, encoding='gb18030')
    return menu()


# 搜索
def search():
    csv = pd.read_csv('source.csv', encoding='gb18030')
    print("输入题干")
    number = 1
    while number:
        txt = str(input())
        info = csv.index[csv["题目"] == "".join(txt.split())].tolist()
        info_value = csv.iloc[info]["答案"].tolist()
        print(info_value[0])
    return menu()


# 展示csv内容
def read():
    csv = pd.read_csv('source.csv', encoding='gb18030')
    print(csv)
    return menu()


# 菜单
def menu():
    print("题库搜索系统\n---------\n输入数字使用\n1.题库写入\n2.题库搜索\n3.题库展示\n4.退出系统")
    number = 1
    while number:
        num = input()
        try:
            if int(num) == 1:
                write()
            elif int(num) == 2:
                search()
            elif int(num) == 3:
                read()
            elif int(num) == 4:
                break
            else:
                print("请输入正确数字")
        except:
            print("请输入正确数字")


if __name__ == "__main__":
    path()
    menu()
