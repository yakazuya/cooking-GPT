from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

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
    output_selector = '#target-dummydiv'
    Outputtext = driver.find_element_by_css_selector(output_selector).get_attribute("textContent")

    return Outputtext

if __name__ == '__main__':
    text = 'Hello DeepL'
    from_lang = 'en'
    to_lang = 'ja'
    translate_text = translate(text, from_lang, to_lang)