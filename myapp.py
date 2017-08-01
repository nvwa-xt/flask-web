from flask import Flask,request,make_response,render_template  
import hashlib 
import time

app = Flask(__name__)
app.debug = True

@app.route('/xiaohui')
def hello():
    return "Hello, world! - Flask- xiaohui"

@app.route('/wx', methods = ['GET', 'POST'] )  
def wechat_auth():  
    if request.method == 'GET':  
        token = 'xiaomeng12348765'   
        query = request.args  
        signature = query.get('signature', '')  
        timestamp = query.get('timestamp', '')  
        nonce = query.get('nonce', '')  
        echostr = query.get('echostr', '')  
        s = [timestamp, nonce, token]  
        s.sort()  
        s = ''.join(s)  
        if ( hashlib.sha1(s).hexdigest() == signature ):    
            return make_response(echostr) 

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/test')
def index():
    return render_template('index.html')
