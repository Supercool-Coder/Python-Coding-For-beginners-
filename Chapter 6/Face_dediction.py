import cv2
video = cv2.VideoCapture(0)
facedectect= cv2.CascadeClassifier(r'C:/Users/a/Pictures/Destop//GDPython/Face_Detection/haarcascad')
No_Mask=0
while True:
    ret, frame=video.read()
    faces= facedectect.detectMultiScale(frame,1.3,5)
    for(x,y,w,h) in faces:
        if No_Mask == './images/images/1':
            cv2.rectangle(frame, (x,y),(x+y,w+h),(0,128,0), 3)
        else:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,128,0), 3)
    cv2.imshow('image',frame)
    k=cv2.waitkey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()