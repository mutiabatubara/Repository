import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path='Dataset'

def getImagesWithID(path):
    #membuat path folder agar bisa dipanggil folder data_wajah
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #membuat list wajah
    faceSamples=[]
    #membuat list id
    IDs=[]
    
    #buat perulangan untuk path folder citra_wajah beserta idnya
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        ID=int(os.path.split(imagePath)[-1].split(".")[1])
        faceSamples.append(imageNp)
        print ID
        IDs.append(ID)
        cv2.imshow("training",imageNp)
        cv2.waitKey(100)
    return faceSamples,IDs

#list wajah terisi dengan id sesuai indeks
faceSamples,Ids = getImagesWithID(path)
recognizer.train(faceSamples, np.array(Ids))
recognizer.save('Trainner/trainner.yml')
cv2.destroyAllWindows()
