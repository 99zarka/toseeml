import os

def speak(text_val="test",lang="en"):
    if lang.lower()=="en":
        os.system(f'pico2wave -w=test.wav "{text_val}"')
        os.system("aplay test.wav")
    elif lang.lower()=="ar":
        import mishkal.tashkeel
        text_val = mishkal.tashkeel.TashkeelClass().tashkeel(text_val)
        os.system(f'echo "{text_val}" | festival --tts --language arabic')
    else:
        text_val = "This language is not supported"
        os.system(f'pico2wave -w=test.wav "{text_val}"')
        os.system("aplay test.wav")
if __name__=="__main__":
    speak("Hello darkness my old friend? Hello darkness my old friend? Hello darkness my old friend? ")
    speak("السلام عليكم كيف احوالكم وكيف اخباركم","ar")
    speak("Hello darkness","ar")









