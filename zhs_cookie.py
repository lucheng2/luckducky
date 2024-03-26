#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/7/6 23:00
# @Author  : HarbourJ
# @TG      : https://t.me/HarbourToulu
# @File    : jdCookie.py

import os
import time
from functools import partial

print = partial(print, flush=True)


def get_cookies():
    cookie_zhs = []
    if os.environ.get("ZHS_COOKIE"):
        print("已获取并使用Env环境 Cookie")
        if '&' in os.environ["ZHS_COOKIE"]:
            cookie_zhs = os.environ["ZHS_COOKIE"].split('&')
        elif '\n' in os.environ["ZHS_COOKIE"]:
            cookie_zhs = os.environ["ZHS_COOKIE"].split('\n')
        else:
            cookie_zhs = [os.environ["ZHS_COOKIE"]]
        # return cookie_zhs
    else:
        if os.path.exists("ZHS_COOKIE.txt"):
            with open("ZHS_COOKIE.txt", 'r') as f:
                zhs_cookies = f.read().strip()
                if zhs_cookies:
                    if '&' in zhs_cookies:
                        cookie_zhs = zhs_cookies.split('&')
                    elif '\n' in zhs_cookies:
                        cookie_zhs = zhs_cookies.split('\n')
                    else:
                        cookie_zhs = [zhs_cookies]

                    # return cookie_zhs
        else:
            print("未获取到正确✅格式的ZHS账号Cookie")
            return None
    cookie_zhs = split(cookie_zhs)
    print(f"====================共{len(cookie_zhs)}个ZHS账号Cookie=========\n")
    print(
        f"==================脚本执行- 北京时间(UTC+8)：{time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())}=====================\n")
    return cookie_zhs


def split(cookie_str_list: list):
    ans = []
    for cookie_str in cookie_str_list:
        cookies = {}
        items = cookie_str.split(';')
        for i in items:
            cookie = deal_cookie(i.strip())
            cookies.update(cookie)
        ans.append(cookies)
    return ans


def deal_cookie(cookie_str: str):
    item = cookie_str.split('=')
    cookie = {item[0]: item[1]}
    return cookie

# a=deal_cookie("PHPSESSID=ton2i0ei5ud30pdeqvtj29ppa9")
# print(a)

# b=split(["PHPSESSID=ton2i0ei5ud30pdeqvtj29ppa9; twk_idm_key=W9imhDG4BvxV8XVN5nf_e; uid=63473; email=2854859592%40qq.com; key=b15157ed89e4637c21339efe6f55999ba02a7a14c4099; ip=1552cb662e07cebdfb4884a253184997; expire_in=1711612169; _gid=GA1.2.975399882.1711379217; _gat_gtag_UA_97496666_2=1; _ga_Z5T89XQJSH=GS1.1.1711379216.25.1.1711379221.55.0.0; _ga=GA1.1.636293395.1702545016; cf_clearance=rNJWttNgRh.S0RzI1DcSNLbh7cKlqEm4Kfv103zhb.4-1711379222-1.0.1.1-Xc9y7NKLB3fzm6raR7D_06z5ACoEcuZDErQ0zuhbz2RptYE.B1EZv1ztXmWX0_Z0nDD1tCjq8ldgvn8V7.cBVw; TawkConnectionTime=0; twk_uuid_6558617991e5c13bb5b1369c=%7B%22uuid%22%3A%221.MSGqDfn8BRUakcRt0l28HtFABtjeAdzHsGFawPf7d1Pxu9pKdkJWntUzp3C8LNfDcVAVcRkc1Ia4lVqosdwlFWAU4mQJRmkFoAjhx1fnG42sa%22%2C%22version%22%3A3%2C%22domain%22%3A%22zhs.tw%22%2C%22ts%22%3A1711379224835%7D"])
# print(b)
