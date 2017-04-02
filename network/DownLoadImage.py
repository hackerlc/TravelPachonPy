# 下载图片

import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

decode = 'utf-8'
headers = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' \
                         ' Query String Parameters view source view URL encoded ')]


def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100

    print(str(percent))


def downLoadImg(url, file_name):
    opener = urllib.request.build_opener()
    opener.addheaders = headers
    urllib.request.install_opener(opener)
    try:
        urllib.request.urlretrieve(url, file_name, reporthook=callbackfunc)
    except:
        return False
    else:
        return True


# test downLoadImg
# downLoadImg('https://jp.netcdn.space/digital/video/1star00763/1star00763pl.jpg', '/Volumes/10.11.3/Users/mac/Downloads/do/test.jpg')
