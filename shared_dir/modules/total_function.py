import numpy as np
from ultralytics import YOLO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import openai

from modules.api_key import API_KEY,ORGANIZATION_KEY

def gpt(food_list:list) -> str:
    openai.organization = ORGANIZATION_KEY
    openai.api_key = API_KEY
    
    if len(food_list) == 1:
        connect_text:str = 'Please tell me the name and process of cooking with ' \
                                + f'{food_list[-1]}'
    else:
        connect_text:str = 'Please tell me the name and process of cooking with ' \
                                + ', '.join(food_list[:len(food_list)-1])  \
                                        + f' and {food_list[-1]}'
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=connect_text,
        max_tokens=2000,
        temperature=0.7,
        n=1,
        stop=None,
    )
    
    return response.choices[0].text



def yolo(img_path:str) -> list:
    model = YOLO('./model/green_pepper.pt')
    # model("sample.png",save=True, conf=0.2, iou=0.5)
    results = model(img_path,save=False, conf=0.2, iou=0.5)
    names = results[0].names
    vegetables_list=[]
    for value in names.values():
        vegetables_list.append(value)
    return vegetables_list



def translate(text:str, from_lang:str, to_lang:str) -> str:
    """
    引数    : 翻訳したいテキスト, 翻訳したいテキストの言語, 翻訳する言語
    返り値  : 翻訳されたテキスト
    """
    # seleniumとchoromDriverでDeepLにアクセス
    load_url = 'https://www.deepl.com/translator#' + from_lang +'/' + to_lang + '/' + text
    chrome_path = '/opt/google/chrome/google-chrome'

    options = Options()
    options.binary_location = chrome_path
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)  #  driver = webdriver.Chrome()
    driver.get(load_url)

    time.sleep(5)

    #2023/04/21
    # output = ".lmt__textarea_container .lmt__inner_textarea_container d-textarea"
    output_selector = 'd-textarea.lmt__textarea.lmt__target_textarea.lmt__textarea_base_style.focus-visible-disabled-container'
    Outputtext = driver.find_element_by_css_selector(output_selector).get_attribute("textContent")

    return Outputtext