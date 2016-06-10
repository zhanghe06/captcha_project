## 验证码服务

架构风格：RESTful

服务类型：

- 验证码生成

- 验证码请求

- 验证码校验

- 验证码识别

依赖：
```
$ pip install Flask
$ pip install flask-restful
$ pip install redis
$ pip install Pillow
$ pip install pytesseract
$ pip install gunicorn
$ pip install supervisor
```

启动
```
$ cd captcha_project
$ virtualenv captcha.env
$ source captcha.env/bin/activate
$ supervisord -c etc/supervisord.conf
$ supervisorctl -c etc/supervisord.conf reload
$ supervisorctl -c etc/supervisord.conf restart all
```

## tesseract-ocr (Tesseract Open Source OCR Engine)

tesseract-ocr 包安装方式：
```
$ sudo apt-get install tesseract-ocr
```

tesseract-ocr 源码安装方式：

github 项目地址：
[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

下载主分支稳定版：
[https://github.com/tesseract-ocr/tesseract/archive/master.zip](https://github.com/tesseract-ocr/tesseract/archive/master.zip)

```
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
```

对于非 linux 系统, 以下文件 tesseract_cmd 根据需要修改
captcha.env/local/lib/python2.7/site-packages/pytesseract/pytesseract.py
```
# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
tesseract_cmd = 'tesseract'
```

## Flask-RESTful

Flask-RESTful provides the building blocks for creating a great REST API.

[https://github.com/flask-restful/flask-restful](https://github.com/flask-restful/flask-restful)

[http://flask-restful.readthedocs.io/en/latest/](http://flask-restful.readthedocs.io/en/latest/)

[http://www.pythondoc.com/Flask-RESTful/](http://www.pythondoc.com/Flask-RESTful/)

典型的项目结构
```
myapi/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure
```
