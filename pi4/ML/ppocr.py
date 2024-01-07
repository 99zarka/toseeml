from cnocr import CnOcr
from take_pic import take_pic
ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3') #en_PP-OCRv3  densenet_lite_136-gru

def run(photo = take_pic()):
    res = ""
    out = ocr.ocr(photo)
    for line in out:
        print(line["text"])
        res += "\n" + line["text"]
    print(res)
    if res.strip() == "":
        print("Couldn't recognize any text.")
        return "Couldn't recognize any text."
    return "The photo cotains this text: "+res


if __name__=="__main__":
    #run('image.jpg')
    run()