import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        cv2.putText(image, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        return True, barcodeData
    return False, ""
        

def start():

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        is_find, decode_data= decoder(frame)
        if is_find:
            cv2.destroyAllWindows()
            return decode_data
            
        
        cv2.imshow('Image', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break
        
