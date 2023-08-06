===================
ip_info：获取ip信息
===================

描述：
当前最右会对用户ip进行地域识别，在敏感时期可能会对某些特定的地区、省份、国家的ip做特殊的标记处理。

说明：
当前此项目用到了ipip上的免费版ip鉴定本地包，对于无法鉴定的ip再用淘宝ip免费ip鉴定接口加以辅助。

使用：
from xc_ip_info.ip_info import IPSearcher
IPSearcher.search('123.125.71.38')
IPSearcher.validate('61.128.101.255')
即可，具体case可以见test下测试用例。

安装：
用的是最内内部的私有pip服务器。因此需要在内网环境下安装。
第一次：sudo pip install xc_ip_info -i 'http://172.16.111.203:8081' --trusted-host '172.16.111.203'
之后：sudo pip install --upgrade xc_ip_info -i 'http://172.16.111.203:8081' --trusted-host '172.16.111.203'
回滚到某个版本：sudo pip install xc_ip_info==0.5 -i 'http://172.16.0.173:8080' --trusted-host '172.16.0.173'
查看所有版本信息的web前端访问：http://172.16.0.173:8080

上传：
1.首先需要获取你的私有pypi账户和密码，可以找op权洲。
2.修改你的~/.pypirc，最简单的包括如下几行：
[distutils]
index-servers =
    local
[local]
repository: http://172.16.0.173:8080
username: yourname
password: yourpassword
3.构建：python setup.py sdist build
4.上传：python setup.py sdist upload -r local