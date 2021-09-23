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

    current_date = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    now = current_date.strftime("%-m月%-d日")

    # 下一个节假日时间
    next_holiday_url = "https://timor.tech/api/holiday/next/?type=N&week=Y"
    next_holiday_str = requests.request("GET", next_holiday_url, headers="", data="").text
    next_1_holiday_date_str = json.loads(next_holiday_str).get("holiday").get("date")  # 下一个节假日的日期
    next_1_holiday_date = datetime.strptime(next_1_holiday_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    next_1_holiday_name = json.loads(next_holiday_str).get("holiday").get("name").replace("六", "末")  # 下一个节假日名字
    day_1s = (next_1_holiday_date - current_date).days  # 下一个节假日还有多少天

    next_work_url = f"http://timor.tech/api/holiday/workday/next/{next_1_holiday_date_str}"
    next_work_str = requests.request("GET", next_work_url, headers="", data="").text
    next_work_data = json.loads(next_work_str).get("workday").get("date")

    # 第2个节假日时间
    next_holiday_url = f"""https://timor.tech/api/holiday/next/{next_work_data}?type=N&week=N"""
    next_holiday_str = requests.request("GET", next_holiday_url, headers="", data="").text
    next_2_holiday_date_str = json.loads(next_holiday_str).get("holiday").get("date")  # 第2个节假日的日期
    next_2_holiday_date = datetime.strptime(next_2_holiday_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    next_2_holiday_name = json.loads(next_holiday_str).get("holiday").get("name")  # 第2个节假日名字
    day_2s = (next_2_holiday_date - current_date).days  # 第2个节假日还有多少天

    next_work_url = f"http://timor.tech/api/holiday/workday/next/{next_2_holiday_date_str}"
    next_work_str = requests.request("GET", next_work_url, headers="", data="").text
    next_work_data = json.loads(next_work_str).get("workday").get("date")

    # 第3个节假日时间
    next_holiday_url = f"""https://timor.tech/api/holiday/next/{next_work_data}?type=N&week=N"""
    next_holiday_str = requests.request("GET", next_holiday_url, headers="", data="").text
    next_3_holiday_date_str = json.loads(next_holiday_str).get("holiday").get("date")  # 第3个节假日的日期
    next_3_holiday_date = datetime.strptime(next_3_holiday_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    next_3_holiday_name = json.loads(next_holiday_str).get("holiday").get("name")  # 第3个节假日名字
    day_3s = (next_3_holiday_date - current_date).days  # 第3个节假日还有多少天

    next_work_url = f"http://timor.tech/api/holiday/workday/next/{next_3_holiday_date_str}"
    next_work_str = requests.request("GET", next_work_url, headers="", data="").text
    next_work_data = json.loads(next_work_str).get("workday").get("date")

    # 第4个节假日时间
    next_holiday_url = f"""https://timor.tech/api/holiday/next/{next_work_data}?type=N&week=N"""
    next_holiday_str = requests.request("GET", next_holiday_url, headers="", data="").text
    next_4_holiday_date_str = json.loads(next_holiday_str).get("holiday").get("date")  # 第4个节假日的日期
    next_4_holiday_date = datetime.strptime(next_4_holiday_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
    next_4_holiday_name = json.loads(next_holiday_str).get("holiday").get("name")  # 第4个节假日名字
    day_4s = (next_4_holiday_date - current_date).days  # 第4个节假日还有多少天


    title = "[ 摸鱼提醒 ]"

    content = now + f"""下午好，摸鱼人
工作再累，一定不要忘记摸鱼哦
有事没事起身去茶水间去厕所去廊道走走，别老在工位上坐着。
钱是老板的，但命是自己的。
距离{next_1_holiday_name}还有{day_1s}天
距离{next_2_holiday_name}假期还有{day_2s}天
距离{next_3_holiday_name}假期还有{day_3s}天
距离{next_4_holiday_name}假期还有{day_4s}天"""

    msg = title + "\n\n" + content
    print(msg)
    
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
