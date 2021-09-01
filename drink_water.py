import os
import requests
import json
from datetime import datetime, timedelta, timezone

def main():
    send_url = os.environ["send_url"]
    send_key = os.environ["send_key"]

    is_holiday_url = "http://timor.tech/api/holiday/info/"

    holiday_str = requests.request("GET", is_holiday_url, headers="", data="").text

    holiday_flag = json.loads(holiday_str).get("type").get("type")

    now = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime("%H点%M分")

    title = "[ 久坐提醒 ]"

    content = "现在时间" + now + "，摸鱼时间到!  你已经坐下很久了，不要忘记喝水哦。起来走几步，划划水，摸摸鱼，再继续工作吧～"

    msg = title + "\n\n" + content

    data = {
        "sendkey": send_key,
        "msg_type": "text",
        "msg": msg
    }

    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }

    if holiday_flag == 0 or holiday_flag == 3:
        response = requests.request("POST", send_url, headers=headers, data=payload)
        print(response.text)
    else:
        print("今天不是工作日，不发送提醒")


if __name__ == '__main__':
    main()
