import os
import requests
import json
import time

def main():
    send_url = os.environ["send_url"]
    send_key = os.environ["send_key"]
    tian_api_key = os.environ["tian_api_key"]

    good_ninght_url = "http://api.tianapi.com/txapi/wanan/index?key=" + tian_api_key

    res_str = requests.request("GET", good_ninght_url, headers="", data="").text

    now = time.strftime("%H点%M分", time.localtime())

    msg = "现在时间" + now + "  不早了，准备休息吧！\n\n" + eval(res_str).get("newslist")[0].get("content")

    data = {
        "sendkey": send_key,
        "msg_type": "text",
        "msg": msg
    }

    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", send_url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()
