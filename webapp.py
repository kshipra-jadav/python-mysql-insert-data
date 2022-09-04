from urllib import request
from flask import Flask, render_template, request
from dbconn import start

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if(request.method == "POST"):
        f = request.files['excel_file']
        f.save(f.filename)
        start(f.filename)
        return 'file upload successfully'



if __name__ == '__main__':
    app.run(debug=True)