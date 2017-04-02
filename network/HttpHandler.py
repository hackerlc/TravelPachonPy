# http处理

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

decode = 'utf-8'
user_agent = 'user_agent'
header_chrome = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' \
                ' Query String Parameters view source view URL encoded '


# 判断连接是否可以访问，如果不能访问则返回none
def getHtml(url):
    req = urllib.request.Request(url)
    req.add_header(user_agent, header_chrome)
    try:
        page = urllib.request.urlopen(req)
    except:
        html = None
    else:
        html = page.read()
        return html.decode(decode)


# test
# html = getHtml('https://avmo.pw/cn/genre')
# if html is None:
#     print('连接丢失')
# else:
#     print(html)
