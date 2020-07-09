from flask import Flask

from flask import render_template,request

app = Flask(__name__)


#路由 匹配url中的action
@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        pass

@app.route('/schoolQuery',methods=['GET','POST'])
def schoolQuery():
    if request.method == 'GET':
        return render_template('schoolQuery.html')
    else:
        pass

@app.route('/catQuery',methods=['GET','POST'])
def catQuery():
    if request.method == 'GET':
        return render_template('catQuery.html')
    else:
        pass


#启动服务器
if __name__ == '__main__':
    app.run()
