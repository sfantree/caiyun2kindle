#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
from selenium import webdriver

'''
# set pip
https://www.atjiang.com/aliyun-pip-mirror/
https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480

cat $HOME/.pip/pip.conf
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple


pip2 install virtualenv --user
virtualenv venv
source venv/bin/activate
cp $HOME/.pip/pip.conf $VIRTUAL_ENV/pip.conf

# install phantomjs
https://github.com/piksel/phantomjs-raspberrypi

'''

# https://stackoverflow.com/a/40037645
def init_phantomjs_driver(*args, **kwargs):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.102 Safari/537.36',
        'Connection': 'keep-alive'
    }

    for key, value in headers.iteritems():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    webdriver.DesiredCapabilities.PHANTOMJS[
        'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (' \
                                               'KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 '

    # driver = webdriver.PhantomJS()
    driver = webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400, 1000)
    return driver


def init_chrome_driver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--proxy-server=http://127.0.0.1:1084')
    driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path='bin/chromedriver.exe')
    driver.set_window_size(1400, 1000)
    return driver

def main():
    # service_args = [
    #     '--proxy=127.0.0.1:9999',
    #     '--proxy-type=http',
    #     '--ignore-ssl-errors=true'
    #  ]

    # driver = init_phantomjs_driver(service_args = service_args)

    # driver.get('http://cn.bing.com')
    # agent = driver.execute_script("return navigator.userAgent")
    # print agent
    # driver.execute_script("return {foo: 'bar'}")

    url = 'https://wiki.archlinux.org/index.php/Installation_guide'
    #url = 'https://www.infoq.cn/'

    print('init_phantomjs_driver')
    driver = init_phantomjs_driver('bin/phantomjs.exe')

    #print('init_chrome_driver')
    #driver = init_chrome_driver()

    print('driver.get(url)')
    driver.get(url)

    print('time.sleep(5)')
    time.sleep(5)

    print('execute_script(caiyunjs)')
    caiyunjs = "return {foo: 'bar'}"
    with open("caiyun.js", "r") as f:
        caiyunjs = f.read()
    driver.execute_script(caiyunjs)

    print('submit_button.click()')
    submit_button = driver.find_elements_by_xpath("//img[@class='cyxy-favorite-btn']")[0]
    submit_button.click()

    print('time.sleep(2)')
    time.sleep(2)

    print('execute_script(autoscroll)')
    autoscroll = 'function scroller(){var position=0;while(position<document.body.scrollHeight)' \
                 '{position+=100;scroll(0,position)}}scroller();'
    driver.execute_script(autoscroll)

    print('time.sleep(5)')
    time.sleep(5)

    print("f.write")
    webtitle = driver.execute_script("return document.title")
    html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
    with open('{}.html'.format(webtitle.encode(sys.getfilesystemencoding())), "w") as f:
        f.write(html.encode('utf-8'))


if __name__ == '__main__':
    main()
