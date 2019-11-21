import cv2
import numpy as np
import os
from config import *
from filter import filter


def hjx_matting(foreground_path=foreground_path,
                background_path=background_path,
                out_path=out_path,
                fg_fx=fg_fx,
                fg_fy=fg_fy,
                center_x=center_x,
                center_y=center_y,
                bg_fx=bg_fx,
                bg_fy=bg_fy,
                median_blur=median_blur,
                filter_name=filter_name):
    """进行图片抠图、合成操作"""
    foreground_path = foreground_path
    background_path = background_path
    fg_filelist = os.listdir(foreground_path)
    bg_filelist = os.listdir(background_path)
    filter_ = cv2.imread(filter_name)
    import shutil
    try:
        shutil.rmtree(out_path)
    except OSError:
        pass
    os.mkdir(out_path)
    for i in range(len(fg_filelist)):
        fb_filename = foreground_path + "/" + fg_filelist[i]
        bg_filename = background_path + "/" + bg_filelist[i]

        # 运行流程日记
        print("%d-%d" % ((i + 1), len(fg_filelist)))

        # 设置前景人物图片大小
        fg_img = cv2.imread(fb_filename)
        fg_img = cv2.resize(fg_img, None, fx=fg_fx, fy=fg_fy)

        # 设置背景图片大小
        bg_img = cv2.imread(bg_filename)
        bg_img = cv2.resize(bg_img, None, fx=bg_fx, fy=bg_fy)

        # 提取mask
        rows, cols, channels = fg_img.shape  # 将展示图片大小的尺寸和通道数重新赋值给原来的值
        hsv = cv2.cvtColor(fg_img, cv2.COLOR_BGR2HSV)  # 转换图片颜色空间
        lower_blue = np.array([lower, 43, 46])  # 新建一个列表数组，为HSV绿色下限
        upper_blue = np.array([upper, 255, 255])  # 新建一个列表数组，为HSV绿色上限
        mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 将hsv格式图片进行阈值处理变成gray格式图片

        # 对mask进行加工处理
        median = cv2.medianBlur(mask, median_blur)  # 进行中值滤波消除边缘锯齿
        erode = cv2.erode(median, None, iterations=erode_iter)  # 腐蚀，消除黑噪点
        dilate = cv2.dilate(erode, None, iterations=dilate_iter)  # 膨胀，消除白噪点
        mask = 255 - dilate

        # 定义前景人物图片在背景图片中的位置
        center = [center_x, center_y]

        # todo 使用cv2的掩码进行合成，每张1080x1920图片提高速度1秒，本来3.4秒现在只需2.38秒
        roi = bg_img[center[0]:center[0] + rows, center[1]:center[1] + cols]  # 在背景上面找到放置的区域
        img1_bg = cv2.bitwise_and(fg_img, fg_img, mask=mask)
        img2_fg = cv2.bitwise_and(roi, roi, mask=dilate)  # 通过掩码将白色的地方盖掉，黑色的地方显示出来
        dst_ = cv2.add(img1_bg, img2_fg)
        bg_img[center[0]:center[0] + rows, center[1]:center[1] + cols] = dst_
        dst = filter(bg_img, filter_)  # 进行滤镜操作
        save_name = out_path + '/' + (str(i)).zfill(4) + '.jpg'
        cv2.imwrite(save_name, dst)
        # break


# if __name__ == '__main__':
#     import time
#     start = time.clock()
#     hjx_matting()
#     end = time.clock()
#     print('Running time: %s Seconds' % (end - start))
