#! /usr/bin/env python3
"""
見やすいコードを書きましょう
"""
import cv2
import numpy as np
from modules.translate_DeepL import translate

def YOLO(img:np.array) -> list:
    food_list = ['egg', 'greenpepper', 'tomato']
    return food_list

def gpt(food_list:list) -> str:
    text =' Here are three recipes that can be made with only the three ingredients you listed:,Tomato and Egg Stir Fry:,Ingredients:,2 medium-sized tomatoes, diced,2 eggs, beaten,1 green pepper, chopped,Salt and pepper, to taste,Instructions:,Heat some oil in a skillet over medium-high heat.,Add the diced tomatoes and chopped green pepper to the skillet and stir-fry for 2-3 minutes until the vegetables are slightly softened.,Pour in the beaten eggs and stir-fry everything together until the eggs are cooked.,Season with salt and pepper to taste, and serve.,Tomato and Green Pepper Omelet:'
    return text

def main(img:np.array) -> str:
    print('バックグラウンドメイン処理')

    # YOLOに入力
    food_list = YOLO(img)

    # chat-GPTに入力
    text = gpt(food_list)

    # DeepLに入力
    """
    引数    : 翻訳したいテキスト, 翻訳したいテキストの言語, 翻訳する言語
    返り値  : 翻訳されたテキスト
    """
    translate_text = translate(text, 'en', 'ja')

    return translate_text


if __name__ == '__main__':
    img = cv2.imread('./test.jpeg', cv2.IMREAD_COLOR)
    output_text = main(img)