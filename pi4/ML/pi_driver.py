import setupgpio
import time
from take_pic import take_pic
import record_voice_note
import detect_objects
import recognizefaces
import ppocr
from speak import speak
import upload_file_ml
import chat

speak("The smart glasses are ready")

buffer=['']*12

def are_all_elements_equal(my_list):
    for i in range(len(my_list)-1):
        if my_list[i]!=my_list[i+1]:
            return False
    return True

while True:
    state = setupgpio.get_joystick_state()
    buffer.append(state)
    oldest_state = buffer[0]
    del buffer[0]
    print(buffer)

    output = ""

    if are_all_elements_equal(buffer[-3:-1]) and buffer[-1] != buffer[-2] and buffer[-2] and not are_all_elements_equal(buffer[:-1]):
        state = buffer[-2]
        print()
        print("short click detected:",state)
        print()
        if state == "pressed":
            print("Performing object detection:")
            speak("Performing object detection:")
            output = detect_objects.run(take_pic())
        if state == "back and down":
            print("Performing object detection on the cloud:")
            speak("Performing object detection on the cloud:")
            output = upload_file_ml.run(take_pic(),"getobject")
        if state == "back":
            print("Performing face recognition:")
            speak("Performing face recognition:")
            output = recognizefaces.run(take_pic())
        if state == "down":
            print("Performing OCR:")
            speak("Performing OCR:")
            output = ppocr.run(take_pic())

        speak(output)

    if are_all_elements_equal(buffer) and state and oldest_state != state:
        print()
        print("long click detected:",state)
        print()
        if state == "pressed":
            print("recording...")
            speak("recording")
            chat.send_file(record_voice_note.run())
        if state == "back and down":
            print("Performing face recognition on the cloud:")
            speak("Performing face recognition on the cloud:")
            output = upload_file_ml.run(take_pic(),"getface")
        if state == "back":
            print("sending picture to your friend:")
            speak("sending picture to your friend:")
            chat.send_file(take_pic())
        if state == "down":
            print("Performing OCR on the cloud:")
            speak("Performing OCR on the cloud:")
            output = upload_file_ml.run(take_pic(),"ocr")

        speak(output)

    time.sleep(0.1)