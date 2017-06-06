import cv2

class Detector(object):


    def __init__(self, cascade, webCam, facesCascade):
        print 'chamou init'
        self.arqCascade = cascade
        self.webCam = webCam
        self.facesCascade = facesCascade



    def comecaReconhecimentoFacial(self):
        while True :
            print 'Reconhecendo ...'
            s, imagem = self.webCam.read()
            imagem = cv2.flip(imagem, 180)

            rostos = self.facesCascade.detectMultiScale(
                imagem,
                minNeighbors=5,
                minSize=(30, 30),
            maxSize=(200,200)
            )

            for (x, y, w, h) in rostos :
                cv2.rectangle(imagem, (x,y), (x + w, y +h),(0, 255, 0),2)

            cv2.imshow('Reconhecedor de faces, v 1.0', imagem)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.webCam.release()
        cv2.destroyAllWindows()