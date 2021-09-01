import os
import requests
import json
import time

def main():
    send_url = os.environ["send_url"]
    send_key = os.environ["send_key"]
    tian_api_key = os.environ["tian_api_key"]

    joke_url = "http://api.tianapi.com/txapi/joke/index?num=1&key=" + tian_api_key

    joke_str = requests.request("GET", joke_url, headers="", data="").text

    joke_body = json.loads(joke_str).get("newslist")[0]

    joke_title = "[ " + joke_body.get("title") + " ]"
    joke_content = joke_body.get("content")
    joke = joke_title + "\n" + joke_content

    now = time.strftime("%H点%M分", time.localtime())
    title = now + "午饭时间到! " + "轻松一笑"

    msg = title + "\n\n" + joke
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
