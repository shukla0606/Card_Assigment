


from flask import Flask, render_template, request, redirect, url_for
from model import probe_model_5l_profit
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        content = file.read()
        data = json.loads(content)
        results = probe_model_5l_profit(data["data"])
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

