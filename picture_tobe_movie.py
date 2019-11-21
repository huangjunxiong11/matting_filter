import cv2
import os
from config import out_path, bg_video_path, out_video


def make_phone_tobe_video(out_path=out_path, bg_video_path=bg_video_path, out_video=out_video):
    """
    将图片集合成视频
    :param out_path: 图片
    :param out_video: 合成的视频
    :param bg_video_path: 参考的视频
    :return: 无
    """
    cap = cv2.VideoCapture(bg_video_path)  # 根据这个视频的帧数和大小来生成视频
    fgs = int(cap.get(cv2.CAP_PROP_FPS))  # 得到参考视频的帧数，如fgs = 30
    size_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 得到参考视频的视频宽度
    size_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 得到参考视频的视频长度
    size = (size_width, size_height)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 表示输出的视频格式为.avi,opencv3.0使用
    video_writer = cv2.VideoWriter(out_video, fourcc, fgs, size)
    pictrue_in_filelist = os.listdir(out_path)

    for i in range(len(pictrue_in_filelist)):
        pictrue_in_filename = out_path + "/" + pictrue_in_filelist[i]
        img12 = cv2.imread(pictrue_in_filename)
        video_writer.write(img12)
    video_writer.release()

