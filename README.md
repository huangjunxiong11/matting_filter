# matting_filter
绿幕视频抠图合成和自定义视频滤镜美化

#### 项目说明

该项目可以进行前景绿幕视频抠图和背景视频融合的操作，还能给合成的视频增加自定义滤镜效果

#### 视频背景项目使用流程

##### 运行环境配置

###### 步骤1

建立虚拟环境，安装项目所需工具包，命令：

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement.txt
```

###### 步骤2

在文件movie_add_music.py文件中修改ffmpeg插件位置，插件已存放在该项目文件夹ffmpeg中，自行根据自己的系统进行修改即可。举例

```python
ffmpeg = 'ffmpeg/bin/ffmpeg'
```

##### 全局环境变量配置

###### 步骤1

将需要替换的背景视频和人物绿幕视频复制在data文件夹中，并命名为bg.mp4，fg.mp4

###### 步骤2

根据自己的需求修改配置文件config.py中的全局变量，注意前景视频的大小不能在背景视频中越界

###### 步骤3

启动run.py脚本

```python
python run.py
```

