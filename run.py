from flask import Flask, url_for, render_template,request
app = Flask(__name__)

@app.route('/')
# @app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

# @app.route('/test/')
# def test():
#     print("this is test page!")
#
# @app.route('/index/')
# @app.route('/index/<name>')
# def h(name= None):
#     return render_template('test.html', name=name)
#
#
# @app.route('/login/', methods=['GET'])
# @app.route('/login/<name>')
# def h_1(name= None):
#     data = request.args.get('name')
#     print(data)
#     return render_template('test.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
1