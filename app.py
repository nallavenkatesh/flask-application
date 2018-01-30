
import os

from flask import Flask, render_template, request
import new


app = Flask(__name__)


app.config['UPLOADED_PATH'] = os.getcwd() + '/upload'


@app.route('/application', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html');

@app.route('/' )
def hello_world():
    list = ['abc siddique', 'def-456', 'ghi-789', 'xyz siddique', '123 siddique']
    print filter(lambda x: 'siddique' in x, list)
    return hello_world;

if __name__ == '__main__':
    app.run(debug=True)