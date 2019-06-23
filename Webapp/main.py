import flask
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

import smtplib
import time
import imaplib
import email
import sys
sys.path.append('D:\EmotionDetection')
# print(sys.path)
from Mails import Mail

app = flask.Flask(__name__,static_url_path='/static')
m=[]
resp=[] 
frm=[]    
subj=[]
# obj=Mail()
# messages=obj.SendLatestMails()
# for i in range(0,len(messages)//4,4):
#   # print(message)
#   frm.append(messages[i])
#   subj.append(messages[i+1])
#   m.append(messages[i+2])
#   resp.append(messages[i+3])


a=["hello"]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
a={}
with open('..\\data.json', 'r') as f:
    distros_dict = json.load(f)
    a=distros_dict
b=a[0]["ratings"]
for i in range(5):
  e.append(b[str(i+1)+' star'])
# print(e)

c=a[0]['reviews']
b=[]
h=[]
sent=[]
k=[]
l=[]
k=a[0]['price']
l=a[0]['url']
for i in range(5):
  d.append(c[i]['review_text'])
  b.append(c[i]['review_posted_date'])
  h.append(c[i]['review_header'])
# print(d[1])
f=open("../emotion.txt")
f1=f.readlines()
recv=[]
count=0
for x in f1:
  if count%2==0:
    sent.append(x)
  elif count%2==1:
    recv.append(x)
  count+=1
# @app.route("/mail")
# def mail():
#     result={'From':frm,'subject':subj,'response':resp}
#     return flask.render_template("mail.html",result=result)
@app.route("/")
def home():
    result={'emotions':sent,'response':recv}
    return flask.render_template("home.html",result=result)

@app.route("/amazon")
def amazon():
    # result = {'count' : str(count.get()), 'uploads' : uploads.get() ,'plate':x}
    result={'ratings':e,'reviews':d,'title':h,'date':b,'url':l,'price':k}
    return flask.render_template("amazon.html",result=result)
@app.route("/about")
def about():
    return flask.render_template("about.html")
if __name__ == "__main__":

    app.run(debug=True)
