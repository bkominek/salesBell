# coding: utf-8
from bluetooth import *
import pygame
import time
import datetime

pygame.init()
music_list = {'nexus 6p': {'file': '/home/pi/salesBell/assets/eye_of_the_tiger.mp3', 'duration': 246}, 'oneplusbloosh': {'file': '/home/pi/salesBell/assets/left_4_dead-tank_theme.mp3', 'duration': 59}, 'andrew lockwood (galaxy note4)': {'file': '/home/pi/salesBell/assets/trololol.mp3', 'duration': 17}, "sean's iphone": {'file': '/home/pi/salesBell/assets/indiana_jones.mp3', 'duration': 146}, "clinton's iphone": {'file': '/home/pi/salesBell/assets/john_denver-country_roads.mp3', 'duration': 181}, "erin's pixel": {'file': '/home/pi/salesBell/assets/backstreet_boys-everybody.mp3', 'duration': 290}, 'zephyr': {'file': '/home/pi/salesBell/assets/duel_of_the_fates.mp3', 'duration': 17}}

print "scanning for bluetooth devices..."

target_devices = ["nexus 6p", "oneplusbloosh", "andrew lockwood (galaxy note4)", "sean’s iphone", "clinton’s iphone", "erin’s pixel", "zephyr"]
found_devices = []
search = True

while search:
    nearby_devices = discover_devices(lookup_names = True)

    for addr, name in nearby_devices:
        lower_name = name.lower()
        if lower_name in target_devices and lower_name not in found_devices:
            print "playing sound for %s" % (name)
            found_devices.append(lower_name)
            pygame.mixer.music.load(music_list[lower_name]['file'])
            pygame.mixer.music.play()
            time.sleep(music_list[lower_name]['duration'])

    now = datetime.datetime.now()
    if now.hour > 10 and now.minute > 30:
        search = False
