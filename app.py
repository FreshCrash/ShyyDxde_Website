"""
Music Artist Profile Website
Flask Application
"""

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    """Default home page"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
