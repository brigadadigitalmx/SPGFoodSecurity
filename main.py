from opt.voronoi import voronoi
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "API working"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
