"""
    作者：zqc
    版本：v1.0
    日期：24/04/2019
    功能：输入某年某月某日，判断这一天是这一年的第几天？
"""

import datetime

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

    #计算之前月份天数的总和以及当前月份天数，例如今天是3月4好，就是 1月+2月+4天
    days_in_month_tup = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    #print(days_in_month_tup[:month-1])
    days = sum(days_in_month_tup[:month-1]) + day


    #判断闰年，和当前是第几天
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        if month > 2:
            days = days +1

    print("这是第{}天！".format(days))


if __name__ == '__main__':
    main()



#下一课，使用列表替代元组。