# shortcut 'hw'
from flask import Flask, render_template

# initialize objects
# searches in 'templates' folder by default, changed to 'views'
app = Flask(__name__, template_folder='views')

# print(app.config)

# changes config so max age for static files from 12 hrs to 0
# good for development, where files change often
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# controllers
# -----------------------------------------------
@app.route('/')
def homepage():
    web_info = {
        'title':'Website title',
        'subtitle':'subtitle here',
        'show_about': True
    }
    return render_template("home.html", sent_data = web_info) 

@app.route('/hw')
def hw():
    return 'Hello World!'

@app.route('/about')
def about():
    return render_template("about.html")

# if app.py is ran directly (say, from an IDE), 
# enable debugging
if __name__ == '__main__':
    app.run(debug=True)
