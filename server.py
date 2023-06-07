from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import os
import random
import ppocr
import detect_objects
import recognizefaces

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/' , methods=['GET'])
def home():
    return "The server is up and running."

operations =['ocr','getface','getobject']

@app.route('/ml/<operation>' , methods=['POST'])
def analyze_image(operation):
    if operation not in operations:
        return "This end point doesn't exist", 400
    
    if 'image' not in request.files:
        return 'No image file found', 400

    image = request.files['image']

    if image.filename == '':
        return 'No selected image file', 400

    if image:
        filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999)) + '.jpg'
        image.save(filename)

        res = ''
        if operation == 'ocr':
            res = ppocr.run(filename)
        elif operation == 'getface':
            res = recognizefaces.run(filename)
        elif operation == 'getobject':
            res = detect_objects.run(filename)

        os.remove(filename)
        return res, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 5557)