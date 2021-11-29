from flask import Flask 
from flask import render_template

app2 = Flask(__name__)

@app2.route('/')
def index():
    return render_template('main.html')

'''
@app2.route('/work_single.html')
def work_single():
    return render_template('work_single.html')
'''

if __name__ == '__main__':
    app2.run(debug=True)