import cv2

cap = cv2.VideoCapture("Bike_Detector/Sample/two_wheeler2.mp4")

bike_cascade = cv2.CascadeClassifier("Bike_Detector/Classifier/two_wheeler.xml")

#แสดงผลวีดีโอ
while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        #จำแนกใบหน้า
        scaleFactor = 1.1
        minNeighbor = 1
        bike_detect = bike_cascade.detectMultiScale(gray_img,scaleFactor,minNeighbor)
        #แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in bike_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)

        cv2.imshow("Output",frame)
        if cv2.waitKey(12) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()