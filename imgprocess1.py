import cv2
from matplotlib import pyplot as plt

#####       1: read image       #####
# img = cv2.imread("")
img = cv2.imread("./lena.png")
cv2.imshow("img", img)
# cv2.waitKey(0)
cv2.waitKey(1000)

plt.figure()
plt.imshow(img)
plt.show()


#####     2: compare cv2.imread with plt.imshow       #####
# lena = cv2.imread("./lena.png")
# plt.figure()
# plt.imshow(lena), plt.title("Lena"), plt.xticks([]), plt.yticks([])
# plt.show()
# cv2.waitKey(0)  # move cv2.waitKey(0) in #1 to here
# print(lena[52, 324])


#####       3: image with colour        #####
# it will read image with colour as the default type
ox = cv2.imread("./ox.jpg")
ox_bgr = cv2.cvtColor(ox, cv2.COLOR_RGB2BGR)  # convert the type of colour
cv2.imshow("ox", ox)

plt.figure()
# plt.imshow(ox), plt.title("ox")
plt.imshow(ox_bgr), plt.title("ox")  # convert the type of colour
plt.show()
cv2.waitKey(0)


#####       4: How to put ox's horn to its face ?       #####
# it will read image with colour as the default type
ox = cv2.imread("./ox.jpg")
ox_bgr = cv2.cvtColor(ox, cv2.COLOR_RGB2BGR)  # convert the type of colour
horn = ox_bgr[48: 86, 221: 243]
plt.figure()
# plt.imshow(horn)
ox_bgr[95:133, 255:277] = horn
plt.imshow(ox_bgr), plt.title("ox")  # convert the type of colour
plt.show()
