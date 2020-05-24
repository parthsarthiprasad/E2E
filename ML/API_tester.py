import cv2
from pred_lib import Predictor

predict = Predictor()

vid = cv2.VideoCapture(0)

while True:
    ret,frame = vid.read()
    if(not(ret)):
        break
    new_frame = predict.get_pred(frame)
    if(type(new_frame)==int):
        continue
    cv2.imshow("Original",frame)
    cv2.imshow("New",new_frame)
    if(cv2.waitKey(1)==27):
        break
cv2.destroyAllWindows()
vid.release()
    