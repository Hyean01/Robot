#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
from frienddata import *
import traceback


def show_list():
    for n in names:
        print(f"{n[0]} {n[1]}")


def show_person(name):
    print(f"您要查找的用户信息是： {name}")
    show_record(name[0])


def find_name(name):
    # 根据输入的名字，查询是否在当前列表中，如果在，返回
    if name.isdigit():
        find_name_byId(name)
    else:
        fname = [n for n in names if n[1] == name]
        if len(fname) == 0:
            print(f"系统不存在您要查找的用户，请检查输入或与用户确认是否已注册。")
        elif len(fname) == 1:
            show_person(fname[0])
        else:
            for n in fname:
                print(f"{n[0]}. {n[1]}")

            conf = True
            while conf:
                num = int(input(f"请输入名单中{fname}的一个序号，查看相关用户的具体记录： "))
                fname_id = [x[0] for x in fname]
                if int(num) not in fname_id:
                    print("您输入的用户序号不在上述名称中， 为您找到该用户的信息如下：")
                    find_name_byId(num)
                else:
                    find_name_byId(num)
                conf = input(f"如果还想继续查看用户记录，请输入yes；输入其他将不再继续查看用户记录： ")
                if conf != 'yes':
                    conf = False


def find_name_byId(num):
    """根据输入数字，判断是否存在该用户，如果存在，进而查出该用户信息"""
    try:
        num = int(num)
        if num not in range(1, len(names)):
            print(f"系统不存在您要查找的用户，请检查输入或与用户确认是否已注册。")
        else:
            useinfo = (num, dict(names)[num])
            show_person(useinfo)
    except:
        print("Value Error")


def show_record(id):
    personal_records = [r for r in records if r[2][0] == id]
    if personal_records:
        for r in personal_records:
            print(f"{r[0][1]}（No.{r[0][0]}） {r[1]} {r[2][1]}, {r[-1]}")
    else:
        print(f"暂无此用户的行为记录。")


def show_all_records():
    for r in records:
        print(f"{r[0][1]}(No.{r[0][0]}) {r[1]} {r[2][1]}（No.{r[2][0]}）, {r[-1]}")


if __name__ == '__main__':
    # show_all_records()
    print(random.sample.__doc__)
