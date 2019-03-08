import cv2 as cv
import numpy as np

def video_demo():
    # VideoCapture 是打开摄像头   0表示第一个摄像头  如果有3个 可以一一打开  视频路径放在这里也能打开  视频没有声音
    capture = cv.VideoCapture(0)
    while(True):
        ret ,frame = capture.read()
        # 调整视频显示方向
        frame= cv.flip(frame,1)
        cv.imshow("video",frame)
        # 50帧比较流畅
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

# 不能使用中文路径
src = cv.imread(r"D:\2.PNG")
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)
cv.imshow("image",src)
# 获取图片信息
# get_image_info(src)
# 获取视频信息
# video_demo()
# 图片序列化写入
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imwrite(r"D:\1.JPG",gray)

cv.waitKey(0)
cv.destroyAllWindows()