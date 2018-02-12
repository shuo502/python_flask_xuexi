from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/run/')
def run():
    return 'Hello run!'
@app.route('/link')
def link():
    x='''
    <a href="./php/index.php">proxy-download</a></br>
<a href="./php/phpproxy.php?url=http://sina.com">proxy-phpproxy http://sina.com</a></br>
<a href="./php/goproxy.php">goproxy</a></br>
<a href="./php/shadowsocksphp/start.php">shadowsocksphp</a></br>
<a href="http://ot-other.a3c1.starter-us-west-1.openshiftapps.com "> python </a></br>
    '''
    return x

if __name__ == '__main__':
    app.run(port=8080)
# pip install pyOpenSSL
# 1
# 2 在 Flask 的代码中可以直接使用
    app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')