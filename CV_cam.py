import cv2

cap=cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    (w,h,c) = frame.shape
    centerH=h/2
    centerW=w/2
    centerH=int(centerH)
    centerW=int(centerW)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.line(frame,(centerH-20,centerW),(centerH+20,centerW),(0,255,0),2)
    gray = cv2.line(frame,(centerH,centerW-20),(centerH,centerW+20),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # org 
    org = (50, 50) 
    
    # fontScale 
    fontScale = 1
    
    # Blue color in BGR 
    color = (255, 0, 0) 
    
    # Line thickness of 2 px 
    thickness = 2
    
    # Using cv2.putText() method 
    grey = cv2.putText(frame, 'OpenCV', org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()