import cv2
import tensorflow as tf
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder

print("starting...")

train_loc = "DataSet"
train_data = tf.keras.preprocessing.image.ImageDataGenerator(horizontal_flip=(True),rescale=(1/255.0),).flow_from_directory(train_loc,batch_size=25,subset=("training"),target_size=(224,224),shuffle=(False))
classes=list(train_data.class_indices.keys())

le = LabelEncoder()
le.fit(classes)
labels = le.classes_

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print("Loading model...")
model = load_model("model-cnn-facerecognition.h5")
print("[INFO] finish load model...")

def run(photo):
    final_result = []
    frame = cv2.imread(photo, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        
        face_img = gray[y:y+h, x:x+w]
        face_img = cv2.resize(face_img, (128, 128))
        face_img = face_img.reshape(1, 128, 128, 1)
        
        result = model.predict(face_img)
        idx = result.argmax(axis=1)
        confidence = result.max(axis=1)*100
        if confidence > 90:
            label_text = "%s (%.2f %%)" % (labels[idx], confidence)
            print(labels[idx])
            final_result.append(str(labels[idx][0]))
        else :
            label_text = "N/A"
        labels[idx]
        
        #cv2.imshow('Detect Face', frame)
    res = ""
    if final_result:
        res = "This picture contains the faces of: "
        for face in final_result:
            res += face+", "
    else:
        res = "Couldn't recognize any familiar faces."
    print(res)
    return res

if __name__=="__main__":
    run("z.jpg")
    #run()