from bluetooth import *
import pygame
import time
import datetime

pygame.init()
music_list = {'Nexus 6P': {'file': 'assets/woo.mp3', 'duration': 3}}

print "scanning for bluetooth devices..."

target_devices = ["Nexus 6P"]
found_devices = []
search = True

while search:
  nearby_devices = discover_devices(lookup_names = True)

  for addr, name in nearby_devices:
    if name in target_devices and name not in found_devices:
      print "playing sound for %s" % (name)
      found_devices.append(name)
      pygame.mixer.music.load(music_list[name]['file'])
      pygame.mixer.music.play()
      time.sleep(music_list[name]['duration'])

  now = datetime.datetime.now()
  if now.hour > 10 and now.minute > 30:
    search = False
