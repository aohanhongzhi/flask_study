from flask import Flask,Response
from flask import render_template
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/json')
def root():
    t = {
        # 'data': [{"Name":"zhangsan","Position":"北京","Office":"五彩城","Extn":"好的"}]
        'data': [["zhangsan","北京","五彩城","好的"],["哇哈哈","上海","外滩","可以"]]
    }
    return t

@app.route('/jsono')
def root1():
    t = {
    "code":200,
    "msg":"返回用户数据",
    "data": [
        {
        "name": "Tiger Nixon",
        "position": "System Architect",
        "salary": "$320,800",
        "start_date": "2011/04/25",
        "office": "Edinburgh",
        "extn": "5421"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        },
        {
        "name": "Garrett Winters",
        "position": "Accountant",
        "salary": "$170,750",
        "start_date": "2011/07/25",
        "office": "Tokyo",
        "extn": "8422"
        }]
    }
    # return t
    return Response(json.dumps(t), mimetype='application/json')
    # return json.dumps(t)

@app.route('/table2/')
@app.route('/table2/<name>')
def table(name=None):
    return render_template('table2.html', name=name)
@app.route('/table3/')
@app.route('/table3/<name>')
def table3(name=None):
    return render_template('table3.html', name=name)
@app.route('/ajax/')
@app.route('/ajax/<name>')
def ajax(name=None):
    return render_template('ajax.html', name=name)
if __name__ == "__main__":
    app.debug = True
    app.run()
    pass