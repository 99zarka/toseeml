from take_pic import take_pic
import detect_objects
import recognizefaces
import ocr
from speak import speak
import pytes_ocr

while True:
    choice = input("1- object detection\t2- face recognition\t3- OCR: ")
    output = ""
    if choice == '1':
        output = detect_objects.run(take_pic())
    elif choice == '2':
        output = recognizefaces.run(take_pic())
    elif choice == '3':
        output = ocr.run(take_pic())
    elif choice == '4':
        output = pytes_ocr.run(take_pic())
    else:
        print("enter a valid option.")
    speak(output)
