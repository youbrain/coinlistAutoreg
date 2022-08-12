import os
from time import sleep

import ffmpeg
from moviepy.editor import *
from selenium import webdriver

import cv2
import numpy as np


def open_chrome(swaped_vide_path):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("disable-signin-scoped-device-id")
    chrome_options.add_argument("use-fake-ui-for-media-stream")
    chrome_options.add_argument("auto-select-desktop-capture-source=Entire")
    chrome_options.add_argument("use-fake-device-for-media-stream")
    chrome_options.add_argument(r"use-file-for-fake-video-capture="+swaped_vide_path)
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_camera": 1
    })
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    return driver


def convert_video(inpt, output):
    ffmpeg.input(inpt).output(output).run()


def make_faceswap(passport_path, video_path, output_path):
    os.system(
        f'python main_video.py --src_img {passport_path} --video_path {video_path} --save_path {output_path} --show --correct_color'
    )


def video_from_img(img_path, output_path, duration):
    a = [ImageClip(img_path).resize(width=850).set_duration(duration)]
    video = concatenate(a, method="compose")
    return video


def concat_videos(video_1, video_2, video_path3, result_path):
    video_3 = VideoFileClip(video_path3)

    final_video = concatenate_videoclips([
        video_1, 
        video_2,
        video_3.resize(height=1450),
        video_1.resize(width=1920, height=1480)
    ], method="compose")

    final_video.write_videofile(result_path)



def prepere_video(video_path):
    video = VideoFileClip(video_path).fx( vfx.speedx, 0.25)
    video.write_videofile('1.mp4')
    os.remove(video_path)
    ffmpeg.input('1.mp4').output(video_path).run()
    os.remove('1.mp4')


if __name__ == '__main__':
    verefication_url = 'https://coinlist.netverify.com/web/v4/app/credential/0/identification/xdevice/nid?locale=en-US&mode=linked&s=q&authorizationToken=eyJhbGciOiJIUzUxMiIsInppcCI6IkdaSVAifQ.H4sIAAAAAAAAAB3OMQsCMQyG4f_S2UDjNWnj5nDCLQ7HITimaTo7OCjif7fn-vHw8n2Cv87PcArIE9Ex5UhCFA5BlzbWXKyLFgGpWiCZV1DGCFOugmpNCvvAtnof2iOTYBTQFDsklQjSUgFDpMpKUzfZ9T_dvUtOo1UdB8aJQQpFcMydODU22388tvdj6Ou83eZ1udzD9wf2GvF6swAAAA.ZrBMqXzMRyGv7FFx-D08pw2WeSEtzvAxcrd6tvo95hO0Y5vKorts-stnrINmZl182PfMgiTew6bba6b7P1Om1Q'
    dir_path = r'C:\tmp\FaceSwap\\'

    photo_front = dir_path+'passport_front.jpg'
    passport_video_front = dir_path+'passport_front.mp4'

    photo_back = dir_path+'passport_back.jpg'
    passport_video_back = dir_path+'passport_back.mp4'

    source_video = dir_path+r'src\mens\15.mp4'
    swaped_avi = dir_path+'swaped.avi'

    result = dir_path+'result.mp4'
    result_y4m = dir_path+'result.y4m'

    # make_faceswap(photo_front, source_video, swaped_avi)
    # prepere_video(swaped_avi)

    # video1 = video_from_img(photo_front, passport_video_front, 2)
    # video2 = video_from_img(photo_back, passport_video_back, 3)
    # try:
    #     os.remove(result)
    #     os.remove(result_y4m)
    # except FileNotFoundError:
    #     pass
    # concat_videos(video1, video2, swaped_avi, result)
    # convert_video(result, result_y4m)

    driver = open_chrome(result_y4m)
    # sleep(1)
    # driver.get(verefication_url)
    # sleep(1)
    # driver.find_element_by_id('guidance-btn').click()
    # sleep(1)
    # driver.find_element_by_id('camera-cropmark').click()
    # sleep(3)
    # driver.find_element_by_id('preview-confirm').click()
    # sleep(1)
    # driver.find_element_by_id('guidance-btn').click()
    # sleep(4)
    # driver.find_element_by_id('camera-cropmark').click()
    # sleep(1)
    # driver.find_element_by_id('preview-confirm').click()
    # sleep(3)
    # driver.find_element_by_id('guidance-btn').click()
    # print(1)
    # sleep(1)
    # driver.find_element_by_id('guidance-btn').click()
