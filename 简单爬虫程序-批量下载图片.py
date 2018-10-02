import re
import urllib.request
import os

def all_url(url_temp):
    """获取所有链接"""
    resp = urllib.request.urlopen(url_temp)  # 访问地址
    data = resp.read().decode('utf-8')  # 将访问的地址的链接读出来并转码
    image_url = re.findall(r'src="(.*?\.jpg)"', data)  # 在全部链接中捕捉图片链接
    return image_url


def down_image(image_url):
    # 获取图片名字
    for i in image_url:
        print(i)
        image_url_str = str(i)
        image_name = image_url_str.split('/')[-1]
        # 下载图片
        image = urllib.request.urlopen(image_url_str)
        image_data = image.read()

        with open(image_name, 'wb') as f:
            f.write(image_data)

def main():
    url = input("请输入链接:")
    image_url_data = all_url(url)
    down_image(image_url_data) 

if __name__ == '__main__':
    main()

