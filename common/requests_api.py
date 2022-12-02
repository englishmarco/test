import requests
from common.readConfig import WRConfigFile
from logs.logsfile import logger


conf = WRConfigFile().read_conf
url_head = conf('requests_setting', 'url_head')
if url_head == '':
    logger.warning('configfile.ini文件没有配置[requests_setting][url_head]')


@logger.catch()
def auto_request(url, method, body=None, headers=None, files=None, allow_redirects=True, timeout=5):
    """
    请求接口方法
    :param url:只需传入资源路径，无需输入域名地址
    :param method:接口去请求方法，只支持GET、POST方法
    :param body:接口请求参数，会根据方法请求参数，自动选择params或data
    :param headers:信息头
    :param files:传入文件
    :param allow_redirects:重定向
    :param timeout:超时
    :return:返回响应内容
    """
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


if __name__ == '__main__':
    params = {'stu_name': '小草'}
    auto_request(url='/api/user/stu_info', method='GET', params=params)
    auto_request(url='/index.php?s=/5&page_id=17')
    data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
    auto_request(url='/api/user/login', method='POST', data=data)











# @logger.catch()
# def auto_get(url=None, params=None, headers=None, allow_redirects=True, timeout=3):
#     all_url = str(url_head) + str(url)
#     try:
#         logger.info('开始请求接口:{all_url}', all_url=all_url)
#         get_response = requests.get(url=all_url, headers=headers, params=params, allow_redirects=allow_redirects, timeout=timeout)
#         logger.success('接口请求成功，等待返回数据。请求URL:{get_response_url}', get_response_url=get_response.url)
#     except BaseException as e:
#         logger.warning('接口请求时发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
#     else:
#         logger.success('接口请求执行成功，返回数据:{get_response}', get_response=get_response.content)
#         return get_response.text
#     finally:
#         logger.info('接口执行完毕')
#
# @logger.catch()
# def auto_post(url=None, data=None, headers=None, allow_redirects=True, timeout=3):
#     all_url = str(url_head) + str(url)
#     try:
#         logger.info('开始请求接口:{all_url}', all_url=all_url)
#         post_response = requests.post(url=all_url, headers=headers, data=data, allow_redirects=allow_redirects, timeout=timeout)
#         logger.success('接口请求成功，等待返回数据。请求URL:{post_response_url}', post_response_url=post_response.url)
#     except BaseException as e:
#         logger.warning('接口请求时发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
#     else:
#         logger.success('接口请求执行成功，返回数据:{post_response}', post_response=post_response.json())
#         return post_response.json()
#     finally:
#         logger.info('接口执行完毕')
#
#
# if __name__ == '__main__':
#     params = {'stu_name': '小黑'}
#     auto_get(url='/api/user/stu_info', params=params)
#     auto_get(url='/index.php?s=/5&page_id=17')
#     data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
#     auto_post(url='/api/user/login', data=data)
