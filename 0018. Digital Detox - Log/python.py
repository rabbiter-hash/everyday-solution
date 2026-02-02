# -*- encoding: utf-8 -*- 
# @Time: 2026/2/2 8:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from datetime import datetime, timedelta

def digital_detox(logs: list) -> bool:
    # 1. 判定是否数组
    if not isinstance(logs, list):
        raise TypeError('logs is not a list')

    # 2. 转换成时间对象
    times = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
    print(id(times))
    # 排序时间对象
    times.sort()
    # print(times)
    print(id(times))

    # 3. 空字典，用于统计键值对
    day_count = {}
    four_hours = timedelta(hours=4) # 这里一定要输入hours=4，不然会是days=4

    # 4. 遍历时间对象数组
    for i, t in enumerate(times):
        # 对排序后的时间对象，比较两个相邻时间
        if(i > 0) and t - times[i-1] < four_hours:
            return False

        # 日期对象
        day = t.date()
        print(day)
        # 字典day_count初始是没有键值对的，所以应该使用get(day, 0)
        # +1的意思是，如果该day_count有了键后，就给它的值+1
        day_count[day] = day_count.get(day, 0) + 1
        if day_count[day] > 2:
            return False
    return True


digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
