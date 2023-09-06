import pymysql
from DataBase import config


class Model:
    ''' 表单信息操作类  '''

    def __init__(self, table, config=config):
        ''' 构造方法 ，显示数据库连接 信息初始化 '''
        try:
            self.tab_name = table
            self.link = pymysql.connect(
                host=config.HOST, user=config.USER, password=config.PASSWD, db=config.DBNAME, charset="utf8")
            self.cursor = self.link.cursor(pymysql.cursors.DictCursor)
            self.pk = "id"  # 表的主健字段名
            self.fields = []  # 当前表中的字段列表明
            self.__loadFields()  # 调用私有化方法初始化信息
        except Exception as err:
            print("数据库model类初始化失败", err)

    def __loadFields(self):
        '''内部私有方法，负责加载当前的主键名和其他字段信息'''
        # 查询当前表结构信息
        sql = "show columns from %s" % (self.tab_name)
        self.cursor.execute(sql)
        dlist = self.cursor.fetchall()
        # 循环表中的每个字段信息
        for v in dlist:
            # 将每个字段名都添加到属性fields中
            self.fields.append(v["Field"])
            # 判断当前字段是否是主键
            if v["Key"] == "PRI":
                self.pk = v["Field"]

    def find(self, id):
        ''' 获取指定id号的单条信息'''
        try:
            sql = "select * from %s where %s='%s'" % (
                self.tab_name, self.pk, id)
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as err:
            print("sql执行出错，原因", err)

    def findAll(self):
        ''' 获取所有信息'''
        try:
            sql = "select * from %s" % (self.tab_name)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print("sql执行出错，原因", err)

    def select(self, where=[], order=None, limit=None):
        ''' 获取所有信息'''
        try:
            sql = "select * from %s" % (self.tab_name)
            # 判断并拼装sql语句
            if isinstance(where, list) and len(where) > 0:
                sql += " where " + "  and ".join(where)
            if order is not None:  # 判断排序
                sql += " order by "+order
            if limit is not None:
                sql += " limit  "+str(limit)
            print(sql)
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as err:
            print("sql执行出错，原因", err)
            return []  # 结果异常返回空列表

    def save(self, data={}):
        ''' 添加数据方法，通过传入字典信息完成信息添加'''
        try:
           # 组织sql语句的数据处理
            keys = []
            values = []
            for k, v in data.items():
                # 判断当前字段名是否存在
                if k in self.fields:
                    keys.append(k)
                    values.append(v)
            sql = "insert into %s(%s) values(%s)" % (
                self.tab_name, ",".join(keys), ",".join(['%s']*len(values)))
            print(sql)
            self.cursor.execute(sql, tuple(values))
            self.link.commit()
            return self.cursor.lastrowid  # 返回自增的id值
        except Exception as err:
            print("sql执行出错，原因", err)
            return 0

    def update(self, data={}):
        ''' 修改数据方法，通过传入字典信息完成信息修改'''
        try:
           # 组织sql语句的数据处理
            keys = []
            values = []
            for k, v in data.items():
                # 判断当前字段名是否存在
                if (k in self.fields) and (k != self.pk):  # 主键不能修改
                    keys.append("{}=%s".format(k))
                    values.append(v)
            sql = "update  %s set %s where %s='%s'" % (
                self.tab_name, ",".join(keys), self.pk, data.get(self.pk))
            print(sql)
            self.cursor.execute(sql, tuple(values))
            self.link.commit()
            return self.cursor.lastrowid  # 返回自增的id值
        except Exception as err:
            print("sql执行出错，原因", err)
            return 0

    def delete(self, id):
        ''' 删除指定id号的单条信息'''
        ''' 获取所有信息'''
        try:
            sql = "delete from %s where %s='%s'" % (self.tab_name, self.pk, id)
            self.cursor.execute(sql)
            self.link.commit()  # 事务提交
            return self.cursor.rowcount
        except Exception as err:
            print("sql执行出错，原因", err)
            return 0

    def total(self):
        """" 获取总数据条数的方法"""
        sql = "select count(*) as num from %s" % (self.tab_name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()["num"]

    def __del__(self):
        ''' 析构方法'''
        if self.link != None:  # 数据库连接失败关闭
            self.link.close()
