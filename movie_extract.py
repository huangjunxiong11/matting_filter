from config import fg_video_path, foreground_path, background_path, bg_video_path
import cv2
EXTRACT_FREQUENCY = 1  # 初始化配置，视频提取帧提取频率


def extract_frames(videopath, dst_folder, index):
    """
    将视频以一定的速率提取为图片
    :param videopath: 视频
    :param dst_folder: 保存的文件夹
    :param index: 每帧提取图片的数量
    :return: 无
    """
    video = cv2.VideoCapture()
    if not video.open(videopath):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = "{}/{:>04d}.jpg".format(dst_folder, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()
    # 打印出所提取帧的总数
    print("Totally save {:d} pics".format(index - 1))


def extract_fg():
    """
    提取前景视频图片
    :return:
    """
    import shutil
    try:
        shutil.rmtree(foreground_path)
    except OSError:
        pass
    import os
    os.mkdir(foreground_path)
    extract_frames(fg_video_path, foreground_path, EXTRACT_FREQUENCY)


def extract_bg():
    """
    提取背景视频图片
    :return:
    """
    import shutil
    try:
        shutil.rmtree(background_path)
    except OSError:
        pass
    import os
    os.mkdir(background_path)
    extract_frames(bg_video_path, background_path, EXTRACT_FREQUENCY)
