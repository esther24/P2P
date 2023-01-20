import torch
import numpy as np
print(torch.cuda.is_available())

model = torch.hub.load('ultralytics/yolov5', 'custom', path='"C:\\Users\\Dell\\Desktop\\SEM 6 mini_project\\cuda_yolov5\\yolov5\\runs\\train\\exp\\weights\\best.pt"', force_reload=True)


import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()