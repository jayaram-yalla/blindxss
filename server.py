from flask import *
import flask
from flask_cors import CORS
app=Flask(__name__)
'''

,static_folder='static',template_folder='templates'

'''

CORS(app)

@app.route("/")
def index():
    ipa=flask.request.remote_addr
    ua=flask.request.user_agent.string
    return ipa+" : "+ua+"<marquee></br></br>goto http://URL/login</marquee>"

@app.route("/login")
def login():
    return render_template('index.html')

@app.route("/logins",methods = ['POST'])
def logins():
    try:
        if request.method == 'POST':
            uname=request.form['username'].encode('utf-8')
            pwd=request.form['password'].encode('utf-8')
            if uname.isalnum() and pwd.isalnum() == True:
                return uname+":"+pwd
            else:
                ipa=flask.request.remote_addr
                ua=flask.request.user_agent.string
                f=open('audit.html','a')
                f.writelines('\n</br>'+ipa+'</br>'+ua+'</br>\n')
                f.close()
                return '''<center><h1>special chars found and your IP, browser info logged for ADMIN review</br>http://URL/adminLogAudit</h1></center>'''
        else:
            return '''method not allowed'''
    except Exception:
        return '''reload the page'''

@app.route("/adminLogAudit")
def admin():
    ipa=flask.request.remote_addr
    if "127.0.0.1" == ipa:
        log=''
        f=open('audit.html','r')
        for i in f:
            log=log+i
        f.close()
        return log
    else:
        return '<center><h1>if you are admin please use the same URL in server box</br>admin log refresh every 5min to remove (</br></h1></center> '
app.run(host="0.0.0.0",port=8090,debug=True)

