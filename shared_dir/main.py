#! /usr/bin/env python3
"""
見やすいコードを書きましょう
"""
import cv2
import numpy as np

from modules.total_function import translate,yolo,gpt

def main(img:np.array) -> str:
    print('バックグラウンドメイン処理')

    # YOLOに入力
    food_list = yolo(img)
    
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