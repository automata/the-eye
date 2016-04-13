import cv2
import time

directory = "/home/vilson/camshots/"

def shot(camera):
    _, im = camera.read()
    return im

def main(port=0, discard_frames=10):
    camera = cv2.VideoCapture(port)

    # Ramp some frames to give it time to white balance
    for frames in xrange(discard_frames):
        disrcarded = shot(camera)
    # Capture a frame
    captured = shot(camera)
    file_name = time.strftime("eye_%Y-%m-%d-%H%M%S.png")
    file_path = directory + file_name
    cv2.imwrite(file_path, captured)
    del(camera)

main(0, 10)
