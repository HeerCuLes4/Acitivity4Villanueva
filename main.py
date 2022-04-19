import cv2
filePath = 'hercules.jpg'
Bravery = int(1)
Image = cv2.imread(filePath,Bravery)
cv2.imshow("Muscle Man",Image)
cv2.waitKey(0)
cv2.destroyAllWindow()
