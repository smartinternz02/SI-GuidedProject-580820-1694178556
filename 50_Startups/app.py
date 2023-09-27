import pickle as pkl

import numpy as np
from flask import *

app = Flask(__name__)
model = pkl.load(open('50_Startup.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def compute():
    p = request.form["rd"]
    q = request.form["ad"]
    r = request.form["me"]
    s = request.form["st"]

    if s == 'cal':
        s = 0
    elif s == 'flo':
        s = 1
    else:
        s = 2

    t = [[float(p), float(q), float(r), float(s)]]
    output = model.predict(t)

    # print(output)

    return render_template("index.html",
                           message="The Predicted profit from your given details is " + str(np.round(output[0])))


if __name__ == '__main__':
    app.run()
