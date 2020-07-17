import numpy as np
import cv2

'''
    You have the change the below path that you want to save images 
'''
path_lena_bitplane = "./lena-bitplane-quiz.png"
path_results = "./Results/"  # you have to make a folder first


img = cv2.imread(path_lena_bitplane, cv2.IMREAD_GRAYSCALE)
print("The shape of img: {}".format(img.shape))
row, col = img.shape  # shape of the image would be [512,512]


def intToBitArray(img):
    binray_value = []
    for i in range(row):
        for j in range(col):
            binray_value.append(np.binary_repr(img[i][j], width=8))
    return binray_value


def bitplane(bitImgVal, img1D):

    bitList = [np.uint8(i[bitImgVal]) for i in img1D]

    return bitList


imgIn1D = intToBitArray(img)  # binary value in width - 8
imgIn2D = np.reshape(imgIn1D, (512, 512))
print(
    "Number one element in the list of binary number: '{}'".format(imgIn1D[0]))

# Multiply the bitplane by 255 to make it brighter
# b8 would be the high frerquency of the image which is the edge of the object
eight = np.array(bitplane(0, imgIn1D)) * 255
eight = np.reshape(eight, (row, col))
cv2.imwrite(path_results + "8bitvalue.png", eight)
# cv2.imshow("eight",eight)

seven = np.array(bitplane(1, imgIn1D)) * 255
seven = np.reshape(seven, (row, col))
cv2.imwrite(path_results + "7bitvalue.png", seven)
# cv2.imshow("seven",seven)

six = np.array(bitplane(2, imgIn1D)) * 255
six = np.reshape(six, (row, col))
cv2.imwrite(path_results + "6bitvalue.png", six)
# cv2.imshow("six",six)

five = np.array(bitplane(3, imgIn1D)) * 255
five = np.reshape(five, (row, col))
cv2.imwrite(path_results + "5bitvalue.png", five)
# cv2.imshow("five",five)


four = np.array(bitplane(4, imgIn1D)) * 255
four = np.reshape(four, (row, col))
cv2.imwrite(path_results + "4bitvalue.png", four)
# cv2.imshow("four",four)


three = np.array(bitplane(5, imgIn1D)) * 255
three = np.reshape(three, (row, col))
cv2.imwrite(path_results + "3bitvalue.png", three)
# cv2.imshow("three",three)


two = np.array(bitplane(6, imgIn1D)) * 255
two = np.reshape(two, (row, col))
cv2.imwrite(path_results + "2bitvalue.png", two)
# cv2.imshow("two",two)


one = np.array(bitplane(7, imgIn1D)) * 255
one = np.reshape(one, (row, col))
cv2.imwrite(path_results + "1bitvalue.png", one)
# cv2.imshow("one",one)

# save combined plane image
combine = eight/2 + seven/4 + six/8 + five / \
    16 + four/32 + three/64 + two/128 + one/256
comb = np.reshape(combine, (row, col))
cv2.imwrite(path_results + "comb.png", comb)
# comb = np.uint8(comb)
# cv2.imshow("comb",comb)
# cv2.waitKey(0)
