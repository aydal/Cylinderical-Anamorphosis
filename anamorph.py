import math
from cv2 import * #saves us the need of using cv2. as a prefix everytie the library is used(which is alot)
import numpy as np


img=imread("images.jpeg")
f=img.copy()
(rows,cols)=f.shape[:2]
r=math.trunc(.25*rows) #offset-gives space to keep cylinder and height of the image from bottom
c=r+rows #this will be the decisive factor in size of output image-maximum radius of warped image
warp=np.zeros([c,2*c,3],dtype=np.uint8) 
warp.fill(0)

def convt(R,b):
	return (math.trunc((b*cols/(2*math.asin(1)))),math.trunc(c-R))
for i in range (0,2*c):
	for j in range (1,c):
		b=math.atan2(j,i-c)
		#print(b)
		R=math.sqrt(j*j+math.pow(i-c,2))
		if R>=r and R<=c:
			(q,p)=convt(R,b)
			warp[c-j,i-1]=f[p-1,q-1]
warp=blur(warp,(3,3))
imshow("orignal",img)
imshow("anamorphed",warp)
waitKey()
