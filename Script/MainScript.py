import requests
import random
import string
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
reqcnt = 0
while True:
    reqcnt += 1
    response = requests.get("https://peakxel.tpddns.cn/")
    print(reqcnt)
