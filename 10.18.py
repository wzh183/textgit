import requests
import os
from lxml import html
import json
import csv
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=13'
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

}
response = requests.get(url, headers=header)
# response.encoding = 'utf-8'
a = response.text
b = json.loads(a)
#
# print(b)
hero = b["hero"]

# with open("图库/ye.jpg", mode='wd', newline='') as f:
for he in hero:
    # print(he)
    tp = he["selectAudio"]
    # print(tp)
    # print()
    # id = he["heroId"]
    # name = he["name"]
    # yw = he["alias"]
    # tp = he["selectAudio"]

    # print(id, name, yw)
    # row = ['id', 'name', 'yw']
    # row1 = [id, name, yw, tp]
    # row1 = [tp]

    # image_url = "https://www.shuquge.com/files/article/image/3/3478/3478s.jpg"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    r = requests.get(tp, headers=headers)
    # 下载图片
    with open("图库", mode="a+b") as f:
        f.write(r.content)  # 图片内容写入文件


        # write = csv.writer(f)
        # write.writerow(row1)




# page = html.etree.HTML(response.text)
# jd = page.xpath('//ul[@class="swiper-slide swiper-slide-visible swiper-slide-active"]/li/p/text()')
# print(jd)