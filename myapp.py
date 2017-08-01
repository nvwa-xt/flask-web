from flask import Flask,request, make_response  
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
    token = 'aomeng12348765' # your token  
    query = request.args  # GET 方法附上的参数  
    signature = query.get('signature', '')  
    timestamp = query.get('timestamp', '')  
    nonce = query.get('nonce', '')  
    echostr = query.get('echostr', '')  
    s = [timestamp, nonce, token]  
    s.sort()  
    s = ''.join(s)  
    if ( hashlib.sha1(s).hexdigest() == signature ):    
      return make_response(echostr)  
