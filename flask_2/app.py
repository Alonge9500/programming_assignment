from flask import Flask,request,render_template
import re

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def match():
    if request.method == 'POST':
        match = request.form['pattern']
        text = request.form['text']
        
        results = re.findall(match,text)
    
        return render_template('index.html',results=results)
    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)