import requests
def run(file_name):
    url = 'https://api.tosee.live/api/Messages/upload'

    files = {'file': open(file_name, 'rb')}

    try:
        response = requests.post(url,files=files)
        print(response.text)
        return response.text
    except:
        print("No internet connection.")
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/195px-No-Image-Placeholder.svg.png"
if __name__=="__main__":
    run('image.jpg')
    