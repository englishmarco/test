import unittest
from common.requests_api import auto_request
from common.base_api import SQL
import os
from retrying import retry


sql = SQL().select_all(table_name='testcase_cjxm')


class TestCJXM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_ZCJK(self):
        url = sql[0]['url']
        method = sql[0]['method']
        body = eval(sql[0]['body'])
        assertion = eval(sql[0]['assert'])
        result = auto_request(url=url, method=method, body=body)
        self.assertEqual(result['error_code'], assertion[0]['error_code'] or assertion[1]['error_code'])

    def test_DL(self):
        url = sql[1]['url']
        method = sql[1]['method']
        body = eval(sql[1]['body'])
        assertion = eval(sql[1]['assert'])
        result = auto_request(url=url, method=method, body=body)
        self.sign = result['login_info']['sign']
        self.assertEqual(result['error_code'], assertion['error_code'])
        return result['login_info']['sign']

    def test_TJJP(self):
        url = sql[2]['url']
        method = sql[2]['method']
        body = eval(sql[2]['body'])
        assertion = eval(sql[2]['assert'])
        file_path = os.path.dirname(os.path.dirname(__file__)) + '/template/githubB.jpg'
        open_file = open(file_path, 'rb')
        files = {'file': open_file}
        result = auto_request(url=url, method=method, body=body, files=files)
        open_file.close()
        self.assertEqual(result['msg'], assertion['msg'])

    def test_CJJK(self):
        url = sql[3]['url']
        method = sql[3]['method']
        body = eval(sql[3]['body'])
        assertion = eval(sql[3]['assert'])
        body['sign'] = TestCJXM().test_DL()
        result = auto_request(url=url, method=method, body=body)
        self.assertEqual(eval(result)['error_code'], assertion[0]['error_code'] or assertion[1]['error_code'])

    @retry(stop_max_attempt_number=3)
    def test_CKZJJL(self):
        url = sql[4]['url']
        method = sql[4]['method']
        body = eval(sql[4]['body'])
        assertion = eval(sql[4]['assert'])
        body['sign'] = TestCJXM().test_DL()
        result = auto_request(url=url, method=method, body=body)
        self.assertEqual(eval(result)['error_code'], assertion['error_code'])

    def test_HQSYJPXX(self):
        url = sql[5]['url']
        method = sql[5]['method']
        body = sql[5]['body']
        assertion = eval(sql[5]['assert'])
        result = auto_request(url=url, method=method, body=body)
        self.assertEqual(eval(result)['error_code'], assertion['error_code'])


if __name__ == '__main__':
    unittest.main()
