import logging
import time
from signalrcore.hub_connection_builder import HubConnectionBuilder
from signalrcore.protocol.messagepack_protocol import MessagePackHubProtocol
import requests
from speak import speak
from take_pic import take_pic
from langdetect import detect
import download_file
import upload_file
import subprocess
subprocess.Popen("python3 update_location.py", shell=True)

hub_url = "https://api.tosee.live/hubs/message"
other_username = "zarka2040"
token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJuYW1laWQiOiI3IiwidW5pcXVlX25hbWUiOiJ6YXJrYTIwMzAiLCJyb2xlIjoiTWVtYmVyIiwibmJmIjoxNjg2NjUwMDgwLCJleHAiOjE2ODkyNDIwODAsImlhdCI6MTY4NjY1MDA4MH0.gfQgM8YZlr_mFOXogWnGkaUlQAWw5DfAVicHFiCn-7iibIiQ8cyXG1UgrUaqm3qk0CKePtYgNhJfkiOJBEPQiA"

headers = {
    "Authorization": f"Bearer {token}"
}



def on_new_message(message):
    print("New message:", message)
    print("content: ",message[0]['content'])
    if message[0]['senderUsername'] == other_username and message[0]['content']:
        intro = "\n\nYou've got a new message from " + message[0]['senderUsername'] + ". It says: "
        res = message[0]['content']+"\n\n"
        print(intro,res)
        speak(intro)
        lang = detect(message[0]['content'])
        if lang == "ar":
            speak(res,lang)
        else:
            speak(res)
    if message[0]['senderUsername'] == other_username and message[0]['content']=="/send image":
        send_file(take_pic())

            
    if message[0]['senderUsername'] == other_username and message[0]['fileUrl']:
        print("You've got a new Voice note from " + message[0]['senderUsername'] + ". It says: ")
        speak("You've got a new Voice note from " + message[0]['senderUsername'] + ". It says: ")
        download_file.run(message[0]['fileUrl'])


try:
    hub_connection = HubConnectionBuilder().with_url(hub_url + "?user=" + other_username, options={"headers": headers})\
        .configure_logging(logging.INFO)\
        .with_automatic_reconnect({
            "type": "raw",
            "keep_alive_interval": 10,
            "reconnect_interval": 5,
            "max_attempts": 5
        }).build()
    hub_connection.on("NewMessage", on_new_message)

    hub_connection.start()
except:
    print("no internet connection.")

def send_file(file_name = take_pic()):
    create_message_dto = {
            "RecipientUsername": other_username,
            "Content": "",
            "File":upload_file.run(file_name)
        }
    try:
        hub_connection.send("SendMessage", [create_message_dto])
    except:
        print("no internet connection.")
#hub_connection.stop()
if __name__=="__main__":
    send_file()