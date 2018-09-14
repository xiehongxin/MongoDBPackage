# coding: utf-8
# @author: hongxin
# @date: 9/14/18

from pymongo import MongoClient


class ModelCommonDao(object):
    def __init__(self, collection, **kwargs):
        self.host = kwargs['host']
        self.user_name = kwargs['user_name']
        self.pwd = kwargs['pwd']
        self.auth_source = kwargs['auth_source']
        self.auth_mechanism = kwargs['auth_mechanism']
        self.client = MongoClient(self.host, username=self.user_name, password=self.pwd,
                                  authSource=self.auth_source, authMechanism=self.auth_mechanism)
        self.db = self.client[kwargs['db']]
        self.model = self.db[collection]

    def check_exist(self, query_condition):
        """
        检查数据是否存在
        :param query_condition: 查询的条件, 如 {'_class': 'class1'}
        :return: True or False
        """
        check_info = self.model.find_one(query_condition)
        if check_info is None:
            return False
        else:
            return True

    def insert_data(self, data_list):
        """
        插入数据
        :param data_list:
        :return: True or False
        """
        uid = self.model.insert_many(data_list)
        uid_list = uid.inserted_ids  # 获取 _id 列表
        if len(uid_list) > 0:
            return True
        else:
            return False

    def find_one_field_all_value(self, query_field):
        """
        获取一个字段的所有取值, 比如获取所有班级的名称
        :return: None or list
        """
        if isinstance(query_field, str):
            query_condition = {query_field: 1, '_id': 0}
            # 获取该字段的所有取值（取全部数据）
            data = self.model.find({}, query_condition)
            data_list = list(data)
            # 转换为字符串列表(有可能该字段无数据, 所以要做判断)
            value_list = [list(d.values())[0] for d in data_list if len(d) > 0]  # 获取
            value_list = list(set(value_list))
            return value_list
        else:
            return None

    def find_data(self, query_condition):
        """
        根据查询条件查询对应的数据, 默认不返回'_id'这个字段
        :param query_condition:
        :return: list & dict
        """
        query_condition.update({'_id': 0})  # 默认不返回'_id' 这个字段
        data = self.model.find(query_condition)
        data = list(data)
        return data

    def modify_data(self, old_condition, new_condition):
        """
        更新时需调用check_exist检查字段是否存在
        :param old_condition:  之间的条件, 需要更新的数据
        :param new_condition:  新的条件
        :return:
        """
        modify_info = self.model.update_many(old_condition, new_condition)
        # modify_info: {'updatedExisting': True, 'nModified': 3, 'ok': 1.0, 'n': 3}
        # modify_info: {'nModified': 0, 'n': 0, 'updatedExisting': False, 'ok': 1.0}
        modify_info = modify_info.raw_result
        if modify_info['updatedExisting'] is False:
            return False
        else:
            return True

    def delete_data(self, delete_condition):
        """
        删除数据
        :param delete_condition:
        :return:
        """
        delete_info = self.model.delete_many(delete_condition)
        # delete_info: {'ok': 1.0, 'n': 0}
        delete_info = delete_info.raw_result
        if delete_info['n'] == 0:
            return False
        else:
            return True

    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    pass
