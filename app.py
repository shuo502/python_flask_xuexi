from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/run/')
def run():
    return 'Hello run!'


if __name__ == '__main__':
    app.run(port=8080)
# pip install pyOpenSSL
# 1
# 2 在 Flask 的代码中可以直接使用
    app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')