#!/usr/bin/env python

""" Detecting faces with OpenCV

Usage: detect_faces.py [IMAGE]

If no image is specified, the script will assume face.jpg should be used.

"""

import sys

import cv2

def detect_face(image_path='face.jpg'):
    """Detect and hightlight faces in an image"""

    face_cascade_xml = \
      '/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_xml)

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 1)

    cv2.imshow('Faces (%d)' % len(faces), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        detect_face(sys.argv[1])
    else:
        detect_face()
