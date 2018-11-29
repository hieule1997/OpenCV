import numpy as np
import cv2
from matplotlib import pyplot as plt
# Load an color image in grayscale
img = cv2.imread('image/DSCF1957.JPG')
name = "hinh anh"


# b,g,r = cv2.split(img)
# img = cv2.merge((r,g,b))
# # tao border khung vien cho anh 
# # Co cac border la BORDER_REPLICATE , BORDER_REPLICATE ,BORDER_REFLECT_101, BORDER_WRAP,BORDER_CONSTANT
# replicate = cv2.copyMakeBorder(img,400,400,400,400,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img,400,400,400,400,cv2.BORDER_REPLICATE)
# reflect101 = cv2.copyMakeBorder(img,400,400,400,400,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img,400,400,400,400,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img,400,400,400,400,cv2.BORDER_CONSTANT)

# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
# # Thay doi hinh anh theo mau cho truoc  
# ball = img[1736:2919, 2044:10090]
# img[236:1419, 544:1590] = ball

# b,g,r = cv2.split(img)
# img = cv2.merge((r,g,b)) # chinh mau theo RGB
# # img[:,:,2] = 0  # chinh mau all theo 0,1,2


# print(img.shape) # chi ra so hang cot va kenh
# print(img.size) # chi ra kich thuoc dung luong anh
# print(img.dtype) # chi ra loai hinh anh

# # chuyen doi mau cua 1 pixel
# img.item(10,10,2) # lay ra mau cua pixel
# print (img.item(10,10,2))
# img.itemset((10,10,2),100) # thay doi mau pixel
# img.item(10,10,2) 
# print(img.item(10,10,2))

# px = img[100,100] # lay ra mau BGR cua hinh anh tai toa do (100,100)
# print (px) # in ra man hinh mau cua toa do 
# blue = img[100,100,0] # Lay ra mau xanh cua toa do voi tham so (100,100,0) mau xanh la (100,100,1) , mau do (100,100,2)
# print (blue)

# # Chuyen doi rgb  
# b,g,r = cv2.split(img)
# img2 = cv2.merge([r,g,b])
# plt.subplot(121);plt.imshow(img) 
# plt.subplot(122);plt.imshow(img2)
# plt.show()


# thay doi kich thuoc hien thi
# newimg = cv2.resize(img,(int(1300),int(650)))
# cv2.imshow(name,newimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # Hien thi tho matplotlib 
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
