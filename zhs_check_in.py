# -*- coding: UTF-8 -*-
"""
__Author__ = "MakiNaruto"
__Version__ = "2.1.0"
__Description__ = ""
__Created__ = 2022/2/14 10:37 下午
"""
import json
import time
import traceback
from functools import partial

import requests
from requests import session

from zhs_cookie import get_cookies

print = partial(print, flush=True)


class ZhsCheckIn():
    def __init__(self):
        # 登录信息
        self.login_cookies = []
        self.session = session()
        # 请求头
        self.headers = {
            'authority': 'zhs.tw',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'content-length': '0',
            # 'cookie': 'PHPSESSID=ton2i0ei5ud30pdeqvtj29ppa9; twk_idm_key=W9imhDG4BvxV8XVN5nf_e; uid=63473; email=2854859592%40qq.com; key=b15157ed89e4637c21339efe6f55999ba02a7a14c4099; ip=1552cb662e07cebdfb4884a253184997; expire_in=1711612169; _gid=GA1.2.975399882.1711379217; _gat_gtag_UA_97496666_2=1; _ga_Z5T89XQJSH=GS1.1.1711379216.25.1.1711379221.55.0.0; _ga=GA1.1.636293395.1702545016; cf_clearance=rNJWttNgRh.S0RzI1DcSNLbh7cKlqEm4Kfv103zhb.4-1711379222-1.0.1.1-Xc9y7NKLB3fzm6raR7D_06z5ACoEcuZDErQ0zuhbz2RptYE.B1EZv1ztXmWX0_Z0nDD1tCjq8ldgvn8V7.cBVw; TawkConnectionTime=0; twk_uuid_6558617991e5c13bb5b1369c=%7B%22uuid%22%3A%221.MSGqDfn8BRUakcRt0l28HtFABtjeAdzHsGFawPf7d1Pxu9pKdkJWntUzp3C8LNfDcVAVcRkc1Ia4lVqosdwlFWAU4mQJRmkFoAjhx1fnG42sa%22%2C%22version%22%3A3%2C%22domain%22%3A%22zhs.tw%22%2C%22ts%22%3A1711379224835%7D',
            'origin': 'https://zhs.tw',
            'referer': 'https://zhs.tw/user',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        }

    def check_in(self):
        """ 签到 """
        self.login_cookies = get_cookies()
        res = []
        for i in range(len(self.login_cookies)):
            cookie = self.login_cookies[i]
            r = self.do_check_in(cookie)
            res.append(r)
        return res

    def do_check_in(self, cookie) -> bool:
        response = requests.post('https://zhs.tw/user/checkin',
                                 headers=self.headers,
                                 cookies=cookie)
        print("response:", response.text)
        if response.status_code != 200:
            return False
        response_result = json.loads(response.text)
        if 1 == response_result['ret']:
            return True
        return False


if __name__ == '__main__':
    a = ZhsCheckIn()
    try:
        res = a.check_in()
        success = filter(lambda x: x is True, res)
        print(f"====================共{len(list(success))}个ZHS账号签到成功=========\n")
        print(
            f"==================脚本执行- 北京时间(UTC+8)：{time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())}=====================\n")
    except Exception as e:
        print(f"===================ZHS账号签到异常===================")
        print(traceback.print_exc())
