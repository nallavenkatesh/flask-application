
import os

from flask import Flask, render_template, request,jsonify



app = Flask(__name__)


app.config['UPLOADED_PATH'] = os.getcwd() + '/upload'


@app.route('/application', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html');

@app.route('/', methods=['GET'])
def hello():
    list = ['abc siddique', 'def-456', 'ghi-789', 'xyz siddique', '123 siddique']
    filter(lambda x: 'siddique' in x, list)
    return jsonify({'list':list })

if __name__ == '__main__':
    app.run(debug=True)