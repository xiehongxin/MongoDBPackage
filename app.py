# coding: utf-8
# @author: hongxin
# @date: 9/14/18

"""
实现内容： 年级学生成绩管理
一个年级有多个班级，一个班级有多个学生，每个学生有姓名，年龄，性别，学号，所属班级等信息

详细需求
1. 查询所有班级
2. 添加学生信息
3. 修改学生信息
4. 删除学生信息
5. 查询学生信息

"""

from model.model_class import ModelClass
from config import mongodb_config
from model_dao.model_class_dao import ModelClassDao

# 实例化一个类
mcd = ModelClassDao('stu_info', **mongodb_config)


def generate_query_condition():
    """
    生成查询条件的函数
    :return:
    """
    pass


def insert_data_test():
    std_data = []
    for i in range(4):
        std_data.append({ModelClass.name: 'aa'+str(i), ModelClass.age: 18+i, ModelClass.sex: 1,
                         ModelClass.class_: 'class1', ModelClass.stu_num: '2015160'+str(i)})
    print(mcd.insert_data(std_data))


def check_exist_test():
    print(mcd.check_exist({ModelClass.class_: 'class1', ModelClass.stu_num: '20151601'}))
    print(mcd.check_exist({ModelClass.class_: 'class2'}))
    print(mcd.check_exist({ModelClass.class_: 'class1'}))


def find_all_class_test():
    print(mcd.find_one_field_all_value(ModelClass.class_))


def modify_data_test():
    print(mcd.modify_data({ModelClass.class_: 'class2'}, {'$set': {ModelClass.class_: 'class1'}}))


def delete_data_test():
    print(mcd.delete_data({ModelClass.stu_num: '20151601'}))
