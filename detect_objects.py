from ultralytics import YOLO
model = YOLO("yolov8x")

def run(picture=0):
    res = model.predict(source=picture ,conf=0.5,save_txt=True,show=False ,save=False)

    get_label = res[0].names
    res = res[0].boxes.cls.tolist()
    res = list(map(lambda x:int(x),res))
    from collections import Counter
    res = Counter(res)
    res2 = "The picture contains: "
    if not res:
        res2 = "Can't recognize familier objects"
    for item in res:
        res2 += str(res[item])+" "+get_label[item]
        if res[item]>1:
            res2 += "s"
        res2 +=", "
    res2 = res2[:-2]+"."
    if not res:
        res2 = "Can't recognize familier objects"
    print(res2)
    return res2

if __name__=="__main__":
    run('dog.jpg')
    #run()