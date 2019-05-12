"""
    作者：zqc
    版本：v4.0
    日期：12/05/2019
    功能：输入某年某月某日，判断这一天是这一年的第几天？
    2.0增加功能：用列表替换元组
    3.0增加功能：将月份划分为不同的集合再操作
    4.0增加功能：将月份及其对应天数通过字典表示
"""

import datetime

def is_leap_year(year):
    """
        判断是否为闰年
        是：返回true
        否：返回false
    """
    #这样写逻辑没问题，但是不好，
    #if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    #    return True
    #else:
    #    return False
    #改写以上代码
    #定义变量
    is_leap = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    else:
        return is_leap

def main():
    """
        主函数
    """
    #从外部输入数据，并转换为时间格式。
    input_str = input("请输入日期(yyyy/mm/dd):")
    input_date = datetime.datetime.strptime(input_str,'%Y/%m/%d')
    print(input_date)

    #获取 输入时间的 年，月，日
    year = input_date.year
    month = input_date.month
    day = input_date.day

    print(year,month,day)

    # 包含30天 月份集合,定义个初始化值
    # _30_days_month_set = {4,6,9,11}
    # _31_days_month_set = {1,3,5,7,8,10,12}

    #月份-天数  字典形式
    month_day_dict = {1:31,
                      2:28,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:30}
    #初始化值
    days = 0
    days += day
    for i in range(1,month):
        days += month_day_dict[i]

    if is_leap_year(year):
        days += 1

    #遍历月份，赋值天数
    # for i in range(1,month):
    #     if i in _30_days_month_set:
    #         days += 30
    #     elif i in _31_days_month_set:
    #         days += 31
    #     else:
    #         days += 28


    #计算之前月份天数的总和以及当前月份天数，例如今天是3月4好，就是 1月+2月+4天
    #此处不用元组，改用list(列表)
    #days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # days_in_month_list = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    # if is_leap_year(year) and month > 2:
    #     days += 1

    print("这是第{}天！".format(days))


if __name__ == '__main__':
    main()



#使用字典。