import cv2
from cvzone.FaceDetectionModule import FaceDetector

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
detector = FaceDetector(minDetectionCon=0.5)


while True:
    _,img = video.read()
    img,bboxes = detector.findFaces(img,draw=False)
    img2 = img.copy()
    if bboxes:
        for bbox in bboxes:
            x,y,w,h = bbox['bbox']
            rec = img[y:y+h,x:x+w]
            # cv2.imshow('Face',rec)
            recBlur = cv2.blur(rec,(30,30))
            # cv2.imshow('Face', recBlur)
            img2[y:y+h,x:x+w] = recBlur


    cv2.imshow('IMG',img)
    cv2.imshow('IMG2', img2)
    cv2.waitKey(1)