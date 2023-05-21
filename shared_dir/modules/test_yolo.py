from ultralytics import YOLO

def yolo(img_path:str) -> list:
    model = YOLO('../model/best.pt')
    # model("sample.png",save=True, conf=0.2, iou=0.5)
    model.conf = 0.5
    results = model(img_path,save=True, iou=0.5)
    names = results[0].names
    vegetables_list=[]
    for value in names.values():
#         if results[1] > 0.9:
#             if value == 'poteto':
#                 value = 'potato'
        vegetables_list.append(value)
    # print(vegetables_list)
    return vegetables_list

def main():
    img_path:str = '../uploads/test.jpg'
    yolo(img_path)

if __name__ == "__main__":
    main()