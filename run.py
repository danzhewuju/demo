from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
