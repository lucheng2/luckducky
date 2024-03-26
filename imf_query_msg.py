import json

import requests

url = "http://172.30.0.14:7484/ImfConsole/getMsgContent.action"
payload_prefix = "dto.msgid="
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'JSESSIONID=BD764FFB4FB795E93F3E14C90660FDCB',
    'Origin': 'http://172.30.0.14:7484',
    'Referer': 'http://172.30.0.14:7484/ImfConsole/jsp/logquery/logquery-dynmsgtrace.jsp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
msg_input_file = 'msg_input.json'
reg_no = ''


def run():
    msg_ids = get_msg_id_list()
    msg_contents = []
    for i in msg_ids:
        ret = do_query(i)
        if msg_filter(ret) is True:
            msg_contents.append(ret)
    with open('mst_output.json', 'w', encoding='utf-8') as fr:
        json.dump(msg_contents, fr)


def msg_filter(msg_content: str) -> bool:
    if reg_no is not None and len(reg_no) > 0:
        return msg_content.__contains__(reg_no)
    return True


def do_query(msg_id):
    response = requests.request("POST", url, headers=headers, data=payload_prefix + msg_id)
    return response.text


def get_msg_id_list():
    content = load_file()
    root = content['root']
    msg_ids = []
    for i in root:
        msg_ids.append(i['msgid'])
    return msg_ids


def load_file():
    """ 读取报名的配置信息 """
    try:
        with open(msg_input_file, 'r', encoding='utf-8') as fr:
            config = json.load(fr)
        return config
    except Exception as e:
        print('-' * 10, '加载配置信息失败', '-' * 10)
        print(e)


run()
