#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def dkjsdkjsd():
    return render_template('honey.html')
@app.route('/vatsal',methods=['GET','POST'])
def jdjdjdjd():
    if(request.method=='POST'):
        a=int(request.form['n1'])
        b=int(request.form['n2'])
        total=a+b
        return render_template('honey.html',card=total)
if __name__=='__main__':
    app.run()


# In[ ]:




