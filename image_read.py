import cv2
img = cv2.imread("image.jpg")
#gray = cv2.imread('logo.png',cv2.IMREAD_GRAYSCALE)
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
from matplotlib import pyplot as plt
print(newimg)
plt.imshow(newimg)
plt.show()

