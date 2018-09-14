#### MongoDB数据库的操作封装

**环境：** Centos7.4 + MongoDB4.0.0 + PyMongo

**背景： **
最近mongodb越来越火, 但是合适的框架并不算多, 目前所了解的只有pymongo, mongokit 及 mongoengine 这三个。

mongokit：orm 框架, 但粗略看了一下, mongokit只是对pymongo加了一层封装。

mongoengine：orm框架 , 但 mongoengine 的orm模型比较难以理解，不易上手，遂放弃。

pymongo：语法跟mongodb官网的差不多，比较容易上手，随意性比较大


综合考虑，自己对pymongo进行封装。
1.将字段映射为类, 第一使人一目了然；第二是便于修改
2.将数据库基本操作抽象出来，便于继承复用

**目录说明：**
 - model.model_class： mongodb的数据库模型
 - model_dao.model_common_dao: mongodb 的数据库操作封装基类/父类
 - model_dao.model_class_dao: mongodb 的数据库操作封装
 - app: mongodb数据库操作测试
 - config： 数据库配置文件

