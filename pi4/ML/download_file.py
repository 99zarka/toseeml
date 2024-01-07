import requests
import soundfile as sf
import os
def run(url,name='new_voice_note.ogg'):
    try:
        response = requests.get(url)
    except:
        return
    if response.status_code == 200:
        with open(name, "wb") as f:
            f.write(response.content)
        print("Photo downloaded successfully!")
        
        import pydub
        audio_file = pydub.AudioSegment.from_file(name)
        audio_file.export("new_voice_note.wav", format="wav")
        os.system("aplay new_voice_note.wav")

    else:
        print("Error downloading photo.")
if __name__=="__main__":
    run('https://res.cloudinary.com/dghg2pc4g/video/upload/v1686883244/da-net7/luez6er01uzubja5zcwc.webm')