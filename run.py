from movie_extract import extract_bg, extract_fg
from picture_matting import hjx_matting
from picture_tobe_movie import make_phone_tobe_video
from movie_add_music import get_videomp3, video_add_mp3
import time

if __name__ == '__main__':
    """
    运行该脚本的时候需要先根据自己的实际需求更改配置文件config
    """
    start = time.clock()
    # extract_fg()  # 将前景视频提取变成前景图片序列集，20s
    # extract_bg()  # 将背景视频提取变成背景图片序列集，30s
    # hjx_matting()  # 将提取出来的视频进行抠图和合成操作变成图片序列集，1402s
    # make_phone_tobe_video()  # 将图片序列集合成视频，根据背景视频的帧数和大小，18.5s
    # get_videomp3()  # 将视频的音频提取出来，并进行保存，1.2s
    video_add_mp3()  # 将提取出来的视频和音频进行合成输出最终转换视频，8.1s
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))
