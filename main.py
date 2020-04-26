from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "API working"


@app.route('/get_voronoi')
def get_voronoi():
    return "lol"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
