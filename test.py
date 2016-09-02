import cv2
import numpy as np
cap = cv2.VideoCapture("./out.mp4")
while not cap.isOpened():
    cap = cv2.VideoCapture("./out.mp4")
    cv2.waitKey(1000)
    print "Wait for the header"

pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
orig = np.zeros((360,638),np.uint8)
while True:
    flag, frame = cap.read()
    print frame.shape
    if flag:
        # The frame is ready and already captured
        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY);
        print pos_frame
        if pos_frame == 1.0:
            print "hoge"
            orig = frame_gray;
        cv2.imshow('video',cv2.absdiff(orig,frame_gray))
        print str(pos_frame)+" frames"
    else:
        # The next frame is not ready, so we try to read it again
        cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
        print "frame is not ready"
        # It is better to wait for a while for the next frame to be ready
        cv2.waitKey(1000)

    if cv2.waitKey(10) == 27:
        break
    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
        # If the number of captured frames is equal to the total number of frames,
        # we stop
        break
