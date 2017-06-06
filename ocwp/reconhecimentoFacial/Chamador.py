import cv2
from FaceDetec import Detector

class Main(object):

    arcCascade = 'haarcascade_frontalface_default.xml'
    facesCascade = cv2.CascadeClassifier(arcCascade)
    webCam = cv2.VideoCapture(0)


    detector = Detector(arcCascade,webCam, facesCascade)
    detector.comecaReconhecimentoFacial()

