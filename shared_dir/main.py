#! /usr/bin/env python3
"""
見やすいコードを書きましょう
"""


import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import cv2
from modules.total_function import *


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def front():
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
            dict = predict(file_path,num)
            # return predict(file_path,num)
            return process(dict)


    return render_template('home.html')
    # return process(text)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/process', methods=['GET','POST'])
def process(dict):
    return render_template('result.html',data=dict)

def predict(filename:str, num:str) -> str:
    # YOLOに入力
    food_list = yolo(filename)
    # food_list = ['tomato','green pepper']
    # # chat-GPTに入力
    text = gpt(food_list)
    # print(text)
    
    # text = '1. Potato and Carrot Mash: Boil the potatoes and carrots until soft. Mash together with butter, salt, pepper, and garlic.' \
    #         + '2. Potato and Carrot Fritters: Grate the potatoes and carrots and mix with an egg, flour, salt, and pepper. Form into patties and pan-fry until golden.' \
    #          + '3. Roasted Potato and Carrot Salad: Cut the potatoes and carrots into cubes and toss with olive oil, salt, and pepper. Roast in a preheated oven at 400°F until tender. Serve with a dressing of your choice over a bed of greens. ' \
    #           + '4. Potato and Carrot Soup: Sauté onions and garlic in a pot. Add the potatoes and carrots and cook until softened. Add stock and simmer until vegetables are cooked through. Blend until smooth. ' \
    #            + '5. Baked Potato and Carrot Chips: Thinly slice potatoes and carrots and toss with olive oil, salt, and pepper. Bake in a preheated oven at 400°F for 20-25 minutes, flipping halfway through.'
    # text = '1.Stuffed Peppers: Stuff hollowed-out green peppers with a mixture of diced tomatoes, cooked rice, onion, garlic and herbs.' \
    #             '2.Tomato Soup: Simmer tomatoes, green peppers, onion, garlic, and a variety of herbs and spices in a pot of vegetable broth.' \
    #                 '3.Tomato and Pepper Sauté: Sauté chopped tomatoes, peppers, onion, garlic, and herbs in olive oil until vegetables are softened.' \
    #                     '4.Tomato and Pepper Pizza: Spread tomato sauce over pizza dough, top with grated cheese and roasted green peppers and tomatoes.' 
    dishes_list,text_list = dishes_select(text,int(num))

    img_list: list = image(dishes_list,text_list)

    # DeepLに入力
    """
    引数    : 翻訳したいテキスト, 翻訳したいテキストの言語, 翻訳する言語
    返り値  : 翻訳されたテキスト
    """
    discription_translate = []
    dish_translate = []
    for dish, text in zip(dishes_list,text_list):
        translate_text = translate(text, 'en', 'ja')
        translate_dish = translate(dish,'en','ja')
        discription_translate.append(translate_text)
        dish_translate.append(translate_dish)

    dict = molding(dish_translate, discription_translate, img_list)

    return dict
    # return img_dict,text_list


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
    # dict = predict(filename=None,num=None)
    # print(dict)
    
