import subprocess
from config import fg_video_path, music_path, out_video, out

# 全部变量
ffmpeg = 'D:/ffmpeg/bin/ffmpeg'  # ffmpeg插件的位置


def get_videomp3(file_name=fg_video_path, outfile_name=music_path):
    """
    从视频file_name中提取音频outfile_name
    :param file_name: 输入的视频
    :param outfile_name: 输出的音频
    :return: 无
    """
    # outfile_name = file_name.split('.')[0] + '.mp3'
    cmd = ffmpeg + ' -i ' + file_name + ' -f mp3 ' + outfile_name
    # 'D:/ffmpeg/bin/ffmpeg -i data/fg.mp4 -f mp3 data/fg.mp3'
    subprocess.call(cmd, shell=True)


def video_add_mp3(file_name=out_video, mp3_file=music_path, outfile_name=out):
    """
    给视频增加音频
    :param file_name: 需要配音频的视频
    :param mp3_file: 音频
    :param outfile_name: 输出的音频
    :return: 无
    """
    # outfile_name = file_name.split('.')[0] + '-txt.mp4'
    cmd = ffmpeg + ' -i ' + file_name + ' -i ' + mp3_file + ' -strict -2 -f mp4 ' + outfile_name
    # 'D:/ffmpeg/bin/ffmpeg -i data/fg_settle.avi -i data/fg.mp3 -strict -2 -f mp4 data/fg_settle-txt.mp4'
    subprocess.call(cmd, shell=True)
