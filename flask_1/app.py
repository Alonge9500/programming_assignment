from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def homepage():
    username = request.args.get('username')
    if username:
        username = username.upper()

        return f'<div><h1>Innomatics Flask Assignment</h1></br><h3>Your Username in uppercase is {username}</h3><body>Hello {username} You are welcome to this website we\'re looking forward to meet your requests.... </body></div>'
    else:
        return '<div><h1>Innomatics Flask Assignment</h1></br><h3>Kindly input your username </h3></div>'
        

if __name__ == '__main__':
    app.run(debug=True)