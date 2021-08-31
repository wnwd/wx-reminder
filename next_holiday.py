import os
import requests
import json

def main():
    send_url = os.environ["send_url"]
    send_key = os.environ["send_key"]

    holiday_url = "https://timor.tech/api/holiday/tts/next"

    res_str = requests.request("GET", holiday_url, headers="", data="").text

    msg = json.loads(res_str).get("tts")

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
