import numpy as np



def filter(img, map):
    """
    对图片img进行滤镜map操作
    :param img: 原图片数组
    :param map: 滤镜色卡数组
    :return:滤镜处理之后的图片数组
    """
    rows, cols = img.shape[:2]
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    b = img[:, :, 0]
    g = img[:, :, 1]
    r = img[:, :, 2]

    r = r.astype(np.int16)
    g = g.astype(np.int16)
    b = b.astype(np.int16)

    x = (g // 4) + (b // 32) * 64
    y = (r // 4) + ((b % 32) // 4) * 64
    for i in range(rows):
        for j in range(cols):
            dst[i][j] = map[x[i][j]][y[i][j]]
    return dst


# if __name__ == '__main__':
#     import time
#     import cv2
#     img = cv2.imread("data/my_ori/original.jpg", 1)
#     map = cv2.imread("data/new/5.png")
#
#     start = time.clock()
#     dst = filter(img, map)
#     end = time.clock()
#     print('Running time: %s Seconds' % (end - start))
#     cv2.imwrite("data/my_new/dst7.jpg", dst)
