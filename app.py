from flask import Flask, redirect,render_template, request,redirect
app = Flask(__name__)
app.config['data']="static/"


def delete(request):
    username=request.form['username']
    msg=open(app.config['data']+"data.txt","r").read().split("\n")
    msg=[x for x in msg if x.split(",")[0]!=username]
    f=open(app.config['data']+"data.txt","w")
    for x in msg:
        f.write(x+"\n")
    user_data,username=show(request)
    return user_data,username
    
    
def add(request):
        username=request.form['username']
        message=request.form['message']
        f=open(app.config['data']+"data.txt","a")
        f.write(username+","+message+"\n")
        dat=open(app.config['data']+"data.txt","r").read().split("\n")
        user_data=[x.split(",")[1] for x in dat if x.split(",")[0] == username]
        user_data.append(message)
        return user_data,username

def show(request):
    username=request.form['username']
    dat=open(app.config['data']+"data.txt","r").read().split("\n")
    user_data=[x.split(",")[1] for x in dat if x.split(",")[0] == username]
    if len(user_data)==0:
        user_data=["No message"]
        return user_data,username
    else:
        return user_data,username
    

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method=="POST":
        if request.form.get('submit') == 'submit':
            user_data,username=add(request)
            return render_template('index.html', result=user_data,username=username)
        elif request.form.get('delete') == 'delete':
            user_data,username=delete(request)
            return render_template('index.html', result=user_data,username=username)
        elif request.form.get('show') == 'show':
            user_data,username=show(request)
            return render_template('index.html', result=user_data,username=username)
        
    return render_template('index.html', result="")
        
if __name__ == "__main__":
    app.run(debug=True)