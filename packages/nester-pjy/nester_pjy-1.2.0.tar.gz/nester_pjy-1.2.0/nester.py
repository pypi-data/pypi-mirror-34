# -*- coding: cp936 -*-
"""
���ǵ���ģ��
"""


def print_lol(the_list):
    """
    �����������Ե���
    :param the_list: 
    :return: null
    """
    for each_list in the_list:
        if isinstance(each_list,list) :
            print_lol(each_list)
        else :
            print(each_list)
