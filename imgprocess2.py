import cv2
import numpy as np


# ''' Image Arithmetic Operations '''

# rice = cv2.imread("./rice.tif")
# f16 = cv2.imread("./f16.tif")
# # cv2.imshow("rice",rice)
# # cv2.imshow("f16",f16)

# # add_1 = cv2.add(rice, f16)

# # cv2.addWeighted(scr1, weight1, scr2, weight2, dst)
# add_2 = cv2.addWeighted(rice, 0.7, f16, 0.3, 0)

# # cv2.imshow("add_1", add_1)
# cv2.imshow("add_2", add_2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


''' cv2.createTrackbar '''


def nothing(x):
    # print("hello")
    pass


rice = cv2.imread("./rice.tif")
f16 = cv2.imread("./f16.tif")

# build a black window
img = np.zeros((500, 500, 3), np.uint8)
# cv2.imshow("img", img)
# cv2.waitKey(0)

cv2.namedWindow('image')

# cv2.createTrackbar(trackbarName, WindowName, minimum of range, Maximum of range, callback function)
cv2.createTrackbar('Weight', 'image', 0, 100, nothing)


while(True):
    cv2.imshow('image', img)

    r = cv2.getTrackbarPos('Weight', 'image')  # get the value of trackbar
    r = float(r)/100.0
    # print("r: ", r)
    img = cv2.addWeighted(rice, r, f16, 1.0-r, 0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        # press q to stop
        break
