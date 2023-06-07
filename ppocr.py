from cnocr import CnOcr
ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3') #en_PP-OCRv3  densenet_lite_136-gru

def run(photo):
    res = ""
    out = ocr.ocr(photo)
    for line in out:
        print(line["text"])
        res += "\n" + line["text"]
    return "The photo cotains this text: "+res


if __name__=="__main__":
    run('9.jpg')
    #run()