from picamera import PiCamera
from time import sleep
import cv2

camera = PiCamera()
pics = 25
camera.resolution = (200, 200)
camera.start_preview()
for i in range(pics):
    camera.capture('/home/pi/Experiments/barrel_detection/dataset/white/image%s.jpg' % i)
    print('picture taken')
    sleep(2)
    
camera.stop_preview()
