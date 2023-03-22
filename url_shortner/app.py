import os
from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import random

alphanumeric="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONOPQRSTUVWXYZ123456789_"

basedir =os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Url(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    url = db.Column(db.String,nullable=True)
    shorten = db.Column(db.String,nullable=False)
    
    def __repr__(self):
        return f"Main Url {self.url}--------Shorten Url {self.shorten}"
    
    
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        short_url = "".join(random.sample(alphanumeric, 4))
        #short_url = short_url
        url_l = Url(url=url,shorten=short_url)
        db.session.add(url_l)
        db.session.commit()
        urls = Url.query.all()
        
        return redirect(url_for('result'))
    else:
        return render_template('index.html')

@app.route('/<id>/<shorten>')
def redirect_url(id,shorten):
    print(id)
    urll = Url.query.filter_by(id=id).first().url
    return redirect(urll)
    

@app.route('/result',methods=['GET','POST'])
def result():
    urls = Url.query.all()
    return render_template('results.html',urls=urls)

    

if __name__ == '__main__':
    app.run(debug=True)