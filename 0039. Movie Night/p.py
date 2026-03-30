""" =====================================================
    *** 第一种解法：循环遍历
===================================================== """
def get_movie_night_cost(day, showtime, number_of_tickets):
    # 1. 周二特殊处理
    if day == "Tuesday":
        total = 5 * number_of_tickets
        return f"${total:.2f}"

    # 2. 判断基础票价
    if day in ["Friday", "Saturday", "Sunday"]:
        price = 12
    else:
        price = 10

    # 3. 解析时间
    # 例如4：30pm
    hour = int(showtime.split(":")[0])
    minute_part = showtime.split(":")[1]
    minute = minute_part[:2]
    period = minute_part[2:] # am pm

    # 4. 转换成24小时
    if period == "pm" and hour != 12:
        hour += 12

    if period == "am" and hour == 12:
        hour = 0

    # 5. 判断是否为午场
    if hour < 17:
        price -= 2

    # 6. 计算总价
    total = price * number_of_tickets

    return f"${total:.2f}"

""" =====================================================
    *** 第二种解法：用datetime
===================================================== """
def get_movie_night_datetime(day, showtime, number_of_tickets):
    from datetime import datetime
    # 1. 周二优先
    if day == "Tuesday":
        total = f"${5 * number_of_tickets:.2f}"

    # 2. 基础票价
    price = 12 if day in ["Friday", "Saturday", "Sunday"] else 10

    # 3. 用datetime解析时间
    t = datetime.strptime(showtime, "$I:%M%p")

    # 4. 午场判断
    if t.hour < 17:
        price -= 2

    return f"${price * number_of_tickets:.2f}"

""" =====================================================
    *** 第三种解法：用映射表
===================================================== """
def get_movie_night_mapping(day, showtime, number_of_tickets):
    # 1. 基础价格，映射表
    base_price = {
        "Monday": 10,
        "Tuesday": 5,
        "Wednesday": 10,
        "Thursday": 10,
        "Friday": 12,
        "Saturday": 12,
        "Sunday": 12
    }

    # 2. 定义每一天的价格
    price = base_price[day]

    # 3. 周二直接返回
    if day == "Tuesday":
        return f"${price * number_of_tickets:.2f}"
    # 4. 时间解析
    hour = int(showtime.split(":")[0])
    period = showtime[-2:]

    # 5. 判定价格
    if period == "pm" and hour != 12:
        hour += 12
    if period == "am" and hour == 12:
        hour = 0

    # 6. 午场
    if hour < 17:
        price -= 2

    return f"${price * number_of_tickets:.2f}"