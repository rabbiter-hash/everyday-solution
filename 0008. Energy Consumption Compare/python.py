# -*- encoding: utf-8 -*- 
# @Time: 2026/1/20 9:19
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def energy_consumption_compare(calories_burned, watt_hours_used):
    """
    :param calories_burned: 运动、锻炼过程中消耗的卡路里
    :param watt_hours_used: 该次运动、锻炼过程中电子设备消耗的电能量
    :return: str
    """
    if(calories_burned < 0 or watt_hours_used < 0):
        raise ValueError('Energy consumption must be postive!')

    workout_energy_joules = calories_burned * 4184
    device_energy_joules = watt_hours_used * 3600

    return (
        'Workout' if workout_energy_joules > device_energy_joules else
        'Devices' if workout_energy_joules < device_energy_joules else
        'Equal'
    )