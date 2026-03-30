# Movie Night

Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

- `"Monday"`
- `"Tuesday"`
- `"Wednesday"`
- `"Thursday"`
- `"Friday"`
- `"Saturday"`
- `"Sunday"`

The showtime will be given in the format `"H:MMam"` or `"H:MMpm"`. For example `"10:00am"` or `"10:00pm"`.

Return the total cost in the format `"$D.CC"` using these rules:

- Weekend (Friday - Sunday): $12.00 per ticket.
- Weekday (Monday - Thursday): $10.00 per ticket.
- Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
- Tuesdays: all tickets are $5.00 each.

## 一、题解和思路

### 1.1、题解

函数接收三个参数，星期几、时间和票数，返回一场表演在特定时间的票价。

- 周末：礼拜五到礼拜天，每张票价12；
- 工作日：周一到周四，每张票价为10；
- 周二：票价为5；
- 特殊情况：在非周二的午场（5:00pm）之前，每张票价减2

### 1.2、思路

- 先判断是不是 Tuesday

- 再判断周末 or 工作日 → 确定基础价格

- 解析时间 → 判断是否是午场（< 5:00pm）

- 应用午场折扣（注意排除 Tuesday）

- 乘以票数，格式化输出

## 二、Returns

1. `get_movie_night_cost("Saturday", "10:00pm", 1)` should return `"$12.00"`.
2. `get_movie_night_cost("Sunday", "10:00am", 1)` should return `"$10.00"`.
3. `get_movie_night_cost("Tuesday", "7:20pm", 2)` should return `"$10.00"`.
4. `get_movie_night_cost("Wednesday", "5:40pm", 3)` should return `"$30.00"`.
5. `get_movie_night_cost("Monday", "11:50am", 4)` should return `"$32.00"`.
6. `get_movie_night_cost("Friday", "4:30pm", 5)` should return `"$50.00"`.
7. `get_movie_night_cost("Tuesday", "11:30am", 1)` should return `"$5.00"`.

## 三、Python Solution(s)

### 3.1、常规解法，使用if ... else

```python
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
```

关键点：用`Tuesday`覆盖规则。可以提前返回，逻辑最清晰。

### 3.2、用datetime

```python
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
```

### 3.3、用映射表

```python
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
```

## 四、JavaScript Solution(s)

### 4.1、常规解法

```js
function getMovieNightCost(day, showtime, numberOfTickets){
    // 1. 周二要覆盖所有规则
    if(day === "Tuesday"){
        return `$${(5 * numberOfTickets).toFixed(2)}`;
    }

    // 2. 基础票价
    let price;
    if(["Friday", "Saturday", "Sunday"].includes(day)){
        price = 12;
    } else {
        price = 10;
    }

    // 3. 解析时间，例如4:30
    let [hourPart, minutePart] = showtime.split(":");
    let hour = parseInt(hourPart);
    let minute = parseInt(minutePart.slice(0, 2));
    let period = minutePart.slice(2);

    // 4. 转24小时
    if(period === "pm" && hour !== 12){
        hour += 12;
    }
    if(period === "am" && hour === 12){
        hour = 0;
    }

    // 5. 午场判断
    if(hour < 17){
        price -= 2;
    }

    // 6.总价
    let total = price * numberOfTickets;

    return `$${total.toFixed(2)}`;
}
```

### 4.2、用Date解析，但是不稳

```js
function getMovieNightCostDate(day, showtime, numberOfTickets){
    // 1. 周二直接返回
    if (day === "Tuesday") {
        return `$${(5 * numberOfTickets).toFixed(2)}`;
    }

    // 2. 价格
    let price = ["Friday", "Saturday", "Sunday"].includes(day) ? 12 : 10;

    // 3. 用 Date 解析时间
    let date = new Date(`1970-01-01 ${showtime}`);

    // 4. 午场
    if (date.getHours() < 17) {
        price -= 2;
    }

    return `$${(price * numberOfTickets).toFixed(2)}`;
}
```

### 4.3、用Mapping映射

```js
function getMovieNightCostMapping(day, showtime, numberOfTickets){
    const basePrice = {
        Monday: 10,
        Tuesday: 5,
        Wednesday: 10,
        Thursday: 10,
        Friday: 12,
        Saturday: 12,
        Sunday: 12
    };

    let price = basePrice[day];

    if (day === "Tuesday") {
        return `$${(price * numberOfTickets).toFixed(2)}`;
    }

    let hour = parseInt(showtime.split(":")[0]);
    let period = showtime.slice(-2);

    if (period === "pm" && hour !== 12) hour += 12;
    if (period === "am" && hour === 12) hour = 0;

    if (hour < 17) price -= 2;

    return `$${(price * numberOfTickets).toFixed(2)}`;
}
```

