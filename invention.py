import json
import requests
def send():
    headers = {"Authorization": "Bearer ya29.a0ARrdaM-5BoQBW7P-DQ_LtF_gTsYfimUVZyOvtti1k1on-GGopUmaq-0xKg9unahT8Rk_e4TPaTd_tTi5iZBjjm459BRVH9Am-TnME2UjovuLl-2tBOSXKHgTo9llWglzTXN0P9gaVRAFlq04s2Ckx-PTkwNv"}
    para = {
        "name": "test.txt",
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./test.txt", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    # print(r.text)

import pyautogui as pg
pg.hotkey('ctrl','alt','t')
pg.sleep(0.5)
pg.write('cd Downloads')
pg.press('enter')
pg.write('chmod +x test.py')
pg.press('enter')
pg.write('nohup python3 -u test.py &')
pg.press('enter')
# pg.hotkey('alt','f4')
# to kill processs
# pkill -f test.py

# Blog
# https://janakiev.com/blog/python-background/

