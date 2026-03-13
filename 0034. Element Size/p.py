# -*- encoding: utf-8 -*- 
# @Time: 2026/3/13 9:19
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

""" =====================================================
    *** 第一种解法：正常且清晰的常规解法
===================================================== """
def get_element_size_normal(window_size, element_vw, element_vh):
    # 1. 数据判定，要信任输入
    # 2. Parse the window_size
    window_width, window_height = window_size.split(" x ")
    window_width = int(window_width.strip())
    window_height = int(window_height.strip())

    # 3. Parse the element vw and element vh
    vw = int(element_vw.replace("vw", "").strip())
    vh = int(element_vh.replace("vh", "").strip())

    # 4. Return element
    element_width = window_width * vw // 100
    element_height = window_height * vh // 100
    print(element_width, element_height)
    return f"{element_width} x {element_height}"

# get_element_size_normal("1200 x 800", "50vw", "50vh")


def get_element_size_normal_pythonic(window_size, element_vw, element_vh):
    # 1. get the window size part
    w, h = map(int, window_size.split(" x ").strip())

    # 2. get the vw and vh int part
    vw = int(element_vw[:-2])
    vh = int(element_vh[:-2])

    return f"{w * vw // 100} x {h * vh // 100}"

""" =====================================================
    *** 第二种解法：正则提取数字
===================================================== """
import re
def get_element_size_with_re(window_size, element_vw, element_vh):
    w, h = map(int, re.findall(r"\d+", window_size))
    vw = int(re.findall(r"\d+", element_vw)[0])
    vh = int(re.findall(r"\d+", element_vh)[0])
    return f"{w * vw // 100} x {h * vh // 100}"

get_element_size_with_re("1200 x 800", "50vw", "50vh")

""" =====================================================
    *** 第三种解法：一行流
===================================================== """
def get_element_size_one(window_size, element_vw, element_vh):
    w, h = map(int, window_size.split(" x ").strip())
    return f"{w * int(element_vw[:-2])//100} x {h * int(element_vh[:-2])//100}"