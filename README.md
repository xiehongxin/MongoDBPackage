#### MongoDB数据库的操作封装

环境： Centos7.4 + MongoDB4.0.0 + PyMongo

背景： 最近mongodb越来越火, 但是合适的框架并不算多, 目前所了解的只有pymongo, mongokit 及 mongoengine 这三个。
pymongo：语法跟mongodb官网的差不多，比较容易上手，数据库的集合包含的字段需要在注释或者其它文档说明，随意性大了点
mongokit：orm 框架, 但粗略看了一下, mongokit只是对pymongo加了一层封装，用起来不一定爽
mongoengine：orm框架 , 但 mongoengine 的orm模型比较难以理解，不易上手

综合考虑，自己对pymongo进行封装。

目录说明：
 - model.model_class： mongodb的数据库模型
 - model_dao.model_common_dao: mongodb 的数据库操作封装基类/父类
 - model_dao.model_class_dao: mongodb 的数据库操作封装
 - app: mongodb数据库操作测试
 - config： 数据库配置文件

