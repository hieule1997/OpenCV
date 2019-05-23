import numpy as np
import cv2
from matplotlib import pyplot as plt

# Tao khoi mau den kich thuoc 512,512
img = np.zeros((1024,512,3), np.uint8)

cv2.line(img,(225,0),(511,511),(225,50,0),50) # line(anh, toado A, toado B , mauRGB,kich thuoc line)

cv2.rectangle(img,(204,20),(510,128),(0,255,0),3)# hinh chu nhat(hinh, toa do A, toa do C, mayRGB , kich thuoc vien)

cv2.circle(img,(447,63), 63, (0,0,255), 1) # circle(anh, toa do tam,ban kinh,mau,kich thuoc vien )

cv2.ellipse(img,(256,256),(200,50),0,1,180,255,-1) #eclip (anh,toa do tam,{chieu dai, chieu rong}, do nghieng,toa do bat dau.toa do ket thuc,mauRBG, do mau vieen )

# # Tao ra da giac voi cac toa do nhu trong hinh
# pts = np.array([[10,5],[20,30],[70,20],[50,10],[90,50],[102,1020]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,255,255))

# # Toa chu viet 

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'Minh Hieu',(10,500), font, 5,(255,255,255),3,cv2.LINE_AA) # diem bat dau (10,500) ,font , co chu, mau chu ,kich thuoc mau chu, kieu chu

plt.imshow(img)
plt.show()