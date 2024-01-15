import os
import sys

main_path = "../"
error = [0, 0]

def getpath():
    """获取文件夹内的.mp4文件地址"""
    path = main_path
    files = os.listdir(main_path)
    for file in files:
        if file.find(".mp4") != -1:
            path += file
    return path

#预防错误
try:
    import cv2
except ModuleNotFoundError:
    print("Module cv2 required but not installed.")
    error[0] = 1
try:
    from alive_progress import alive_bar
except ModuleNotFoundError:
    print("Module alive_progress required but not installed.")
    error[0] = 1
if getpath() == main_path:
    print("You should put your .mp4 file in the same folder with run.sh !")
    error[1] = 1

if error[0] != 0 or (error[1] == 1 and sys.argv[1] == '1'):
    print("Press [Enter] to quit.")
    input()
    exit(1)

def video_to_frames():
    """将视频逐帧读取，并把每一帧储存到文本文件里"""
    path = getpath()                                                                              #  使用opcenv2读取目录中整个视频，并获取总帧数
    print("Transforming...")                                                                      #
    video = cv2.VideoCapture(path)                                                                #
    frame_ct = int(video.get(7))                                                                  #
    
    with alive_bar(frame_ct) as bar:
        for i in range(frame_ct):
            success, frame = video.read()                                                         #  将获取的帧储存在目录中，并用灰度图模式读取
            cv2.imwrite(main_path+"temp.jpg", frame)                                              #
            frame = cv2.imread(main_path+"temp.jpg", cv2.IMREAD_GRAYSCALE)                        #                                                          

            if i < 1:                                                                             #  第一次运行循环的时候计算画幅的大小并对格栅做出调整
                height, width = frame.shape                                                       #
                print(height, width)                                                              #
                s = max([int(width/97)+1, int(height/55)+1])                                      #
                width -= width%s                                                                  #
                height -= height%s                                                                #
                vs = int(height/s)                                                                #
                hs = int(width/s)                                                                 #
                gnome = int((97 - hs) / 2) * "  "                                                 #
                dis = max([54 - vs, 0])
            
            with open(main_path+"frames/"+str(i)+".frame", "a") as target:                        #  生成并打开文件，将获取到的帧内容储存在文本文件中
                symbols = ["..","==", "##", "░░", "▒▒", "▞▞", "▓▓", "██"]                         #
                for y in range(vs):                       #  格栅化读取帧内容                        #
                    target.write(gnome)                   #                                       #
                    for x in range(hs):                   #                                       #
                        grey = int(frame[s*y, s*x]/36.4)  #                                       #                    
                        target.write(symbols[grey])                                               #
                    target.write('\n')                                                            #
                for i in range(dis):                                                              #
                    target.write("\n")                                                            #
            bar()                                                                                 #
    
    with open(main_path+"frames/disp.format", "a") as format:                                     #  生成并打开格式文件，将视频总帧数记录
        format.write(str(frame_ct))                                                               #
    os.remove(main_path+"temp.jpg")                                                               #  删除生成的临时文件

def initiallize():
    """初始化, 即删除现有的frame文件"""
    print("Initiallizing...")
    files = os.listdir(main_path+"frames")
    with alive_bar(len(files)) as bar:
        for file in files:
            os.remove(main_path+"frames/" + file)
            bar()
            
initiallize()
if(sys.argv[1] == '1'):
    video_to_frames()
print("Done! Press [Enter] to continue.")
input()

os.system('sh ../run.sh')