import cv2
def take_pic(name="image.jpg"):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
    ret, frame = cap.read()
    #stretched_frame = cv2.resize(frame, (5000, 1440),
    #           interpolation = cv2.INTER_LINEAR)
    cv2.imwrite(name, frame)
    return name

if __name__=="__main__":
    take_pic()