#encoding: utf-8

from flask import Flask,request,make_response,render_template  
import hashlib 
import time

app = Flask(__name__)
app.debug = True

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/login')
def login():
    return render_template('login.html')
