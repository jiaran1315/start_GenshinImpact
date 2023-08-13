import subprocess
from PIL import ImageGrab
import configparser
import time  # 需要导入 time 模块


# 检测屏幕是否全白
def is_screen_all_white(image):
    white_threshold = 200  # 阈值，用于判断颜色是否为白色
    for pixel in image.getdata():
        # 检查每个像素的 R、G、B 值是否都在白色阈值以上
        if pixel[0] < white_threshold or pixel[1] < white_threshold or pixel[2] < white_threshold:
            return False
    return True


# 启动原神
def start_genshinimpact(genshinimpact_path):
    subprocess.Popen(genshinimpact_path)


# 主程序
def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    genshinimpact_path = config.get("Paths", "genshinimpact_path")

    screen_width = 1920
    screen_height = 1080

    while True:
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))

        if is_screen_all_white(screenshot):
            start_genshinimpact(genshinimpact_path)
            break
        else:
            print("未检测到屏幕全白")

        # 每次检测之后等待 0.5 秒
        time.sleep(0.5)


if __name__ == "__main__":
    main()
