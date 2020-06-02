from flask import Flask, url_for, render_template, request
import os

app = Flask(__name__)


'''
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)
'''

@app.route('/', methods=['GET', 'POST'])
@app.route('/<name>')
def hello(name=None):
    ori_path = None
    gen_path = None
    if request.method == 'POST':
        img = request.files.get('file1')
        img_name = img.filename
        upload_path = os.path.join("static", "upload")
        imgsrc_path = os.path.join("static", "img")
        img_path = os.path.join(upload_path, img_name)
        img.save(img_path)
        ori_path = os.path.join("..", img_path)
        gen_path = os.path.join('..', imgsrc_path, img_name.split('.')[0] + "_fake.png")

    return render_template('hmq.html', name=name, ori_path=ori_path, gen_path=gen_path)


if __name__ == '__main__':
    app.run(debug=True)
