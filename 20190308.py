import cv2 as cv
# 不能使用中文路径
# src = cv.imread(r"D:\2.PNG")
src = cv.imread(r'D:\456.png')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
cv.waitKey(0)
cv.destroyAllWindows()
