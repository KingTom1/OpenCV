import cv2 as cv
import numpy as np
def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]  # 色彩空间,三通道   blue green red
    print("width : %s ,height : %s, channels : %s"%(width, height , channels))
    # 遍历图片像素 并一一减少  像素取反
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixels_demo",image)
# 跟上面循环的作用一样  但是效率快50倍 底层C++写的
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)

# 改变像素,创造新图片
def create_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,2] = np.ones([400,400])*255
    cv.imshow("new image",img)



# 不能使用中文路径
src = cv.imread(r"D:\2.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
# 测量运算速度
t1 = cv.getTickCount()
inverse(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print("time : %s ms"%(time*1000))

cv.waitKey(0)
cv.destroyAllWindows()