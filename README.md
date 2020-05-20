# caiyun2kindle
english web output with caiyun translator

使用彩云小译脚本翻译为中英双语网页并导出为kindle可阅读的格式

---

#### 说明

##### 安装phantomjs

手动下载`phantomjs`到`bin`目录

树莓派适配的`phantomjs`的二进制文件

https://github.com/piksel/phantomjs-raspberrypi

##### 设置pip

https://www.atjiang.com/aliyun-pip-mirror/

https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480

```bash
cat $HOME/.pip/pip.conf
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple
```

推荐使用virtualenv

```bash
pip2 install virtualenv --user
virtualenv venv
source venv/bin/activate
cp $HOME/.pip/pip.conf $VIRTUAL_ENV/pip.conf
```
