import requests
def run(file_name,operation):
    operations = ['getobject','ocr','getface']
    if operation not in operations:
        print("wrong operation, available operations are ['getobject','ocr','getface']")
    url = 'http://serveo.net:5557/ml/'+operation
    files = {'image': open(file_name, 'rb')}
    try:
        response = requests.post(url,files=files)
        print(response.text)
        return response.text
    except:
        print("No internet connection.")
        return("No internet connection.")

if __name__=="__main__":
    run('image.jpg','getobject')
