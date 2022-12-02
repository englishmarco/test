# auto_api
# 接口自动化全篇

本篇已同步到 **[csdn博客](https://blog.csdn.net/qq_42795860)**

-------------------
### 整体思路

### 1、连接mysql数据库、封装数据库方法

### 2、封装requests方法

### 3、使用unittest框架编写接口测试用例

   - 调用封装的数据库方法取数据库数据
   - 数据传入requests封装方法中
   - 断言：响应数据是否和存在数据库中的断言字段一致，判断用例是否通过依据

### 4、执行用例

### 5、HtmlTestRunner_PY模块生成测试报告

### 6、准备数据（接口自动化前）、清理数据（接口自动化后）

-------------------

# 文件目录

- **commnon文件夹**：公共使用的类
    - **base_api.py**：连接数据库，读取数据库表数据
	- **readConfig.py**：读写configfile.ini文件配置信息
	> **注意**：**读写操作时需分开进行**，不能用同一个实例，否则会重复写入之前配置文件中存在的内容。
	- **requests_api.py**：增加auto_request，更适用项目
	- **testcase.sql**：数据库脚本，附带了点数据
- **logs文件夹**：存放日志系统和项目日志
	- **logsfile.py**：配置日志存放目录和日志相关信息
- **report文件夹**：测试报告放置在这里
- **template文件夹**：存放用例中用到的文件或图片
- **HtmlTestRunner_PY文件夹**：放置测试报告类
- **testcase文件夹**：测试用例文件存放
- **configfile.ini**：项目相关配置文件 
- **run.py**：程序运行主文件，运行main函数

# 数据库表结构

|case_id  |case_num   |title     |url        |method    |body   |headers|assert|status  |token      |
|:-------:|:---------:|:--------:|:---------:|:--------:|:-----:|:-----:|:----:|:------:|:---------:|
|测试用例ID|测试用例编号|测试用例标题|接口资源地址|接口请求方法|接口参数|请求头  |断言  |接口状态码|存放cookies|

## requests_api.py

`@logger.catch()`：捕获运行中的异常写入error日志文件  

`auto_request()`：需要传入url、method、body，函数会根据method方法判断接口请求方式  
> **注意：**`url`根据配置文件主机地址加上资源路径，所以`auto_request()`函数**url只需传入资源路径**  


``` python 
@logger.catch()
def auto_request(url, method, body=None, headers=None, files=None, allow_redirects=True, timeout=5):
    all_url = str(url_head) + str(url)
    global get_response
    global post_response
    try:
        logger.info('开始请求接口:{all_url}', all_url=all_url)
        if method == 'GET':
            get_response = requests.get(url=all_url, headers=headers, params=body, files=files, allow_redirects=allow_redirects, timeout=timeout)
            logger.success('接口请求成功，等待返回数据。请求URL:{get_response_url}', get_response_url=get_response.url)
        elif method == 'POST':
            post_response = requests.post(url=all_url, headers=headers, data=body, files=files, allow_redirects=allow_redirects, timeout=timeout)
            logger.success('接口请求成功，等待返回数据。请求URL:{post_response_url}', post_response_url=post_response.url)
        else:
            logger.warning('接口method方法错误,请检查后重试')
            raise Exception('接口请求方法错误,暂无' + str(method) + '方法')
    except BaseException as e:
        logger.error('接口请求时发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
    else:
        if method == 'GET':
            logger.success('接口请求执行成功，返回数据成功')
            # logger.success('接口请求执行成功，返回数据:{get_response}', get_response=get_response.content)
            return get_response.text
        elif method == 'POST':
            logger.success('接口请求执行成功，返回数据成功')
            # logger.success('接口请求执行成功，返回数据:{post_response}', post_response=post_response.json())
            return post_response.json()
    finally:
        logger.info('接口执行完毕')
```

## base_api.py代码片段

`select_one()`：需要传入表名、字段、值，函数会返回在数据库查询到的数据  
`select_all()`：传入表名，函数会返回在数据库表的所有数据  

``` python 
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
```

## logsfile.py代码片段

`debug_logs_path`：传入日志路径  
`filter`：设置日志等级  
`enqueue`：支持异步写入  
`rotation`：每天0点日志写入新文件  
`retention`：日志保留时间

```python 
logger.add(debug_logs_path,
           filter=lambda x: x['level'].name == 'DEBUG',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
```

## testcase/test_CJXM.py

用例模板：  
从数据库取数据  
取出的数据传入auto_request  
断言响应数据和断言是否一致  

> 注意：数据库取出来的断言数据类型是否和响应数据类型一致，否则会断言失败  

```python 
sql = SQL().select_all(table_name='testcase_cjxm')
def test_ZCJK(self):
    url = sql[0]['url']
    method = sql[0]['method']
    body = eval(sql[0]['body'])
    assertion = eval(sql[0]['assert'])
    result = auto_request(url=url, method=method, body=body)
    self.assertEqual(result['error_code'], assertion[0]['error_code'] or assertion[1]['error_code'])
```

## run.py

`output`：测试报告存放路径  
`stream`：测试报告文件流  
`report_title`：测试报告标题  
`descriptions`：测试报告描述

``` python 
if __name__ == '__main__':
    one_file_path = report_path + '\\' + file_name
    fp = open(one_file_path, 'a', encoding='utf-8')
    one_run = HTMLTestRunner(output=report_path, stream=fp, report_title='测试报告', descriptions='用例执行情况')
    one_run.run(one_test_case)
    fp.close()
```

-------------------
# 使用说明

- 需要python基础  
- 能基本使用`unittest`框架
- 安装了 **[mysql数据库](https://dev.mysql.com/downloads/mysql/)** ，能基本操作数据库数据  

### 1、数据库运行common/testcase.sql脚本  
### 2、在testcase文件夹添加py文件，编写测试用例脚本
   - 编写unittest基本框架内容  
   - 导入common/base_api.py  
   - 导入common/requests_api.py  
   - 编写用例方法，使用`select_one()`、`select_all()`方法查询数据库数据，请求`auto_request()`传入数据库查询的数据
### 3、运行run.py文件  
### 4、report目录下查看测试报告
-------------------