# coding: utf-8
from bluetooth import *
import pygame
import time
import datetime

pygame.init()
music_list = {'nexus 6p': {'file': '/home/pi/salesBell/assets/eye_of_the_tiger.mp3', 'duration': 28}, 'oneplusbloosh': {'file': '/home/pi/salesBell/assets/left_4_dead-tank_theme.mp3', 'duration': 59}, 'andrew lockwood galaxy note4': {'file': '/home/pi/salesBell/assets/trololol.mp3', 'duration': 17}, "seans iphone": {'file': '/home/pi/salesBell/assets/indiana_jones.mp3', 'duration': 36}, "clintons iphone": {'file': '/home/pi/salesBell/assets/stone_cold.mp3', 'duration': 20}, "erins pixel": {'file': '/home/pi/salesBell/assets/backstreet_boys-everybody.mp3', 'duration': 290}, 'zephyr': {'file': '/home/pi/salesBell/assets/duel_of_the_fates.mp3', 'duration': 17}, 'marquis iphone': {'file': '/home/pi/salesBell/assets/poison.mp3', 'duration': 75}, 'nan phone': {'file': '/home/pi/salesBell/assets/chinese_zither.mp3', 'duration': 23}}

print "scanning for bluetooth devices..."

target_devices = ["nexus 6p", "oneplusbloosh", "andrew lockwood galaxy note4", "seans iphone", "clintons iphone", "erins pixel", "zephyr", "marquis iphone", "nan phone"]
found_devices = []
search = True

while search:
    # try:
    #     nearby_devices = discover_devices(lookup_names = True)
    # except:
    nearby_devices = []

    for addr, name in nearby_devices:
        lower_name = name.lower()
        lower_name = lower_name.strip()
        replacers = "'()’"
        for char in replacers:
            lower_name = lower_name.replace(char,"")

        if lower_name in target_devices and lower_name not in found_devices:
            print "playing sound for %s" % (lower_name)
            found_devices.append(lower_name)
            pygame.mixer.music.load(music_list[lower_name]['file'])
            pygame.mixer.music.play()
            time.sleep(music_list[lower_name]['duration'])
            print "sound finished"

    now = datetime.datetime.now()
    if now.hour > 10 and now.minute > 30:
        search = False
