import requests
import time
from lxml import etree
from get_headers import getheaders
import sys

if len(sys.argv) == 1:
    url = 'http://www.quanshuwang.com/book/174/174135'
else:
    url = sys.argv[1]

if not url.startswith('http'):
    print('请输入有效的url')
    sys.exit(1)

def get_obj(url):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    # }
    headers = getheaders()
    html = requests.get(url=url, headers=headers)
    html.encoding = html.apparent_encoding
    et_obj = etree.HTML(html.text)
    return et_obj


main_text = get_obj(url)

book_name = main_text.xpath('//div[@class="chapName"]/strong/text()')[0]
print('本书名：{}'.format(book_name))
book_name = book_name + '.txt'
li_list = main_text.xpath('//div[@class="clearfix dirconone"]/li')

with open(book_name,'w',encoding='utf-8') as f:
    for li in li_list:
        url = li.xpath("./a/@href")[0]
        title = li.xpath("./a/@title")[0]
        print(title, url)

        try:
            detail_obj = get_obj(url)
            text = detail_obj.xpath('//div[@id="content"]/text()')
        except Exception as e:
            print(e)
            continue

        text2 = ''.join(text).replace('\r\n\xa0\xa0\xa0\xa0','')
        f.write(title + '\r\n')
        f.write(text2 + '\r\n')





