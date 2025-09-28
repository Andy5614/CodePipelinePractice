# application.py
from flask import Flask

# Elastic Beanstalk 預設會尋找名為 'application' 的 WSGI 變數
application = Flask(__name__)

@application.route('/')
def index():
    return "Hello, Elastic Beanstalk! 部署成功!!!!!!!!!!??????????????🎉7777777999888"

# 本地測試時可以使用這段
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
