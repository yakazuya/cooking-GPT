#! /usr/bin/env python3
"""
見やすいコードを書きましょう
"""


import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import cv2
from modules.total_function import translate,yolo,gpt,dishes_select,image


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template('front.html')

@app.route('/home', methods=['GET', 'POST'])
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
            num = request.form.get('num')  # numの値を取得
            text = predict(file_path,num)
            # return predict(file_path,num)
            return process(text)


    return render_template('home.html')
    # return process(text)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/process', methods=['GET','POST'])
def process(text):
    return render_template('result.html',text=text)

def predict(filename:str, num:str) -> str:
    # YOLOに入力
    food_list = yolo(filename)
    food_list = ['tomato','green pepper']
    # chat-GPTに入力
    # text = gpt(food_list)
    sug = 3
    text = '1. Potato and Carrot Mash: Boil the potatoes and carrots until soft. Mash together with butter, salt, pepper, and garlic.' \
            + '2. Potato and Carrot Fritters: Grate the potatoes and carrots and mix with an egg, flour, salt, and pepper. Form into patties and pan-fry until golden.' \
             + '3. Roasted Potato and Carrot Salad: Cut the potatoes and carrots into cubes and toss with olive oil, salt, and pepper. Roast in a preheated oven at 400°F until tender. Serve with a dressing of your choice over a bed of greens. ' \
              + '4. Potato and Carrot Soup: Sauté onions and garlic in a pot. Add the potatoes and carrots and cook until softened. Add stock and simmer until vegetables are cooked through. Blend until smooth. ' \
               + '5. Baked Potato and Carrot Chips: Thinly slice potatoes and carrots and toss with olive oil, salt, and pepper. Bake in a preheated oven at 400°F for 20-25 minutes, flipping halfway through.'
    dishes_list: list = dishes_select(text,sug)

    img_dict: dict = image(dishes_list)

    # for i, dish in enumerate(dishes_list):
    #     img_dict[dish].save(f"{i}.png")

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
