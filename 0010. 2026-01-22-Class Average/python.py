# -*- encoding: utf-8 -*- 
# @Time: 2026/1/22 17:13
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_average_grade(scores):
    """ 注释 #=============================================
            *** 平均分计算
                scores：列表
          ============================================= # """
    # 1. 不是列表直接返回
    if (not isinstance(scores, list)) or (len(scores) <= 1):
        print('不符合条件！')
        return

    # 2. python中计算列表总和有sum函数
    total = sum(scores)
    average = total / len(scores)

    # 3. 条件判断
    if(average >=97):
        return "A+"
    elif(average >=93):
        return "A"
    elif(average >=90):
        return "A-"
    elif(average >=87):
        return "B+"
    elif(average >=83):
        return "B"
    elif(average >=80):
        return "B-"
    elif(average >=77):
        return "C+"
    elif(average >=73):
        return "C"
    elif(average >=70):
        return "C-"
    elif(average >=67):
        return "D+"
    elif(average >=63):
        return "D"
    elif(average >=60):
        return "D-"
    else:
        return "F"

def get_average_score_map(scores):
    """ 注释 #=============================================
                *** 平均分计算
                    使用伪map映射
              ============================================= # """
    # 1. 不是列表直接退出
    if not isinstance(scores, list) or len(scores) <= 1:
        print('不符合条件！')
        return

    # 2. 平均分
    average_score = sum(scores) / len(scores)

    # 3. 映射map
    grade_map = [
        (97, "A+"), (93, "A"), (90, "A-"),
        (87, "B+"), (83, "B"), (80, "B-"),
        (77, "C+"), (73, "C"), (70, "C-"),
        (67, "D+"), (63, "D"), (60, "D-"),
        (0, "F")
    ]

    # 4. 遍历
    for score_threshold, grade in grade_map:
        if average_score >= score_threshold:
            return grade
