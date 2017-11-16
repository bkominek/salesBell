from bluetooth import *

print "performing inquiry..."

target_devices = ["Nexus 6P"]
found_devices = []
nearby_devices = discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)

for addr, name in nearby_devices:
  if name in target_devices and name not in found_devices:
    found_devices.append(name)
  print " %s - %s" % (addr, name)

print found_devices

music = pyglet.resource.media('assets/woo.mp3')
music.play()

pyglet.app.run()