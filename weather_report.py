import os
import requests
import json
import time

def main():
    send_url = os.environ["send_url"]
    send_key = os.environ["send_key"]
    cur_city = "上海"
    weather_url = "https://api.vvhan.com/api/weather?city=" + cur_city
    holiday_url = "http://timor.tech/api/holiday/tts"

    weather_str = requests.request("GET", weather_url, headers="", data="").text
    weather_info = json.loads(weather_str).get("info")
    weather_type = weather_info.get("type")
    high_temp = weather_info.get("high").split(" ")[1]
    low_temp = weather_info.get("low").split(" ")[1]
    wind_type = weather_info.get("fengxiang")
    wind_level = weather_info.get("fengli")

    holiday_str = requests.request("GET", holiday_url, headers="", data="").text
    tips = json.loads(holiday_str).get("tts")

    content = "城市：" + cur_city + "\n天气：" + weather_type + "\n最高温度：" + high_temp + "\n最低温度：" + low_temp + "\n风向：" + wind_type + "\n风力：" + wind_level + "\n提示：" + tips
    now = time.strftime("%m月%d日", time.localtime()).replace("0", "")

    title = "[ " + now + " 天气状况 ]"
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

    response = requests.request("POST", send_url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()
