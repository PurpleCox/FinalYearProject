import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time


def info():
    return ["Pi Camera Example", "pi", [("Run Cam Example", run_cam_example()), ("test", test())]]


def run_cam_example():

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 60
    raw = PiRGBArray(camera, size=(640, 480))

    window = cv2.namedWindow("camera")

    time.sleep(1)

    for frame in camera.capture_continuous(raw, format="bgr", use_video_port=True):
        image = frame.array
        height, width = image.shape[:2]
        M = cv2.getRotationMatrix2D((width / 2, height / 2), 180, 1)
        image_flipped = cv2.warpAffine(image, M, (width, height))

        cv2.imshow("camera", image_flipped)
        raw.truncate()
        raw.seek(0)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    camera.close()
    cv2.destroyAllWindows()


def test():
    print("test")
