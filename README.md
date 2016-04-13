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
$ pip install redis
$ pip install Pillow
$ pip install pytesseract
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

