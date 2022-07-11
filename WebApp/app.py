from threading import Thread
from flask import Flask, request as req, render_template
from flaskwebgui import FlaskUI
import os
from login import addDocs


app = Flask(__name__)
RSS = os.path.join('static', 'RSS')
app.config['UPLOAD_FOLDER'] = RSS
# app.config['UPLOAD_FOLDER'] = './RSS'


ui = FlaskUI(app)


@app.route("/", methods = ['GET', 'POST'])
def login():
    if req.method == 'POST':
        uname = req.form.get('uname')
        pwd = req.form.get('pwd')
        addDocs(uname, pwd)
        print(f'Username: {uname}, Password: {pwd}')
    return render_template('login.html', img = os.path.join(app.config['UPLOAD_FOLDER'], 'Authentication_Page.jpg'))

@app.route("/index")
def landing():
    return render_template("index.html")

@app.route("/classifier")
def classifier():
    return render_template("classifier.html")

@app.route("/classifier_output")
def classifier_output():
    return render_template("classifier_output.html")

def main():
    # ui.run()
    app.run(debug = True)

    # t_app = Thread(target = app.run(debug = True))
    # t_ui = Thread(target =  ui.run())
    # t_app.start()
    # t_ui.start()
    # t_app.join()
    # t_ui.join()

if __name__ == '__main__':
    main()
