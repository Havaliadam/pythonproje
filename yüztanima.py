import cv2
import face_recognition


imgyazilimci=face_recognition.load_image("resim/resim.png")
imgyazilimci=cv2.cvtColor(imgyazilimci,cv2.COLOR_BGR2RGB)
imgtest=face_recognition.load_image_file("resim/resim.png")
imgtest=cv2.cvtColor(imgyazilimci,cv2.COLOR_BGR2RGB)


faceLoc=face_recognition.face_locations(imgyazilimci)[0]
encodeyazilimci=face_recognition.face_encodings(imgyazilimci)[0]
cv2.rectangle(imgtest,(faceLoc[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

result=face_recognition.compare