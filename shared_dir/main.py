#! /usr/bin/env python3
"""
見やすいコードを書きましょう
"""


import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
import numpy as np
import cv2
from modules.total_function import translate,yolo,gpt


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # return redirect(url_for('uploaded_file', filename=filename))

            return predict(file_path)


    return '''
    <!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>cookGPT</title></head>
    <body>
    <h1>ファイルをアップロード</h1>
    <form method = post enctype = multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def predict(filename:str) -> str:
    # YOLOに入力
    food_list = yolo(filename)
    # chat-GPTに入力
    text = gpt(food_list)

    # DeepLに入力
    """
    引数    : 翻訳したいテキスト, 翻訳したいテキストの言語, 翻訳する言語
    返り値  : 翻訳されたテキスト
    """
    # translate_text = translate(text, 'en', 'ja')

    # return translate_text
    return text


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
