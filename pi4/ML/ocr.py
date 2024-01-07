from ppocronnx.predict_system import TextSystem
from take_pic import take_pic
import cv2

text_sys = TextSystem()

def run(photo = take_pic()):
    img = cv2.imread(photo)
    res = text_sys.detect_and_ocr(img)
    res2=""
    for boxed_result in res:
        res2+=boxed_result.ocr_text.strip()+"\n"
    print(res2)
    return res2

if __name__=="__main__":
    run("9.jpg")
