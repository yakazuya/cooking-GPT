from ultralytics import YOLO

def yolo(img_path:str) -> list:
    model = YOLO('../model/best.pt')
    # model("sample.png",save=True, conf=0.2, iou=0.5)
    model.conf = 0.5
    results = model(img_path,save=True, iou=0.5)
    names = results[0].names
    classes = results[0].boxes.cls
    names= [ names[int(cls)] for cls in classes] 
    vegetables_list=[]
    for value in names.values():
        vegetables_list.append(value)
    return vegetables_list

def main():
    img_path:str = '../uploads/test.jpg'
    yolo(img_path)

if __name__ == "__main__":
    main()