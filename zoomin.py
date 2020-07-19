import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./dustmite0.jpg', cv2.IMREAD_GRAYSCALE)
img2 = img[200:500, 500:700]

plt.figure()
plt.subplot(221), plt.imshow(img, cmap="gray")
plt.subplot(222), plt.imshow(img2, cmap="gray")
# plt.subplot(222) means cutting the whole figure into 2(row), 2(column)
# and select number 2 position for the following plt.imshow
# in this case, img2 will be shown in postion 2
plt.show()


# the name of path should be like this (including the extension)
img = cv2.imread('./dustmite0.jpg', cv2.IMREAD_GRAYSCALE)

# the function of line 8,9 are to resize the picture
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800, 600)

cv2.imshow('image', img)
cv2.waitKey(0)
# 0 means wait until you press a button
# 10 means 10 microsecond
cv2.destroyAllWindows()
