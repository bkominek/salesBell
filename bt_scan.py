from bluetooth import *

print "performing inquiry..."

target_devices = ["Nexus 6P"]
found_devices = []

nearby_devices = discover_devices(lookup_names = True)
print nearby_devices
print "found %d devices" % len(nearby_devices)

for name, addr in nearby_devices:
  if name in target_devices:
    found_devices.append(name)
  print " %s - %s" % (addr, name)

print found_devices