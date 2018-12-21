import cv2


cap = cv2.VideoCapture(0) 
###pla();
##print("Capturing Image")
##while(True):
##    font = cv2.FONT_HERSHEY_SIMPLEX
##    ret,frame = cap.read()
##    cv2.imwrite('new.jpg',frame)
##
##    id="saran"
##    img1=frame
##    cv2.putText(img1,'Click Y to for your image',(20,50), font, 1.3,(0,255,0),2,cv2.LINE_AA)
##
##    cv2.imshow('img1',img1) 
##    if (0xFF == ord('y')): #save on pressing 'y' 
##        cv2.imwrite('new.jpg',frame1)
##        cv2.imshow('frame1',frame1);
##        cv2.destroyAllWindows()
##        break
##
##cap.release()
while(True):
    font = cv2.FONT_HERSHEY_SIMPLEX
    ret,frame = cap.read() 
    id="saran"
    img=frame
    cv2.putText(img,'Click Y to for your image',(20,50), font, 1.3,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('img1',img) 
    if (cv2.waitKey(1) & 0xFF == ord('y')): #save on pressing 'y' 
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                           
        cv2.imwrite('new.jpg',gray_image)
        cv2.imshow('frame1',gray_image);
        cv2.destroyAllWindows()
        break
cap.release()
