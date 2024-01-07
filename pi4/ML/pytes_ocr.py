import pytesseract
from PIL import Image
from take_pic import take_pic

def run(photo = take_pic()):
    result = pytesseract.image_to_string(Image.open(photo))
    print(result)
    return result

if __name__=="__main__":
    run()