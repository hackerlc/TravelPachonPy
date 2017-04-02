# 地点正则

import re


def getAddress(html):
    patten = re.compile(r'<a href="/travel-scenic-spot/mafengwo/[\S]*?.html" target="_blank">(.*?)[\s]?<')
    address = patten.findall(html)

    return address

# test
# print(getAddress('<a href="/travel-scenic-spot/mafengwo/10065.html" target="_blank">北京</a>'
#                  '<a href="/travel-scenic-spot/mafengwo/12684.html" target="_blank">台湾</a>'
#                  '<a href="/travel-scenic-spot/mafengwo/57166.html" target="_blank">瑙鲁 <span class="en">Nauru</span>'))
