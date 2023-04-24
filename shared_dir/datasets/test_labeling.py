#! usr/env python
import cv2
import numpy as np
from rembg import remove

magic_number = {
    'h1' : 110,
    'h2' : 150,
    'w1' : 90,
    'w2' : 170
}
def boundingRect(img):
    print('')
    # 画像リストの取得
    h, w = img.shape[:2]
    rgb = img
    # center crop
    rgb = rgb[int(h/2) - magic_number['h1'] : int(h/2) + magic_number['h2'], int(w/2) - magic_number['w1'] : int(w/2) + magic_number['w2']]

    # rembgでマスク作成
    rgb_rembg = remove(rgb)
    gray = cv2.cvtColor(rgb_rembg, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
    mask_h, mask_w = mask.shape[:2]
    # 0梅
    pad = {
        'top' : int((h/2) - magic_number['h1']),
        'bottom' : None,
        'left' : int((w/2) - magic_number['w1']),
        'right' : None
    }
    pad['bottom'] = int(h - mask_h - pad['top'])
    pad['right'] = int(w - mask_w - pad['left'])
    
    # 元の画像サイズに戻す
    mask = cv2.copyMakeBorder(mask, pad['top'], pad['bottom'], pad['left'], pad['right'], cv2.BORDER_CONSTANT, (0))
    mask2 = mask

    # 1
    x,y,w,h = cv2.boundingRect(mask)
    img = cv2.rectangle(img,(x-10,y-10),(x+w+10,y+h+10),(255,0,0),2)
    cv2.imwrite('a.png', img)

    # 2
    contours, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key=cv2.contourArea)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    img = cv2.drawContours(img,[box],0,(0,0,255),2)
    cv2.imwrite('b.png', img)

    


if __name__ == '__main__':
    img = cv2.imread('./test.png', cv2.IMREAD_COLOR)
    boundingRect(img)