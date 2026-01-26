# -*- encoding: utf-8 -*- 
# @Time: 2026/1/26 13:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from typing import Union
from numbers import Real
import re

def scale_image(size: str, scale: Real) -> str:

    # 如果是3.10后的版本应该是
    # def scale_image(size: str, scale: int | float) -> str:
    """ 注释 #=============================================
    		*** 传入图片的尺寸和scale，返回scale后的尺寸
    			- 1. size类似： "1200x720"
    			- 2. scale 可以是整数也可以是 浮点数
    			- 3. 如果是scale是2，需要返回 "2400x1440*
    			- 4. Real包含了int，float，Decimal，Fraction
    	  ============================================= # """
    return "x".join(str(int(int(_) * scale)) for _ in size.split("x"))

print(scale_image('800x600', 2))
