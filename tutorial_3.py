import cv2 as cv
import numpy as np

# 视频内容识别 捕捉某一指点颜色区域
def extrace_object_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_RGB2HSV)
        lower_hsv =np.array([37,43,46])
        upper_hsv =np.array([77,255,255])
        # 颜色对象提取  inRange
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c = cv.waitKey(40)
        if c == 27:
            break

def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb",Ycrcb)
    # 无法转回去
    input = cv.cvtColor(yuv,cv.COLOR_BGR2RGB)
    cv.imshow("input",input)


# 不能使用中文路径
src = cv.imread(r"‪D:\456.png")
src = cv.imread(r'D:\456.png')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
# 视频颜色分别
# extrace_object_demo()

# 三色通道分离
b, g, r = cv.split(src)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
# 三色通道的合并
src[:,:,1] = 255
# src = cv.merge([b,g,r])

cv.imshow("changed image",src)

cv.waitKey(0)
cv.destroyAllWindows()