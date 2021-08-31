import os

def main():
    SCKEY = os.environ["key"]
    MESSAGE = os.environ["message"]

    print(SCKEY)
    print(MESSAGE)
    print("获取变量成功!")


if __name__ == '__main__':
    main()
