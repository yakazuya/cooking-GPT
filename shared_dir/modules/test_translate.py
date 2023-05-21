from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
# seleniumとchoromDriverでDeepLにアクセス
from_lang = 'en'
to_lang = 'ja'
# text = 'How’s everything?'
text = 'As consumers pay more attention to package labels, and legislation starts requiring food companies to be upfront about what goes into their products, downsizing has become a popular way for good businesses to deal with increasing pressure to cut calories and boost healthiness in processed foods.'
load_url = 'https://www.deepl.com/translator#' + from_lang +'/' + to_lang + '/' + text
print(load_url)
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
# print('')
# print('')
# print(f'input : {text}')
print(f'output : {Outputtext}')
