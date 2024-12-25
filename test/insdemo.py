# -*- encoding: utf-8 -*-
"""
    @File : insdemo.py \n
    @Contact : yafei.wang@pisemi.com \n
    @License: (C)Copyright {} \n
    @Modify Time: 2023/11/23 10:25 \n
    @Author : Pisemi Yafei Wang \n
    @Version: 1.0 \n
    @Description : None \n
    @Create Time: 2023/11/23 10:25 \n
"""
import pyvisa
from piinspy import *

if __name__ == '__main__':

    rm = pyvisa.ResourceManager()
    # dmm = PiIns(rm, "DMM", "9060", "USB0::0x2184::0x0059::GEW912422::INSTR")
    pi_power_list, pi_dmm_list, pi_smu_list, pi_Load_list = ins_scan(rm)
    if pi_power_list is not None:
        for i in pi_power_list:
            print(i)
    else:
        del pi_power_list
    if pi_dmm_list is not None:
        for i in pi_dmm_list:
            print(i)
            if i.pInsName == "34461":
                print(i.dmm_ins_read())
    else:
        del pi_dmm_list
    if pi_smu_list is not None:
        for i in pi_smu_list:
            print(i)
    else:
        del pi_smu_list
    if pi_Load_list is not None:
        for i in pi_Load_list:
            print(i)
    else:
        del pi_Load_list
