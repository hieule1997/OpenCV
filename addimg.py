#Tìm hiểu một số phép toán số học trên các hình ảnh như cộng, trừ, hoạt động bitwise, v.v.
#Bạn sẽ học các hàm này: cv2.add () , cv2.addWeighted (), v.v.

import numpy as np
import cv2
from matplotlib import pyplot as plt
x = np.uint8([250])
y = np.uint8([10])
print (cv2.add(x,y))
print (x+y)
# ghep 2 anh vao thanh 1 
# luy uy cac hinh anh phai cung kich co
img1 = cv2.imread('image/DSCF1957.JPG')
img2 = cv2.imread('image/IMG_0031.JPG')
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dst = cv2.addWeighted(img1,0.8,img2_resized,0.2,0)
newimg = cv2.resize(dst,(int(700),int(450)))
cv2.imshow('ghep anh',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # Load two images
# img1 = cv2.imread('image/DSCF1957.JPG')
# img2 = cv2.imread('image/IMG_0031.JPG')

# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols ]

# # Now create a mask of logo and create its inverse mask also
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)

# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst
# newimg = cv2.resize(img1,(int(700),int(450)))
# cv2.imshow('res',newimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()