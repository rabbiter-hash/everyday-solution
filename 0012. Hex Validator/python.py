# -*- encoding: utf-8 -*- 
# @Time: 2026/1/23 15:17
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)
import re
def is_valid_hex(s):
    """
    Checks if a string is a valid CSS HEX Color. It must like below:
        1. #332;
        2. #123abc;
    :param s:
    :return: true if the string is a valid hexadecimal string, false otherwise
    """
    # 1. 判定是否是合法的字符串
    if not isinstance(s, str):
        return "Not a hexadecimal string"

    # 2. 用正则判定，以#开头，中间是0-9a-f和A-F
    pattern = re.compile("^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
    return bool(pattern.match(s))

def is_valid_hex_color(s):
    """
    Checks if a string is a valid hexadecimal color. It must like below:
    :param s:
    :return: bool
    """
    return isinstance(s, str) and bool(
        re.fullmatch(r"^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$", s)
    )
if __name__ == "__main__":
    print(is_valid_hex_color("#331"))