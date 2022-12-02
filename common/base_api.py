import pymysql
from common.readConfig import WRConfigFile
from logs.logsfile import logger


class SQL(object):
    @logger.catch()
    def __init__(self):
        conf = WRConfigFile().read_conf
        host = conf('database', 'host')
        user = conf('database', 'user')
        password = conf('database', 'password')
        base_name = conf('database', 'base_name')
        try:
            logger.info('正在连接数据库,数据库地址={host},用户名={user},数据库密码={password},数据库名称={base_name}',
                        host=host, user=user, password=password, base_name=base_name)
            self.connection = pymysql.connect(
                host='192.168.1.163',
                user='root',
                password='root',
                database='guest',
                cursorclass=pymysql.cursors.DictCursor
            )
        except BaseException as e:
            logger.warning('数据库连接时发生异常:{e}', e=e)
        else:
            logger.success('连接数据库成功')
        self.cursor = None

    def creat_connect(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_base(self):
        self.connection.close()
        logger.success('关闭数据库成功')

    @logger.catch()
    def select_one(self, table_name=None, field_name=None, value_name=None):
        cursors = self.creat_connect()
        sql = 'select * from %s where %s = "%s"' % (table_name, field_name, value_name)
        try:
            cursors.execute(sql)
            logger.success('执行查询SQL语句:{sql}', sql=sql)
        except BaseException as e:
            logger.warning('SQL语句执行异常，请检查SQL语句:{sql},异常:{e}', sql=sql, e=e)
        else:
            result = cursors.fetchall()
            logger.success('数据库返回查询数据:{result}', result=result)
            return result
        finally:
            cursors.close()
            self.close_base()

    @logger.catch()
    def select_all(self, table_name=None):
        cursors = self.creat_connect()
        sql = 'select * from %s' % table_name
        try:
            cursors.execute(sql)
            logger.success('执行查询SQL语句:{sql}', sql=sql)
        except BaseException as e:
            logger.warning('SQL语句执行异常，请检查SQL语句:{sql},异常:{e}', sql=sql, e=e)
        else:
            all_result = cursors.fetchall()
            logger.success('数据库返回查询数据:{all_result}', all_result=all_result)
            return all_result
        finally:
            cursors.close()
            self.close_base()


if __name__ == '__main__':
    SQL().select_one(table_name='testcase_cjxm', field_name='case_id', value_name='1')
    SQL().select_one()
    SQL().select_all(table_name="testcase_cjxm")
