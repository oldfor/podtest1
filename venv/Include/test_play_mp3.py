#_*_encoding='utf-8'_*_

'''
author:@chengxm
time:2020/8/19 15:59
'''

from pygame import mixer # Load the required library


def play_music(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
