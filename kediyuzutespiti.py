import cv2
import os

files = os.listdir()
print(files)


img_path = []

for f in files:
    if f.startswith("kedi"):
        img_path.append(f)

print(img_path)

cf = cv2.CascadeClassifier('C:\Users\Dogan\Pygame\pythonProject2\.venv\ nesne tespiti\haarcascade_frontaldogface.xml')

for i in img_path:
    img = cv2.imread(i)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rect = cf.detectMultiScale(gray_img, scaleFactor = 1.03, minNeighbors= 2)

    for (j,(x,y,w,h)) in enumerate(rect):
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow(i, img)

    if cv2.waitKey(0) & 0xFF == ord('g'): continue



