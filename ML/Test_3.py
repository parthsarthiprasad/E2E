from Predictor import Pred
import cv2
import numpy as np

vid = cv2.VideoCapture(0)
predictor = Pred()

while True:
    ret,frame = vid.read()
    cv2.imshow("Original",frame)
    new_frame = predictor.get_pred(frame)
    cv2.imshow("Predicted", new_frame)
    if(cv2.waitKey(1)==27):
        break

vid.release()
cv2.destroyAllWindows()
    