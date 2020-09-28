import sys
sys.path.insert(0, '/User/odakyeong/sba-2-api')

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()

    