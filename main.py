import cv2 as cv

camera = cv.VideoCapture(0)

if camera.isOpened():
    fps = camera.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    fourCC = cv.VideoWriter_fourcc(*'mp4v')
    width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))
    video = cv.VideoWriter('sample.mp4', fourCC, fps, (width, height))
    isRecord = False
    isFilter = False
    img_prev = cv.createBackgroundSubtractorMOG2()

    while True:
        valid, img = camera.read()
        if not valid:
            break

        if isFilter:
            img = cv.bitwise_not(img)

        if isRecord:
            cv.rectangle(img, (5, 5), (width - 5, height - 5), color=(0, 0, 255) ,thickness=3)
            cv.circle(img, (30, 40), radius=10, color=(0, 0, 255), thickness=-1)
            cv.putText(img, 'REC', (45 , 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=3)
            video.write(img)

        cv.imshow('camera', img)

        key = cv.waitKey(wait_msec)
        if key == 27:
            break
        elif key == ord(' '):
            isRecord = not isRecord
        elif key == ord('\t'):
            isFilter = not isFilter

    video.release()
    camera.release()
    cv.destroyAllWindows()
